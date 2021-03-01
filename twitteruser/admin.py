from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import TwitterUserChangeForm, TwitterUserCreationForm
from .models import TwitterUser


class TwitterUserAdmin(UserAdmin):
    add_form = TwitterUserCreationForm
    form = TwitterUserChangeForm
    model = TwitterUser
    list_display = ['email', 'username', ]


admin.site.register(TwitterUser, TwitterUserAdmin)
