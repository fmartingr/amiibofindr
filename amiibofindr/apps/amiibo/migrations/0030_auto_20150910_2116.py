# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


BACKUP = {}


def backup(apps, schema_editor):
    AmiiboShop = apps.get_model("amiibo", "AmiiboShop")
    for shop in AmiiboShop.objects.all():
        BACKUP[shop.pk] = {
            'amiibo_id': shop.amiibo_id,
        }

def restore(apps, schema_editor):
    AmiiboShop = apps.get_model("amiibo", "AmiiboShop")
    Amiibo = apps.get_model("amiibo", "Amiibo")
    for pk, info in BACKUP.items():
        a = AmiiboShop.objects.get(pk=pk)
        a.amiibo.add(Amiibo.objects.get(pk=int(info['amiibo_id'])))
        a.save()


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0029_amiiboshop_shop_name'),
    ]

    operations = [
        migrations.RunPython(backup),
        migrations.RemoveField(
            model_name='amiiboshop',
            name='amiibo',
        ),
        migrations.AddField(
            model_name='amiiboshop',
            name='amiibo',
            field=models.ManyToManyField(related_name='shops_set', to='amiibo.Amiibo'),
        ),
        migrations.RunPython(restore),
    ]
