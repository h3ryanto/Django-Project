from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url('about', views.about, name='about'),
    url('', views.index, name='index'),

]
