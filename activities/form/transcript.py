from django import forms

from activities.models import Transcript, TranscriptAttribute

class TranscriptRequestForm(forms.ModelForm):

    class Meta:
        model = Transcript
        exclude =['has_paid']
