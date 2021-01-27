# views blog
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'blog',
        'subtitle': 'Selamat datang di Blog saya',
        'content': 'ini adalah halaman index blog',
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'about',
        'subtitle': 'Selamat datang about di Blog saya',
        'content': 'ini adalah halaman about blog',
    }
    return render(request, 'blog/index.html', context)
