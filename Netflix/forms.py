from django import forms
from Netflix.models import Movies,Categories
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields="__all__"

class CategoriesForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields="__all__"