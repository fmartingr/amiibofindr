# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0017_auto_20150625_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='check_price',
            field=models.BooleanField(default=True),
        ),
    ]
