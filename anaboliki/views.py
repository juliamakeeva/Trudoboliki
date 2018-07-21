from django.shortcuts import render
from .models import City


def main(request):
    return render(request, 'anaboliki/index.html',)


def catalog(request):
    return render(request, 'anaboliki/catalog.html', {
        'towns': City.objects.all().order_by('name')
    })


def city(request, town):
    return render(request, 'anaboliki/cities.html', {
        'town': City.objects.get(id=town)
    })
