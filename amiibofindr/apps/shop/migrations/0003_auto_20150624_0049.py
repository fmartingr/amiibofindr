# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop_flag_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('name',)},
        ),
    ]
