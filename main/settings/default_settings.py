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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# email settings 
EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'