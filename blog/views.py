from django.shortcuts import render, get_object_or_404

from .models import Blog
from .models import Author
from .models import Entry

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})

def possiblechange(request):
    blogs = Blog.objects
    return render(request, 'blog/possiblechange.html', {'blogs':blogs})

def Aboutpage(request):
    blogs = Blog.objects
    entry = Entry.objects
    return render(request, 'blog/About-Jonas-Zuckerman.html', {'blogs':blogs}, {'entry':entry})

def detailentry(request, entry_id):
    detailentry = get_object_or_404(Entry, pk=entry_id)
    return render(request, 'blog/detailentry.html', {'entry':detailentry})
