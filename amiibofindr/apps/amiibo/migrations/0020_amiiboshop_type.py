# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0019_auto_20150827_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='type',
            field=models.CharField(default=1, max_length=1, choices=[(1, b'Figure'), (2, b'Pack')]),
        ),
    ]
