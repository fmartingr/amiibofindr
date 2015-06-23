# coding: utf-8

# py3
from __future__ import unicode_literals

from .amazon import (
    AmazonUSCrawler,
    AmazonESCrawler,
    AmazonUKCrawler,
    AmazonITCrawler,
    AmazonDECrawler,
    AmazonJPCrawler,
    AmazonFRCrawler,
)


class Crawler(object):
    crawler_classes = {
        'amazon-us': AmazonUSCrawler,
        'amazon-uk': AmazonUKCrawler,
        'amazon-fr': AmazonFRCrawler,
        'amazon-es': AmazonESCrawler,
        'amazon-de': AmazonDECrawler,
        'amazon-it': AmazonITCrawler,
        'amazon-jp': AmazonJPCrawler,
    }

    def __new__(self, shop_slug):
        if shop_slug in self.crawler_classes:
            return self.crawler_classes[shop_slug]()
        raise Exception('Shop slug {} not found!'.format(shop_slug))
