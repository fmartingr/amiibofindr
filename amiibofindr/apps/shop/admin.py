# coding: utf-8

# django
from django.contrib import admin

# third party
import reversion

# shop
from amiibofindr.apps.shop.models import Shop


class ShopAdmin(reversion.VersionAdmin):
    pass

admin.site.register(Shop, ShopAdmin)
