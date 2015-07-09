# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150624_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
