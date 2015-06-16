# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0004_amiibo_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amiibo',
            name='box',
        ),
        migrations.RemoveField(
            model_name='amiibo',
            name='statue',
        ),
    ]
