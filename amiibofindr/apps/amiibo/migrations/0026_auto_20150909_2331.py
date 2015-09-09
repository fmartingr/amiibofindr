# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0025_amiibocard_card_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='name_de',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_en',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_es',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_fr',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_it',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
