# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.conf import settings


def debug(request):
    return {
        'DEBUG': settings.DEBUG,
    }


def files(request):
    return {
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    }


def i18n(request):
    result = []
    for lang_code, name in settings.LANGUAGES:
        this = {
            'code': lang_code,
            'name': name,
            'url': request.path.replace(request.LANGUAGE_CODE, lang_code)
        }
        result.append(this)

    return {
        'LANGUAGES': result
    }
