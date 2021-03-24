from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('accounts/login/', views.login_user, name= 'login_user'),
    url('inventory', include('inventory.urls',namespace = 'inventory')),
    url('login_user/', views.login_user, name= 'login_user'),
    url('logoutView/', views.logoutView, name= 'logoutView'),
    path('', views.index, name= 'index'),
    path('admin/', admin.site.urls),
    
]
