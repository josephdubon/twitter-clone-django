from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from twitteruser.models import TwitterUser
from .models import Tweet
from .forms import CreateTweetForm
from twitterclone import settings


# Home tweet list view
@login_required
def tweet_home_view(request):
    twitteruser_obj = request.user
    tweets_total = Tweet.objects.filter(author=twitteruser_obj).count()
    followers_total = twitteruser_obj.followers.count()
    tweets = Tweet.objects.all().order_by('-create_time')
    tweets = [tweet for tweet in tweets if tweet.author in request.user.followers.all() or request.user == tweet.author]
    return render(request, 'home.html', {
        'twitteruser_obj': twitteruser_obj,
        'tweets_total': tweets_total,
        'followers_total': followers_total,
        'tweets': tweets,
    }
                  )


# Tweet list view
@login_required
def tweet_list_view(request):
    tweets = Tweet.objects.all().order_by('-create_time')
    return render(request, 'tweet_list.html', {
        'tweets': tweets,
    }
                  )


# Tweet detail view
def tweet_detail_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)

    return render(request, 'tweet_detail.html', {
        'tweet': tweet
    }
                  )


# Create tweet view
@login_required
def create_tweet(request):
    context = {}

    if request.method == "POST":
        form = CreateTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Tweet.objects.create(
                title=data['title'],
                author=request.user,
                body=data['body'],
            )
            if new_ticket:
                return HttpResponseRedirect(reverse('home'))

    form = CreateTweetForm()
    context.update({'form': form})
    return render(
        request,
        'create_tweet.html',
        context
    )
