# coding: utf-8

# django
from django.contrib import admin

# third party
import reversion

# amiibo
from .models import Collection, Amiibo


class CollectionAdmin(reversion.VersionAdmin):
    list_display = ('name', 'amiibo_number', )

    def amiibo_number(self, obj):
        return obj.amiibos.count()
    amiibo_number.short_description = 'Amiibos'


class AmiiboAdmin(reversion.VersionAdmin):
    list_display_links = ('name', )
    list_display = ('statue_image', 'name', 'collection',)

    def statue_image(self, obj):
        return '<img src="{}" width="80" />'.format(obj.statue.url)
    statue_image.allow_tags = True


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Amiibo, AmiiboAdmin)
