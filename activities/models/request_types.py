from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from users.models import User, Staff

from libs.constants import TranscriptStatus
# Create your models here.

class TranscriptAttribute(models.Model):
    transcript_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.transcript_type}'

class Transcript(models.Model):

    # after an instance is created it will send an email to a user in that group
    # to approve the request hence filing the approved_by with the staff
    
    status_choices = (
        (TranscriptStatus.INITIATED, 'Initiated'),
        (TranscriptStatus.PAID, 'Paid'),
        (TranscriptStatus.APPROVED,'Approved'),
        (TranscriptStatus.DENIED, 'Denied')
        )
    request_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    transcript_type = models.OneToOneField(TranscriptAttribute, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    requires_payment = models.BooleanField(default=True)
    address = models.CharField(max_length=200, null=True)
    has_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=status_choices, default=TranscriptStatus.INITIATED)
    approved_by = models.OneToOneField(Staff, on_delete=models.CASCADE, blank=True,null=True)
    class Meta:
        permissions = [
            ('change_status', 'can change the status of a request to accept or rejected'),
        ]

    def __str__(self):
        return f'Transcript {self.transcript_type} by {self.request_by}'

class ResultRemarking(models.Model):
    pass