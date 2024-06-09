from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

from .forms import CommentForm
from .models import Post, Comment


def blog_list_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(published_datetime__lte=now()).select_related('author').prefetch_related('category')

    # Filter posts by category
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs.get("cat_name"))

    if kwargs.get("tag_name"):
        posts = posts.filter(tags__name__in=[kwargs.get("tag_name")])

    # Paginate posts
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)


def blog_detail_view(request, pk):
    queryset = Post.objects.filter(status=True, published_datetime__lte=now())

    post = get_object_or_404(queryset, id=pk)
    post.counted_view += 1
    post.save()

    next_post = queryset.filter(id__gt=post.id).order_by("id").first()
    previous_post = queryset.filter(id__lt=post.id).order_by("id").last()

    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_datetime')

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "your comment has been sent successfully")
        else:
            messages.error(request, "your comment has not been sent")

    comment_form = CommentForm()

    context = {"post": post,
               "next_post": next_post,
               "previous_post": previous_post,
               "comments": comments,
               "comment_form": comment_form}
    return render(request, "blog/blog-single.html", context)


def blog_search_view(request):
    posts = Post.objects.filter(status=True, published_datetime__lte=now())
    if request.method == "GET":
        if s := request.GET.get("q"):
            posts = posts.filter(content__contains=s)

    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
