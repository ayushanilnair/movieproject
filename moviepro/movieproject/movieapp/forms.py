from django import forms
from .models import Movie


class Mform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','description','year']