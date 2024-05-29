import datetime
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .models import Post


def blog_list_view(request):

    time = now()

    posts = Post.objects.filter(status=True)
    posts = posts.filter(published_datetime__lte=time)

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_detail_view(request, pk):

    post = get_object_or_404(Post, id=pk)
    post.counted_view += 1
    post.save()

    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
