from django.contrib import admin
from .models import Staff, User, StaffVerification
# Register your models here.
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(StaffVerification)