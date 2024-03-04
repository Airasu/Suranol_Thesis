from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator



def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    # __import__('pdb').set_trace()
    return render(request, "posts/list.html", {"posts":posts})


    
def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post_slug, publish__year=year, publish__month=month, publish__day=day)

    return render(request, "posts/detail.html", {"post": post})

