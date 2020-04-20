from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
from django.db import transaction
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template import loader
from django import forms
from django.core.mail import send_mail
from .models import User, Staff, StaffVerification


class UserRegistrationForm(UserCreationForm):
    faculty = (
        ('sict','SICT'),
        ('set','SET'),
    )
    faculty = forms.ChoiceField(choices=faculty)
    
    department = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={'placeholder':'Abbreviation eg: css'}
            )
        )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name','last_name', 'username','email',
            'faculty', 'department', 'password1','password2'
        ]

class TeacherSignUpForm(UserCreationForm):
    faculty = [
        ('sict','SICT'),
        ('senate','Senate'),
        ('set','SET'),
    ]
    faculty = forms.ChoiceField(choices=faculty)
    class Meta(UserRegistrationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_active = False
        user.save()
        staff = Staff.objects.create(user=user)
        html_ = loader.render_to_string(
            'email/staff_verify_email.html',
            {
                'user':user,
                'subject':settings.TEACHER_SIGNUP_SUBJECT,
                'staff':staff
            }
            )
        send_mail(
            settings.TEACHER_SIGNUP_SUBJECT, '',
            settings.ADMIN_EMAIL_USER, [user.email],
            fail_silently=True,html_message=html_
            )
        return user


class StaffVerificationForm(forms.ModelForm):

    def save(self, commit=True):
        verification = super().save(commit=False)
        verification.staff = self.request.user.staff
        verification.save()
    class Meta:
        model = StaffVerification
        fields = ['selfie', 'id_card']