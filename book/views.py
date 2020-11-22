from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django import template

register = template.Library()

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('book_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def DisLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('book_id'))
    post.likes.remove(request.user)
    post.likes.remove(1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'editedaboutus.html')

def booksearch(request):
    return render(request, 'index.html')

def books(request):
    return render(request, 'books.html')

def children(request):
    context = {
        'books': Post.objects.filter(categories="Children"),
    }
    return render(request, 'book.html', context)

def teen(request):
    context = {
        'books': Post.objects.filter(categories="Teen"),
    }
    return render(request, 'book.html', context)

def policy(request):
    return render(request, 'policy.html')
