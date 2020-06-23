from django import forms

class StudentRegFormMixin:
    """ Form mixin to help validate matricuation numbers"""
    VALID_MATRIC_SUFFIX = ['cs', 'it', 'sc']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        suffix = username[-2:]

        if not (suffix in self.VALID_MATRIC_SUFFIX):
            raise forms.ValidationError('Not a valid matriculation number')
        return username


class EmailMixin:
    """
    checks if an email belongs to fut or not
    """
    VALID_EMAIL_PROVIDERS = ['st.futminna.edu.ng']

    def clean_email(self):

        email = self.cleaned_data['email']

        if not email.lower().endswith(tuple(self.VALID_EMAIL_PROVIDERS)):
            raise forms.ValidationError("This email domain is not allowed. Please use FUTMinna's email")
        return email