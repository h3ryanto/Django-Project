# views blog
from django.shortcuts import render

# Create your views here.


def index(request):
    contex:
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')
