from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    # __import__('pdb').set_trace()
    return render(request, "posts/list.html", {"posts":posts})
    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)

    return render(request, "posts/detail.html", {"post":post})