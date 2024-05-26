from django.shortcuts import render

def blog_list_view(request):
    return render(request, 'blog/blog-home.html')

def blog_detail_view(request):
    return render(request, 'blog/blog-single.html')