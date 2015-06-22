# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0009_amiiboshop_item_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amiiboshop',
            options={'ordering': ('shop__name',)},
        ),
        migrations.RemoveField(
            model_name='amiiboprice',
            name='amiibo',
        ),
        migrations.RemoveField(
            model_name='amiiboprice',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='amiibopricehistory',
            name='amiibo',
        ),
        migrations.RemoveField(
            model_name='amiibopricehistory',
            name='shop',
        ),
        migrations.AddField(
            model_name='amiiboprice',
            name='amiibo_shop',
            field=models.ForeignKey(default=1, to='amiibo.AmiiboShop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amiibopricehistory',
            name='amiibo_shop',
            field=models.ForeignKey(default=1, to='amiibo.AmiiboShop'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amiiboshop',
            name='amiibo',
            field=models.ForeignKey(related_name='shops_set', to='amiibo.Amiibo'),
        ),
        migrations.AlterField(
            model_name='amiiboshop',
            name='shop',
            field=models.ForeignKey(related_name='amiibos_set', to='shop.Shop'),
        ),
    ]
