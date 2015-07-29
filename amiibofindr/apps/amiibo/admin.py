# coding: utf-8

# django
from django.contrib import admin

# third party
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import reversion


# amiibo
from .models import (
    Collection, Amiibo,
    AmiiboShop,
    AmiiboPrice, AmiiboPriceHistory
)


class ColectionResource(resources.ModelResource):
    class Meta:
        model = Collection


class AmiiboResource(resources.ModelResource):
    class Meta:
        model = Amiibo


class AmiiboShopResource(resources.ModelResource):
    class Meta:
        model = AmiiboShop


class CollectionAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = ColectionResource

    list_display = ('name_eu', 'amiibo_number', )

    def amiibo_number(self, obj):
        return obj.amiibos.count()
    amiibo_number.short_description = 'Amiibos'


class AmiiboAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = AmiiboResource

    list_display_links = ('name_eu', )
    list_display = ('statue_image', 'name_eu', 'collection',)
    search_fields = ('collection__name_eu', 'name_eu', 'name_us',
                     'model_number')

    def statue_image(self, obj):
        if obj.statue:
            return '<img src="{}" width="80" />'.format(obj.statue.url)
        else:
            return ''
    statue_image.allow_tags = True

    def box_image(self, obj):
        return '<img src="{}" width="80" />'.format(obj.box.url)
    box_image.allow_tags = True


class AmiiboShopAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = AmiiboShopResource
    list_display = ('amiibo', 'shop', 'check_price')
    list_filter = ('amiibo', 'shop', )
    list_editable = ('check_price', )



class AmiiboPriceAdmin(reversion.VersionAdmin):
    pass


class AmiiboPriceHistoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Amiibo, AmiiboAdmin)
admin.site.register(AmiiboShop, AmiiboShopAdmin)
admin.site.register(AmiiboPrice, AmiiboPriceAdmin)
admin.site.register(AmiiboPriceHistory, AmiiboPriceHistoryAdmin)
