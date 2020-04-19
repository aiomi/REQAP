from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from PIL import Image
# Create your models here.

class User(AbstractUser):
    
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
        return f'staff {self.user.first_name}'

    

class StaffVerification(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    selfie = models.ImageField(upload_to='staffs', blank=True, null=True)
    id_card = models.ImageField(upload_to='staffs', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def save(self):
        super().save()
        img = Image.open(self.selfie.path)
        if img.height > 500 or img.width > 500:
            output_size = (500,500)
            img.save(self.img.path)

        img_ = Image.open(self.id_card.path)
        if img_.height > 500 or img_.width > 500:
            output_size = (500,500)
            img_.save(self.img_.path)