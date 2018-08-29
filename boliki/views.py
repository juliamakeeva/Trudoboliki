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

    success_url = "/login/"

    template_name = "register.html"

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)

#def register(request):
    #if request.method == 'POST':
       # form = RegistrationForm(request.POST)
       # if form.is_valid():

        #    form.save()
        #    username = form.cleaned_data.get('username')
        #    raw_password = form.cleaned_data.get('password1')
        #    user = authenticate(username=username, password=raw_password)
        #    login(request, user)
        #    messages.success(request, 'Вы успешно зарегистрировались')
        #    return redirect('/')
    #else:
     #   form = RegistrationForm()
    #return render(request, 'anaboliki/register.html',
     #             {
      #                  'form': form,
      #          })