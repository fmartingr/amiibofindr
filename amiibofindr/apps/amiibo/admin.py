# coding: utf-8

# django
from django.contrib import admin

# third party
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import reversion


# amiibo
from .models import Collection, Amiibo


class ColectionResource(resources.ModelResource):
    class Meta:
        model = Collection


class AmiiboResource(resources.ModelResource):
    class Meta:
        model = Amiibo


class CollectionAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = ColectionResource

    list_display = ('name_eu', 'amiibo_number', )

    def amiibo_number(self, obj):
        return obj.amiibos.count()
    amiibo_number.short_description = 'Amiibos'


class AmiiboAdmin(ImportExportModelAdmin, reversion.VersionAdmin):
    resource_class = AmiiboResource

    list_display_links = ('name_eu', )
    list_display = ('statue_image', 'box_image', 'name_eu', 'collection',)
    search_fields = ('collection__name_eu', 'name_eu', 'name_us', )

    def statue_image(self, obj):
        return '<img src="{}" width="80" />'.format(obj.image_statue)
    statue_image.allow_tags = True

    def box_image(self, obj):
        return '<img src="{}" width="80" />'.format(obj.image_box)
    box_image.allow_tags = True


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Amiibo, AmiiboAdmin)
