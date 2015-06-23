# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0013_auto_20150623_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiiboprice',
            name='price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
    ]
