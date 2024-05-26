from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list_view, name='list_view'),
    path('single/', views.blog_detail_view, name='detail_view'),
]
