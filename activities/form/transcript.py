from django import forms

from activities.models import Transcript, TranscriptAttribute

class TranscriptRequestForm(forms.ModelForm):

    class Meta:
        model = Transcript
        exclude =['has_paid', 'requires_payment', 'request', 'approved_by', 'status']
