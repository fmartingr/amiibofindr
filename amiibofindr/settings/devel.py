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

OPENEXCHANGERATES_KEY = 'aa703ed87a7749afab77b2966559c9df'

try:
    from local_settings import *
except ImportError:
    pass
