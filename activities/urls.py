from django.urls import path, include,re_path

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('request-transcript/', views.request_transcripts, name='transcript-request'),
    re_path('get-transcript-amount/$', views.get_transcript_amount, name='get_transcript_amount')
]