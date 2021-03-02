from django.urls import path

from tweet import views

urlpatterns = [
    path('author/<int:author_id>/', views.author_detail_view, name='author_detail'),
    path('<int:tweet_id>/', views.tweet_detail_view, name='tweet_detail'),
    path('create-tweet/', views.create_tweet, name='create_tweet'),
    path('', views.tweet_list_view, name='tweet_list'),
]
