from django import template
from django.utils.timezone import now

from ..models import Category, Post

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
        'category').order_by('-published_datetime').prefetch_related('category').select_related('author')
    categories = Category.objects.prefetch_related('post_set').all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}
