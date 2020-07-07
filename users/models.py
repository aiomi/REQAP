from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils import timezone
from PIL import Image
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20, blank=False, null = False, unique=True)
    #matric_number = 
    faculty = models.CharField(max_length=12, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)

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
        return f'staff {self.user.username}'

    

class StaffVerification(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    selfie = models.ImageField(upload_to='staffs', blank=True, null=True)
    id_card = models.ImageField(upload_to='staffs', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.staff.user.username} verification files'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.selfie.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.save(self.selfie.path)

        img_ = Image.open(self.id_card.path)
        if img_.height > 500 or img_.width > 500:
            output_size = (500,500)
            img_.save(self.id_card.path)