# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import amiibofindr.apps.amiibo.models


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibo',
            name='box',
            field=models.ImageField(null=True, upload_to=amiibofindr.apps.amiibo.models.image_box_upload, blank=True),
        ),
    ]
