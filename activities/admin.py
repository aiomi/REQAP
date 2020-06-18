from django.contrib import admin

from .models import  Transcript, TranscriptAttribute
# Register your models here.
admin.site.register(TranscriptAttribute)
admin.site.register(Transcript)