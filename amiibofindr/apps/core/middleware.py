# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import activate


class LanguageMiddleware:
    def process_request(self, request):
        languages = dict(settings.LANGUAGES)
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')

        if not accept_language:
            return None

        lang = accept_language.split(',')[0]

        if '-' in lang:
            lang = lang.split('-')[0]

        if lang in languages:
            activate(lang)

        return None
