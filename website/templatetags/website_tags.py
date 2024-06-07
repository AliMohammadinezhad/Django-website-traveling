from django import template
from django.utils.timezone import now

from blog.models import Post

register = template.Library()


@register.inclusion_tag("website/website-blog.html")
def website_blog_latest_posts(arg=6):
    posts = Post.objects.filter(status=True, published_datetime__lte=now()).order_by(
        "-published_datetime"
    ).select_related('author').prefetch_related('category')[:arg]
    return {"posts": posts}
