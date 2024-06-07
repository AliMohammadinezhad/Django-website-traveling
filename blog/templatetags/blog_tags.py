from django import template
from django.utils.timezone import now

from ..models import Category, Post, Comment

register = template.Library()


@register.inclusion_tag("blog/blog-latest-post.html")
def latestposts(arg=3):
    posts = Post.objects.filter(status=True, published_datetime__lte=now()).order_by(
        "-published_datetime"
    ).prefetch_related('category').select_related('author')[:arg]
    return {"posts": posts}


@register.inclusion_tag("blog/blog-category.html")
def post_categories():
    posts = Post.objects.filter(status=True, published_datetime__lte=now()).select_related('author').prefetch_related(
        'category').order_by('-published_datetime')
    categories = Category.objects.prefetch_related('post_set')
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}


@register.simple_tag(name='comment_count')
def comment_count(pid):
    return (Comment.objects.filter(post=pid, approved=True)
            .prefetch_related('post__category__post_set')
            .select_related('post__author').count())
