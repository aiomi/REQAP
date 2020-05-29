import os
from .common import *
import django_heroku

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','13cup!y_6m69lex=qr=$#t5auinxk1=f7jnshf7hp86-oq$2ju')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['request-approval.herokuapp.com']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# email settings 
EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'

PAYSTACK_SECRET_KEY = 'sk_test_89a731d195ed54e9a31e62a40969af5122234f31'
PAYSTACK_PUBLIC_KEY = 'pk_test_0648fd53970b44f3e99c8a4fe69f4bbbdd679233'
PAYSTACK_EMAIL = 'greatness@gmail.com'

django_heroku.settings(locals())