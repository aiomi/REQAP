from django import forms

class NoteForm(forms.Form):
    action = forms.CharField(
        max_length=10, widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Approved/Rejected',
                'row':'3'
                }
        )
        )
    reason = forms.CharField(
        max_length=160, widget=forms.Textarea(
            attrs={'class':'form-control reduced-textarea'}
        )
        )
