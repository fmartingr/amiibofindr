# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations


def convert(apps, schema_editor):
    Amiibo = apps.get_model("amiibo", "Amiibo")
    for amiibo in Amiibo.objects.all():
        amiibo.name_en = amiibo.name_eu
        amiibo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0030_auto_20150910_2116'),
    ]

    operations = [
        migrations.RunPython(convert),
    ]
