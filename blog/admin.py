from django.contrib import admin
from .models import Post, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_datetime'
    empty_value_display = '-empty-'
    list_display = ['title', 'counted_view', 'status', 'login_require', 'published_datetime', 'created_datetime', 'modified_datetime']
    list_filter = ('status',)
    search_fields = ['title','content']
    list_editable = ['login_require']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_datetime'
    empty_value_display = '-empty-'
    list_display = ['name', 'subject', 'email', 'approved', 'created_datetime', 'modified_datetime']
    list_filter = ('approved',)
    search_fields = ['name', 'subject']