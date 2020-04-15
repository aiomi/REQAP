from django.db import models
from django.utils import timezone

from users.models import User
# Create your models here.


class Request(models.Model):
    # state = (
    #     ('initiated','Initiated'),
    #     ('')
    #     )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Request by {self.user}'

class TranscriptAttribute(models.Model):
    transcript_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.transcript_type} costs {self.amount}'

class Transcript(models.Model):
    transcript_type = models.OneToOneField(TranscriptAttribute, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    requires_payment = models.BooleanField(default=True)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Transcript {self.transcript_type} by {self.request.user}'

class Leave(models.Model):
    pass

class ResultRemarking(models.Model):
    pass