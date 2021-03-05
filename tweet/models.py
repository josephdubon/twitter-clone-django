from django.db import models

from twitterclone import settings


class Tweet(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author',
        null=True
    )
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=140)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.author} |{self.title} | {self.body})'

    class Meta:
        ordering = ('-create_time',)
