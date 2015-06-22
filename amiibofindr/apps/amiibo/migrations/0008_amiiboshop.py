# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('amiibo', '0007_amiibopricehistory_diff'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmiiboShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('amiibo', models.ForeignKey(to='amiibo.Amiibo')),
                ('shop', models.ForeignKey(to='shop.Shop')),
            ],
        ),
    ]
