# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amiibo', '0021_auto_20150907_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAmiibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('want', models.BooleanField(default=False)),
                ('have', models.BooleanField(default=False)),
                ('trade', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('_amiibo', models.ForeignKey(to='amiibo.Amiibo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
