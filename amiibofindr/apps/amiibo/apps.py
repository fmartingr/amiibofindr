# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save

# amiibo
from .handlers import (
    pre_check_price_change, post_check_price_change,
    save_historical_price
)
from .signals import amiibo_price_changed


class AmiiboAppConfig(AppConfig):
    name = 'amiibofindr.apps.amiibo'

    def ready(self):
        AmiiboPrice = self.get_model('AmiiboPrice')

        # pre_save.connect(pre_check_price_change,
        #                  sender=AmiiboPrice)

        post_save.connect(post_check_price_change,
                          sender=AmiiboPrice)

        amiibo_price_changed.connect(save_historical_price,
                                     sender=AmiiboPrice)
