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
    AmiiboFigure, AmiiboCard,
    AmiiboShop,
    AmiiboPrice, AmiiboPriceHistory
)


class ColectionResource(resources.ModelResource):
    class Meta:
        model = Collection


class AmiiboFigureResource(resources.ModelResource):
    class Meta:
        model = AmiiboFigure


class AmiiboShopResource(resources.ModelResource):
    class Meta:
        model = AmiiboShop


class AmiiboCardResource(resources.ModelResource):
    class Meta:
        model = AmiiboCard


class CollectionAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = ColectionResource

    list_display = ('name_eu', 'amiibo_number', )

    def amiibo_number(self, obj):
        return obj.amiibos.count()
    amiibo_number.short_description = 'Amiibos'


class AmiiboFigureAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = AmiiboFigureResource

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


class AmiiboCardAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = AmiiboCardResource

    list_display_links = ('name_eu', )
    list_display = ('image_image', 'name_eu', 'collection',)
    search_fields = ('collection__name_eu', 'name_eu', 'name_us',
                     'model_number')

    def image_image(self, obj):
        if obj.image:
            return '<img src="{}" width="80" />'.format(obj.image.url)
        else:
            return ''
    image_image.allow_tags = True


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
admin.site.register(AmiiboFigure, AmiiboFigureAdmin)
admin.site.register(AmiiboCard, AmiiboCardAdmin)
admin.site.register(AmiiboShop, AmiiboShopAdmin)
admin.site.register(AmiiboPrice, AmiiboPriceAdmin)
admin.site.register(AmiiboPriceHistory, AmiiboPriceHistoryAdmin)
