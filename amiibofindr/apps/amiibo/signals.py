# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django import dispatch


amiibo_price_changed = dispatch.Signal(
    providing_args=[
        "instance",
        "amiibo",
        "old_stock",
        "old_price", "new_price"
    ]
)
