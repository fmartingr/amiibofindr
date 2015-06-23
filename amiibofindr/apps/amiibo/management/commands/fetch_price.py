# coding: utf-8

# python3
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand

# amiibo
from amiibofindr.apps.amiibo.models import AmiiboShop


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for amiibo_shop in AmiiboShop.objects.order_by('shop__flag_code'):
            print(amiibo_shop.shop.flag_code, amiibo_shop.item_id, amiibo_shop.url)
