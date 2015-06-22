# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0008_amiiboshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='item_id',
            field=models.CharField(default='--', max_length=64),
            preserve_default=False,
        ),
    ]
