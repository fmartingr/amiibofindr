# coding: utf-8

from __future__ import unicode_literals

from django.utils.translation import activate, deactivate, get_language
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
    lang = get_language()
    result = []
    for lang_code, name in settings.LANGUAGES:
        activate(lang_code)
        this = {
            'code': lang_code,
            'name': name,
            'url': request.path.replace('/' + request.LANGUAGE_CODE,
                                        '/' + lang_code)
        }
        result.append(this)
        deactivate()

    activate(lang)
    return {
        'LANGUAGES': result
    }
