# coding: utf-8

# django
from django.contrib import admin

# 3rd party
import reversion

# notifications
from .models import AmiiboNotification


class AmiiboNotificationAdmin(reversion.VersionAdmin):
    list_display = ('amiibo', 'max_price', 'interval', 'shops_list', 'notify_twitter', 'last_notification',)
    list_editable = ('interval', 'notify_twitter', )
    filter_horizontal = ('shops', )

    def shops_list(self, obj):
        return ','.join(obj.shops.values_list('shop__name', flat=True))

admin.site.register(AmiiboNotification, AmiiboNotificationAdmin)
