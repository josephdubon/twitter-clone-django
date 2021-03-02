from django.contrib import admin

from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'body',
    )


admin.site.register(Tweet, TweetAdmin)
