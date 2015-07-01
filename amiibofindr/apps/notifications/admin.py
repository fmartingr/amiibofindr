# coding: utf-8

# django
from django.contrib import admin

# 3rd party
import reversion

# notifications
from .models import AmiiboNotification


class AmiiboNotificationAdmin(reversion.VersionAdmin):
    filter_horizontal = ('shops', )

admin.site.register(AmiiboNotification, AmiiboNotificationAdmin)
