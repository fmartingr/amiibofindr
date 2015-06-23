# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0015_auto_20150624_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiiboprice',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
