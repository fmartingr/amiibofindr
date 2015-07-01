# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0017_auto_20150625_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmiiboNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_price', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('interval', models.PositiveIntegerField(default=3600)),
                ('notify_twitter', models.BooleanField(default=True)),
                ('last_notification', models.DateTimeField(null=True, blank=True)),
                ('amiibo', models.ForeignKey(related_name='notifications', to='amiibo.Amiibo')),
                ('shops', models.ManyToManyField(to='amiibo.AmiiboShop', blank=True)),
            ],
        ),
    ]
