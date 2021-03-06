from django.urls import path
from twitteruser import views

app_name = 'twitteruser'

urlpatterns = [
    path('listall/', views.TwitterUserListView.as_view(), name='twitter_list_view'),
    path('<int:user_id>/', views.twitter_user_detail, name='user_detail_view'),
    path('follow/<int:user_id>/', views.follow_twitteruser, name='follow_view'),
    path('unfollow/<int:user_id>/', views.unfollow_twitteruser, name='unfollow_view'),
]
