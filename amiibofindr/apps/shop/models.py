# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    flag_code = models.CharField(max_length=2, blank=True, null=True)
    referer_id = models.CharField(max_length=64, blank=True, null=True)
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name
