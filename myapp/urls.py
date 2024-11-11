
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('services', views.service, name='services'),
    path('starter', views.starter, name='starter'),
]
