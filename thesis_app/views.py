from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post



def post_list(request):
    posts = Post.published.all()
    
    return render(request, "posts/list.html", {"posts":posts})


    

def post_detail(requests, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    return render(requests, "thesis_app/post/detail.html", {"post":post})