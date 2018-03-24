from django import forms
from .models import *

class ArticlesForm(forms.ModelForm):

    class Meta:
        model = Articles
        exclude = ["date"]
