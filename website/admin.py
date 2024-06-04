from django.contrib import admin

from .models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_datetime']
    list_filter = ('email',)
    search_fields = ['name', 'message']
    date_hierarchy = 'created_datetime'

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    search_fields = ['email', 'id']
