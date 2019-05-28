from django import forms
from django.core import validators
from django.forms import CharField

from .models import Show


# hmm...should this have been a Model Form?
# Implemented using forms.Form
# class ShowForm(forms.Form):
#     title = forms.CharField(label='TV Show Title', max_length=100)
#     network = forms.CharField(label='TV Network', max_length=100)
#     description = forms.CharField(label='Description', max_length=100)
#     release_date = forms.DateField(label="Release date")

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ["title", "network", "description", "release_date"]


class SlugField(CharField):
    default_validators = [validators.validate_slug]
