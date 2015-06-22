# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0011_auto_20150622_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiiboshop',
            name='url',
            field=models.TextField(),
        ),
    ]
