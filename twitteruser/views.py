from django.db import models
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView

from tweet.models import Tweet
from .models import TwitterUser


# # Author detail view
# def author_detail_view(request, author_id):
#     author_obj = TwitterUser.objects.get(id=author_id)
#     tweets = Tweet.objects.filter(author=author_id).order_by('-create_time')
#
#     return render(request, 'author_detail.html', {
#         'author': author_obj,
#         'tweets': tweets
#     }
#                   )


class TwitterUserListView(ListView):
    model = TwitterUser
    template_name = 'user_list.html'
    context_object_name = 'twitterusers'  # object_list as default

    # def get_queryset(self):
    # return TwitterUser.objects.all().exclude(self)


class TwitterUserDetailView(DetailView):
    model = TwitterUser
    template_name = 'author_detail.html'
    context_object_name = 'twitterusers'  # object_list as default

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_twitteruser = TwitterUser.objects.get(pk=pk)
        return view_twitteruser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_twitteruser = self.get_object()
        my_twitter = TwitterUser.objects.get(username=self.request.user)
        if view_twitteruser in my_twitter.followers.all():
            follow = True
        else:
            follow = False
        context['follow'] = follow
        return context
