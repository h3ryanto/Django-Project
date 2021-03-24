from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url('', views.index, name='index'),
]