from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',
    auth_views.LoginView.as_view(template_name='registration/login.html'),
    name='login'),
    path(r'logout/', auth_views.LogoutView.as_view(template_name='accounts/registration/logout.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    
    path(
        'register/staff',
        views.TeacherSignUpView.as_view(), name='teacher-registration'
        ),
    
    path(
        'staff_verify/<int:pk>',
        views.StaffVerificationView.as_view(),
        name='staff-verification'
        ),
    path('dashboard/', views.profile, name='user-profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)