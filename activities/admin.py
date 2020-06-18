from django.contrib import admin

from .models import Transcript, TranscriptAttribute, TranscriptNote
# Register your models here.
admin.site.register(TranscriptAttribute)
admin.site.register(Transcript)
admin.site.register(TranscriptNote)