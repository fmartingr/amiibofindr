# coding: utf-8

from __future__ import unicode_literals

from django.utils.translation import activate, deactivate, get_language
from django.core.urlresolvers import resolve, reverse_lazy
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
    try:
        res = resolve(request.path)
        for lang_code, name in settings.LANGUAGES:
            activate(lang_code)
            this = {
                'code': lang_code,
                'name': name,
                'url': reverse_lazy(res.view_name, args=res.args, kwargs=res.kwargs)
            }
            result.append(this)
            deactivate()
        activate(lang)
    except:
        for lang_code, name in settings.LANGUAGES:
            this = {
                'code': lang_code,
                'name': name,
                'url': '/{}/'.format(lang_code)
            }
            result.append(this)
    return {
        'LANGUAGES': result
    }
