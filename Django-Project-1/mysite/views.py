from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Profil


def index(request):
    profil = Profil.objects.all
    context = {
        'judul': 'Django-Project',
        'subjudul': 'selamat datang di Blog Django Project',
        'Profil': profil,
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],

        ]
    }
    return render(request, 'index.html', context)
