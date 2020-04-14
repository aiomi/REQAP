from django.db import models
#from django.contrib.auth.models import User
from users.models import User
# Create your models here.


class Request(models.Model):
    request_types = (
        ('leave', 'Leave'),
        ('transcripts', 'Transcripts'),
        )
    request_type = models.CharField(choices=request_types, default=request_types, max_length=18)
    request_date = models.DateTimeField(default=None)
    approved_by = models.ManyToManyField(User, through='Action')

    def __str__(self):
        return f'Request on {self.request_date}'


class Action(models.Model):
    """
    This is the approvals model that holds both user and request FKs
    """
    action_types = (
        ('PE','Pending'),
        ('AP', 'Approved'),
        ('DS', 'Disallowed'),
        ('RE', 'Rejected')
    )
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=12, choices = action_types, default=action_types)
    comment = models.TextField(max_length =200, blank=True)


    def __str__(self):
        return f'Action {self.request_id} with status {self.status}'