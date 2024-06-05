from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_datetime

    def location(self, item):
        return reverse("blog:detail_view", kwargs={"pk": item.id})
        