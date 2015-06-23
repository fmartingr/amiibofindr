# coding: utf-8

# py3
from __future__ import unicode_literals

# third party
from amazon.api import AmazonAPI

# django
from django.conf import settings


class AmazonBaseCrawler(object):
    region = 'US'

    def __init__(self):
        self.amazon = AmazonAPI(
            settings.AMAZON_ACCESS_KEY,
            settings.AMAZON_SECRET_KEY,
            settings.AMAZON_ASSOC_TAG,
            region=self.region
        )

    def fetch_by_id(self, product_id):
        product = self.amazon.lookup(ItemId=product_id)
        price_and_currency = product.price_and_currency
        amiibo_price = {
            'shop_product_id': product_id,
            'price': price_and_currency[0],
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
