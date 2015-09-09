# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0024_auto_20150908_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibocard',
            name='card_type',
            field=models.CharField(default=b'special', max_length=12),
        ),
    ]
