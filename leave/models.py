from django.db import models
import datetime
from users.models import Staff
# Create your models here.


class Leave(models.Model):
    leave_status = (
        ('AP','Approved'),
        ('DE', 'Denied')
        )
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, blank=False, null=False)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    reason = models.TextField(max_length=400)
    leave_processor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='leave_processor')
    status = models.CharField(default=leave_status, max_length=12, blank=True, null=True)

