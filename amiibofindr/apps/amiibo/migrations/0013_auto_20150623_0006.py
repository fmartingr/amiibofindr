# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0012_auto_20150623_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboprice',
            name='stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amiibopricehistory',
            name='stock',
            field=models.BooleanField(default=False),
        ),
    ]
