from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

from .models import User, Staff


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
        Staff.objects.create(user=user)
        return user