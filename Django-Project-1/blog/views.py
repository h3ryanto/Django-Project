from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello worls. You're at the Blog Index")
