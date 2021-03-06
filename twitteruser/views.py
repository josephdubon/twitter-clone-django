from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView

from tweet.models import Tweet
from .models import TwitterUser


def follow_twitteruser(request, user_id):
    # get id of users profile you are on
    user = request.user
    follow_user = TwitterUser.objects.get(id=user_id)
    # then add him to followers list
    user.followers.add(follow_user)
    user.save()
    # then redirect home
    return redirect('home')


def unfollow_twitteruser(request, user_id):
    # get id of users profile you are on
    user = request.user
    follow_user = TwitterUser.objects.get(id=user_id)
    # then add him to followers list
    user.followers.remove(follow_user)
    user.save()
    # then redirect home
    return redirect('home')


class TwitterUserListView(ListView):
    model = TwitterUser
    template_name = 'user_list.html'
    context_object_name = 'twitterusers'  # object_list as default


def twitter_user_detail(request, user_id):
    twitteruser_obj = request.user
    follow_user = TwitterUser.objects.get(id=user_id)
    tweets = Tweet.objects.filter(author=follow_user)
    tweets_total = Tweet.objects.filter(author=follow_user).count()
    followers_total = follow_user.followers.count()

    return render(
        request,
        'author_detail.html',
        {
            'twitteruser_obj': twitteruser_obj,
            'follow_user': follow_user,
            'tweets': tweets,
            'tweets_total': tweets_total,
            'followers_total': followers_total,
        }
    )
