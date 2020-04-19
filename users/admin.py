from django.contrib import admin
from .models import Staff, User, StaffVerification
# Register your models here.

admin.site.register(StaffVerification)


class StaffVerificationInline(admin.TabularInline):
    model = StaffVerification

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):

    inlines = [
        StaffVerificationInline,
    ]

    list_display = ('user', 'office',)

    list_filter = ('office',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username','first_name','last_name',
        'is_teacher', 'faculty', 'department',
        )
    
    list_filter = (
        'is_active', 'is_teacher', 'faculty',
        'department','date_joined',
        )

    search_fields = ('username',)
    ordering = ('-date_joined',)