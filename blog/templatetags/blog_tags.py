from django import template
from django.utils.timezone import now

from ..models import Category, Post

register = template.Library()


@register.inclusion_tag("blog/blog-latest-post.html")
def latestposts(arg=3):
    posts = Post.objects.filter(status=True, published_datetime__lte=now()).order_by(
        "published_datetime"
    )[:arg]
    return { "posts" : posts }


@register.inclusion_tag("blog/blog-category.html")
def post_categories():
    posts = Post.objects.filter(status=True, published_datetime__lte=now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return { "categories" : cat_dict }    
    