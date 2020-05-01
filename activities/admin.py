from django.contrib import admin

from .models import Request, Transcript, TranscriptAttribute
# Register your models here.
admin.site.register(Request)
admin.site.register(TranscriptAttribute)
admin.site.register(Transcript)