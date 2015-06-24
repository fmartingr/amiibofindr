# coding: utf-8

# py
from __future__ import unicode_literals
from time import sleep

# third party
from amazon.api import AmazonAPI

# django
from django.conf import settings

# amiibofindr
from amiibofindr.apps.core.utils import chunks


class AmazonBaseCrawler(object):
    region = 'US'
    max_batch_lookup = 10

    def __init__(self):
        self.amazon = AmazonAPI(
            settings.AMAZON_ACCESS_KEY,
            settings.AMAZON_SECRET_KEY,
            settings.AMAZON_ASSOC_TAG,
            region=self.region
        )

    def fetch_batch(self, product_ids):
        result = []
        for chunk_product_ids in chunks(product_ids, self.max_batch_lookup):
            products = self.amazon.lookup(ItemId=','.join(chunk_product_ids))
            for product in products:
                price_and_currency = product.price_and_currency
                result.append({
                    'shop_product_id': product.asin,
                    'price': price_and_currency[0].replace(',', ''),
                    'currency': price_and_currency[1],
                })
            sleep(1)

        return result

    def fetch_from_id(self, product_id):
        product = self.amazon.lookup(ItemId=product_id)
        price_and_currency = product.price_and_currency
        amiibo_price = {
            'shop_product_id': product_id,
            'price': price_and_currency[0].replace(',', ''),
            'currency': price_and_currency[1],
        }

        return amiibo_price


class AmazonUSCrawler(AmazonBaseCrawler):
    pass


class AmazonESCrawler(AmazonBaseCrawler):
    region = 'ES'


class AmazonFRCrawler(AmazonBaseCrawler):
    region = 'FR'


class AmazonUKCrawler(AmazonBaseCrawler):
    region = 'UK'


class AmazonDECrawler(AmazonBaseCrawler):
    region = 'DE'


class AmazonITCrawler(AmazonBaseCrawler):
    region = 'IT'


class AmazonJPCrawler(AmazonBaseCrawler):
    region = 'JP'
