# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('amiibo', '0005_auto_20150616_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmiiboPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('currency', models.CharField(default=b'EUR', max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amiibo', models.ForeignKey(to='amiibo.Amiibo')),
                ('shop', models.ForeignKey(to='shop.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AmiiboPriceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('currency', models.CharField(default=b'EUR', max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amiibo', models.ForeignKey(to='amiibo.Amiibo')),
                ('shop', models.ForeignKey(to='shop.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
