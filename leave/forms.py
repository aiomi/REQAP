from django import forms
from .models import Leave
class LeaveForm(forms.ModelForm):


    class Meta:
        model = Leave
        exclude = ['status', ]