from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TwitterUser


class TwitterUserCreationForm(UserCreationForm):
    class Meta:
        model = TwitterUser
        fields = ('username', 'email')


class TwitterUserChangeForm(UserChangeForm):
    class Meta:
        model = TwitterUser
        fields = ('username', 'email')
