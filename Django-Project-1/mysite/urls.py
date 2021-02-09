from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    url('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
