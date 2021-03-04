from django.urls import path

from twitteruser import views

urlpatterns = [
    path('<int:author_id>/', views.author_detail_view, name='author_detail'),
]
