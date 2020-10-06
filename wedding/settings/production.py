import os
from .base import *


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'amf$+%4%7-vr-dfrq#x$(#ge_491e=4uoered%ujytoq@o3og0')

DEBUG = False

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_NAME = '__Secure-sessionid'

CSRF_COOKIE_HTTPONLY = True

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_NAME = '__Secure-csrftoken'

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 31536000

X_FRAME_OPTIONS = 'DENY'

ALLOWED_HOSTS = ['deuxouipourunnom.love', 'www.deuxouipourunnom.love']

DEFAULT_DOMAIN = 'https://deuxouipourunnom.love'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', ''),
        'USER': os.environ.get('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}
