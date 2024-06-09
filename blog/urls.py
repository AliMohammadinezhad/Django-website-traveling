from django.urls import path
from . import views
from .feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list_view, name='list_view'),
    path('category/<str:cat_name>/', views.blog_list_view, name='category'),
    path('tag/<str:tag_name>/', views.blog_list_view, name='tag'),
    path('search/', views.blog_search_view, name='search'),
    path('<int:pk>/', views.blog_detail_view, name='detail_view'),
    path("rss/feed/", LatestEntriesFeed()),
]
