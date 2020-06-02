import os
from .common import *

SECRET_KEY = 'h4ye7m8sj2rj^b2b1x$s20)^0j0n&^a5704y1tb(m7@#w6^w#r'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'reqap_db',
        'USER': 'reqap',
        'PASSWORD': 'reqap',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
# email settings 
EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'

PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY')

PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY')
PAYSTACK_EMAIL = os.environ.get('PAYSTACK_EMAIL')