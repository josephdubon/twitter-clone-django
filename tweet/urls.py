from django.urls import path

from tweet import views

urlpatterns = [
    path('<int:tweet_id>/', views.tweet_detail_view, name='tweet_detail'),
    path('create-tweet/', views.create_tweet, name='create_tweet'),
    path('', views.tweet_list_view, name='tweet_list'),
]
