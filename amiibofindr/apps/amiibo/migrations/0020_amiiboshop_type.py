# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0018_amiiboshop_check_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiiboshop',
            name='type',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Figure'), (b'2', b'Pack')]),
        ),
    ]
