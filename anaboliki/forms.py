from django import forms
from .models import City


# class NameForm(forms.Form):
    # name = forms.CharField(label="City", max_length=100)

class NameForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']