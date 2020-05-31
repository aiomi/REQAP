from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from datetime import date
from users.models import Staff
from .models import Leave

class LeaveForm(forms.ModelForm):
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)
    leave_processor = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(), widget = FilteredSelectMultiple('leave processors',False))
    class Meta:
        model = Leave
        exclude = ['status', 'staff']
    class Media:
        css = {
                'all': (
                          '/static/admin/css/widgets.css',
                          '/static/css/widgets.css',
                       )
              }
        js = [
                '/admin/jsi18n/'
             ]
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('from_date')
        end_date = cleaned_data.get('to_date')

        if end_date < start_date:
            raise forms.ValidationError('End date should be greater than start date')
