from django.urls import path
from . import views

app_name = "thesis_app"
urlpatterns = [
    path("", views.post_list, name="post-list"),  # /posts: shows all posts in the database
   # path("<int:id>", views.post_detail, name="post_detail")
   path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),

   path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
]

