from django.db import models
import datetime
from users.models import Staff
# Create your models here.


class Leave(models.Model):
    leave_status = (
        ('AP','Approved'),
        ('DE', 'Denied')
        )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    reason = models.TextField(max_length=400)
    leave_processor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='leave_processor')
    status = models.CharField(max_length=12, blank=True, null=True)


    def __str__(self):
        return f'{self.leave_type} Leave by {self.user}'

