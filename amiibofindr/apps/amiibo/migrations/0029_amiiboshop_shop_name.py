# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0028_auto_20150910_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='shop_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
