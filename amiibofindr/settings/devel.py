# coding: utf-8

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amiibofindr',
        'USER': 'vagrant',
        'PASS': 'vagrant',
        'HOST': '127.0.0.1',
    }
}
