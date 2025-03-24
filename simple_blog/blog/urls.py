from django.urls import path
from .views import list_blog_posts, create_blog_post

urlpatterns = [
    path('', list_blog_posts, name='list_blog_posts'),
    path('create/', create_blog_post, name='create_blog_post'),
]