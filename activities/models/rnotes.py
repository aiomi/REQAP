from django.db import models
from . import Transcript
from users.models import Staff


class TranscriptNote(models.Model):
    transcript = models.ForeignKey(Transcript, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    reason = models.CharField(max_length=160, blank=True, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)