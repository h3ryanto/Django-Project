from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World! ini adalah halaman index")


def about(request):
    return HttpResponse("Hello World! ini adalah halaman about")
