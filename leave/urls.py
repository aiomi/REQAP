from django.urls import path

from . import views

urlpatterns = [
    path('apply-for-leave', views.apply_for_leave, name='leave-apply')
]