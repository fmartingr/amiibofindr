# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import amiibofindr.apps.amiibo.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amiibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('statue', models.ImageField(upload_to=amiibofindr.apps.amiibo.models.image_statue_upload)),
                ('name_es', models.CharField(max_length=64)),
                ('release_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=128)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='amiibo',
            name='collection',
            field=models.ForeignKey(related_name='amiibos_qs', to='amiibo.Collection'),
        ),
    ]
