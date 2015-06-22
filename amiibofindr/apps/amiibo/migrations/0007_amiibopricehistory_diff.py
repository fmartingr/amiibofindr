# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0006_amiiboprice_amiibopricehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='amiibopricehistory',
            name='diff',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
