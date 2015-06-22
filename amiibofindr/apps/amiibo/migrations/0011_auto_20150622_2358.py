# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0010_auto_20150622_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amiibopricehistory',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='amiiboprice',
            name='amiibo_shop',
            field=models.ForeignKey(related_name='price_set', to='amiibo.AmiiboShop'),
        ),
        migrations.AlterField(
            model_name='amiibopricehistory',
            name='amiibo_shop',
            field=models.ForeignKey(related_name='price_history_set', to='amiibo.AmiiboShop'),
        ),
        migrations.AlterField(
            model_name='amiiboshop',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]
