# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0023_amiiboshop_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useramiibo',
            old_name='have',
            new_name='own',
        ),
    ]
