from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',
    auth_views.LoginView.as_view(template_name='registration/login.html'),
    name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='accounts/registration/logout.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

]