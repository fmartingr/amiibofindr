# coding: utf-8

# python3
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand

# amiibo
from amiibofindr.apps.amiibo.models import AmiiboShop
from amiibofindr.apps.shop.models import Shop
from amiibofindr.apps.shop.crawlers import Crawler


class Command(BaseCommand):
    def update_product(self, product, region):
        amiibo_shop = AmiiboShop.objects.get(
            item_id=product['shop_product_id'],
            shop__flag_code=region[0]
        )
        amiibo_shop.shop_name = product.title
        amiibo_shop.update_price(product['price'], product['currency'])

    def handle(self, *args, **kwargs):
        regions = Shop.objects.all()\
            .order_by('flag_code')\
            .distinct('flag_code')\
            .values_list('flag_code', 'slug')

        for region in regions:
            item_codes = AmiiboShop.objects.filter(
                shop__flag_code=region[0],
                check_price=True).values_list('item_id', flat=True)
            amazon = Crawler(region[1])
            products = amazon.fetch_batch(item_codes)
            try:
                for product in products:
                    self.update_product(product, region)
            except TypeError:
                self.update_product(product, region)
