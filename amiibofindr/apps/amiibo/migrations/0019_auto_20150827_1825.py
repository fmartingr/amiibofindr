# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import amiibofindr.apps.amiibo.models


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0018_amiiboshop_check_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmiiboCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=60)),
                ('name_en', models.CharField(max_length=64, null=True, blank=True)),
                ('name_es', models.CharField(max_length=64, null=True, blank=True)),
                ('name_fr', models.CharField(max_length=64, null=True, blank=True)),
                ('name_it', models.CharField(max_length=64, null=True, blank=True)),
                ('name_de', models.CharField(max_length=64, null=True, blank=True)),
                ('name_eu', models.CharField(max_length=64, null=True, blank=True)),
                ('name_jp', models.CharField(max_length=64, null=True, blank=True)),
                ('name_us', models.CharField(max_length=64, null=True, blank=True)),
                ('slug', models.SlugField(max_length=60)),
                ('image', models.ImageField(upload_to=amiibofindr.apps.amiibo.models.image_card_upload)),
                ('dice', models.IntegerField(default=1)),
                ('rps', models.CharField(default=1, max_length=1, choices=[(1, b'Rock'), (2, b'Paper'), (3, b'Scissors')])),
            ],
            options={
                'ordering': ('collection', 'number', 'name'),
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='have_cards',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='amiibocard',
            name='collection',
            field=models.ForeignKey(related_name='cards_qs', to='amiibo.Collection'),
        ),
    ]
