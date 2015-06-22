# coding: utf-8

# django
from django.contrib import admin

# third party
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import reversion

# shop
from amiibofindr.apps.shop.models import Shop


class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop


class ShopAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = ShopResource

    list_display = ('name', 'slug', 'referer_id', )

admin.site.register(Shop, ShopAdmin)
