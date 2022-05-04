from django.shortcuts import render
from .models import Post

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request, 'blog_index.html',context)

def blog_detail(request, pk):

    posts = Post.objects.get(pk=pk)
    context = {
        'posts': posts
    }
    return render(request,'blog_detail.html',context)

