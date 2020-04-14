from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('make_request/', views.make_request, name='make-request'),
]