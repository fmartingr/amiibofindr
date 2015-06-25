# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.conf import settings
from django.core.files import File
from django.db import models, migrations

import amiibofindr.apps.amiibo.models


def update_images(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Person = apps.get_model("amiibo", "Amiibo")
    for amiibo in Amiibo.objects.all():
        amiibo.statue = File(open(os.path.join(settings.MEDIA_ROOT, 'amiibos', amiibo.collection.slug, '{}.png'.format(amiibo.slug))))
        amiibo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0016_auto_20150624_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibo',
            name='box',
            field=models.ImageField(null=True, upload_to=amiibofindr.apps.amiibo.models.image_box_upload, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='statue',
            field=models.ImageField(default='amiibos/noimage.png', upload_to=amiibofindr.apps.amiibo.models.image_statue_upload),
            preserve_default=False,
        ),
        migrations.RunPython(update_images),
    ]
