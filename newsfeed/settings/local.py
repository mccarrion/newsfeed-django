"""
These are the local settings for this Django project.
"""
import os

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7x*9_#61df+4xe2_%dz0k3*7!e&!3b20ql0s2y5607ow@5ichy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}

# This is a whitelist of who is allowed to make HTTP
# requests on the backend
CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'newsfeed/temp/email')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
