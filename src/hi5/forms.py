from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accouts.models import *

class accountForm(ModelForm):
    class Meta:
        model=account
        fields='__all__'
        exclude=['username']

class CreateuserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']