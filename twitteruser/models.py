from twitterclone import settings
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    pass


def __str__(self):
    return self.username
