from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World! ini adalah halam index")


def about(request):
    return HttpResponse("Hello World! ini adalah halaman about")
