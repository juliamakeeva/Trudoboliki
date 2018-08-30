from django.shortcuts import render
from .models import City, Item
from .forms import NameForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages


def main(request):
    return render(request, 'anaboliki/index.html', )


def catalog(request):
    towns = City.objects.filter(is_approved=True).order_by('name')

    if 'search' in request.GET:
        towns = towns.filter(name__contains=request.GET['search'])

    return render(request, 'anaboliki/catalog.html', {
        'towns': towns
    })


def city(request, town):
    return render(request, 'anaboliki/cities.html', {
        'town': City.objects.get(id=town)
    })


def new_town(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_city = City(
                name=form.cleaned_data['name']
            )
            new_city.save()
            new_city.user = request.user
            new_city.save()

            messages.add_message(
                request, messages.INFO,
                "Город {} успешно добавлен".format(new_city.name))

            return HttpResponseRedirect('/new_town/new/')
    else:
        form = NameForm()
    return render(request, 'anaboliki/new_town.html',
                  {
                      'form': form

                  })


def edit_town(request, town):
    if not City.objects.filter(id=town).exists():
        return HttpResponseNotFound()

    city = City.objects.get(id=town)
    if request.user != city.user:
        return HttpResponseNotFound()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST, instance=city)
        # check whether it's valid:
        if form.is_valid():
            inst = form.save()
            inst.user = request.user
            inst.save()

            messages.add_message(
                request, messages.INFO,
                "Город {} успешно изменен".format(inst.name))

            return HttpResponseRedirect('/new_town/new/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm(instance=city)
    return render(request, 'anaboliki/new_town.html',
                  {
                      'form': form

                  })


