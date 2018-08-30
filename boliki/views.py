from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


def auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            raise ValueError('eeeeee')

    else:
        form = AuthenticationForm()
    return render(request, 'auth.html',
                 {
                        'form': form

                })


class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)
