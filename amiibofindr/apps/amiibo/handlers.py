# coding: utf-8

# py3
from __future__ import unicode_literals

# python
import copy
from decimal import Decimal

# amiibo
from .signals import amiibo_price_changed


def save_historical_price(sender, instance, **kwargs):
    old_price = kwargs.get('old_price')
    if old_price:
        old_price = Decimal(old_price)
    new_price = kwargs.get('new_price')
    if new_price:
        new_price = Decimal(new_price)

    if old_price != new_price:
        instance.save_history(old_price, new_price)


def post_check_price_change(sender, instance, created, **kwargs):
    if (
        instance.price != instance.old_price
        or instance.stock != instance.old_stock
    ):
        amiibo_price_changed.send(
            sender=instance.__class__,
            instance=instance,
            amiibo=instance.amiibo_shop.amiibo,
            old_stock=instance.old_stock,
            old_price=instance.old_price,
            new_price=instance.price
        )
