from django.shortcuts import render, reverse

from tweet.models import Tweet
from .models import TwitterUser


# Author detail view
def author_detail_view(request, author_id):
    author_obj = TwitterUser.objects.get(id=author_id)
    tweets = Tweet.objects.filter(author=author_id).order_by('-create_time')

    return render(request, 'author_detail.html', {
        'author': author_obj,
        'tweets': tweets
    }
                  )
