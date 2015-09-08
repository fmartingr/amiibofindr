# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import amiibofindr.apps.amiibo.models


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0022_useramiibo'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='image',
            field=models.ImageField(null=True, upload_to=amiibofindr.apps.amiibo.models.shop_item_upload, blank=True),
        ),
    ]
