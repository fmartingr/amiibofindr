# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0014_auto_20150624_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibopricehistory',
            name='price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2),
        ),
    ]
