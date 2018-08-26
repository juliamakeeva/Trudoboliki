from django.contrib.auth.forms import AuthenticationForm


def auth(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        raise ValueError('eeeeee')



        # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()
    return render(request, 'auth.html',
                 {
                        'form': form

                })