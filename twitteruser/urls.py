from django.urls import path
from twitteruser import views

app_name = 'twitteruser'

urlpatterns = [
    path('listall/', views.TwitterUserListView.as_view(), name='twitter_list_view'),
    path('<pk>/', views.TwitterUserDetailView.as_view(), name='user_detail_view'),
    # path('follow/<str:user_name>', views.follow_view, name='follow_view'),
]
