import datetime
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .models import Post


def blog_list_view(request):

    posts = Post.objects.filter(status=True)
    posts = posts.filter(published_datetime__lte=now())

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_detail_view(request, pk):
    queryset = Post.objects.filter(status=True, published_datetime__lte=now())
    
    post = get_object_or_404(queryset, id=pk)
    post.counted_view += 1
    post.save()
    
    next_post = queryset.filter(id__gt=post.id).order_by('id').first()   
    previous_post = queryset.filter(id__lt=post.id).order_by("-id").last()   
    
       
         

    context = {"post": post, "next_post": next_post, "previous_post": previous_post}
    return render(request, "blog/blog-single.html", context)
