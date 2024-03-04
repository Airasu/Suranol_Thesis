from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post-list"),  # /posts: shows all posts in the database
]