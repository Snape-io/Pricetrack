from django import forms
from .models import Link
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields =('url',)

