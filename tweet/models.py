from django.db import models
from django.urls import reverse
from django.utils import timezone

from twitterclone import settings


# class Author(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True)
#
#     def __str__(self):
#         return self.user
#

class Tweet(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author',
        null=True
    )
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=140)
    create_time = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f'({self.author} |{self.title} | {self.body})'
