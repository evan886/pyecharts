from django.contrib import admin
from django.urls import path
from . import  views

from django.conf.urls import url

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
]
