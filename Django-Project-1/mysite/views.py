from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'judul': 'Django-Project',
        'subjudul': 'selamat datang di Blog Django Project',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'index.html', context)
