# coding: utf-8

# python
from __future__ import unicode_literals
import json
import os

# third party
import requests

# django
from django.conf import settings
from django.core.management.base import BaseCommand

# amiibo
from amiibofindr.apps.amiibo.models import AmiiboPrice


class Command(BaseCommand):
    @property
    def rates_url(self):
        return 'https://openexchangerates.org/api/latest.json?app_id={}'.format(
            settings.OPENEXCHANGERATES_KEY
        )

    def handle(self, *args, **kwargs):
        currencies = AmiiboPrice.objects.all().distinct('currency')\
            .values_list('currency', flat=True)

        rates = requests.get(self.rates_url).json()

        result = {
            'base': rates['base'],
            'rates': {}
        }

        for currency, rate in rates['rates'].iteritems():
            if currency in currencies:
                result['rates'][currency] = rate

        handler = open(os.path.join(settings.MEDIA_ROOT, 'rates.json'), 'w')
        handler.write(json.dumps(result))
        handler.close()

        print(result)
