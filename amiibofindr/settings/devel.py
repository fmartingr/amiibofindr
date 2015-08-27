# coding: utf-8

#
# Development settings prepared for vagrant
#

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amiibofindr',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '127.0.0.1',
    }
}

# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = '/vagrant/media'

try:
    from local_settings import *
except ImportError as e:
    print(e)
