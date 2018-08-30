from django import forms
from .models import City


class NameForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']



