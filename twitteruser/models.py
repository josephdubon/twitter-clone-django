from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    followers = models.ManyToManyField(
        'self',
        related_name='follows',
        symmetrical=False,
        blank=True
    )
    bio = models.TextField(default='User has not written bio yet...')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def twitteruser_tweets(self):
        return self.twitteruser_tweets()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-create_time',)
