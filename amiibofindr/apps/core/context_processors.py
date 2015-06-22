# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.conf import settings


def debug(request):
    return {
        'DEBUG': settings.DEBUG,
    }
