from django import forms
from .models import Leave
class LeaveForm(forms.ModelForm):


    class Meta:
        model = Leave
        exclude = ['status', ]

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('from_date')
        end_date = cleaned_data.get('to_date')

        if end_date < start_date:
            raise forms.ValidationError('End date should be greater than start date')
