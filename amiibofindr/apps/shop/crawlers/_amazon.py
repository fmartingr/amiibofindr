# coding: utf-8

# py
from __future__ import unicode_literals
from time import sleep
import urllib2

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

    def parse_product(self, product):
        price_and_currency = product.price_and_currency

        price = price_and_currency[0]
        currency = price_and_currency[1]

        if currency == 'JPY':
            price = float(price)*100

        print(self.region, product.asin, price, currency, product.title)

        return {
            'shop_product_id': product.asin,
            'price': price,
            'currency': currency,
            'title': product.title,
        }

    def fetch_batch(self, product_ids):
        result = []
        for chunk_product_ids in chunks(product_ids, self.max_batch_lookup):
            try:
                products = self.amazon.lookup(ItemId=','.join(chunk_product_ids))
            except urllib2.HTTPError:
                return result
            try:
                for product in products:
                    result.append(self.parse_product(product))
            except TypeError:
                result.append(self.parse_product(products))
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
