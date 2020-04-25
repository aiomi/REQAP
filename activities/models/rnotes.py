from django.db import models
from . import Request
from users.models import Staff


class Note(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    reason = models.CharField(max_length=160, blank=True, null=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)