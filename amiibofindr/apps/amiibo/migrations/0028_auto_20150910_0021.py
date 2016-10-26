# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0027_auto_20150910_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibocard',
            name='rps',
            field=models.CharField(default=b'rock', max_length=12, choices=[(b'rock', b'Rock'), (b'paper', b'Paper'), (b'scissors', b'Scissors')]),
        ),
    ]
