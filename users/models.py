from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.

class User(AbstractUser):
    
    faculty = models.CharField(max_length=12, blank=True, null=True)
    department = models.CharField(max_length=65, blank=True, null=True)

    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    #has_graduated = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.username}'

class Staff(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #office = models.CharField(max_length=25, choices=staff_offices)
    office = models.ForeignKey(Group, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f'staff {self.user.first_name}'