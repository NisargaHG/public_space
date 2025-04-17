# space/urls.py
from django.urls import path
from . import views

app_name = 'space'

urlpatterns = [
    path('post/', views.post_tweet_view, name='post_tweet'),  
    path('post-limit/', views.post_limit_view, name='post_limit'),
]
