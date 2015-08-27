# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.apps import AppConfig
from django.db.models.signals import pre_save, post_save

# project
from amiibofindr.apps.amiibo.signals import amiibo_price_changed

# notifications
from .handlers import launch_notifications


class NotificationsAppConfig(AppConfig):
    name = 'amiibofindr.apps.notifications'

    def ready(self):
        AmiiboNotification = self.get_model('AmiiboNotification')

        amiibo_price_changed.connect(
            launch_notifications
        )
