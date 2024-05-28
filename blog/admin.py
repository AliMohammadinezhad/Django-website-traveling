from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_datetime'
    empty_value_display = '-empty-'
    list_display = ['title', 'counted_view', 'status', 'published_datetime', 'created_datetime', 'modified_datetime']
    list_filter = ('status',)
    search_fields = ['title','content']
