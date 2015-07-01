# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.db import models


class AmiiboNotification(models.Model):
    amiibo = models.ForeignKey('amiibo.Amiibo', related_name='notifications')
    max_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    interval = models.PositiveIntegerField(default=60*60)
    shops = models.ManyToManyField('amiibo.AmiiboShop', blank=True)

    notify_twitter = models.BooleanField(default=True)

    last_notification = models.DateTimeField(blank=True, null=True)
