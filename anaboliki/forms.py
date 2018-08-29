from django import forms
from .models import City


class NameForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']


#class RegistrationForm(forms.ModelForm):
  #  email = forms.EmailField(max_length=254, required=True)

  #  class Meta:

   #     model = User
     #   fields = ('username', 'email', 'password1', 'password2',)
