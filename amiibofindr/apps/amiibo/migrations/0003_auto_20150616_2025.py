# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0002_amiibo_box'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='name',
            new_name='name_eu',
        ),
        migrations.RemoveField(
            model_name='amiibo',
            name='name_es',
        ),
        migrations.RemoveField(
            model_name='amiibo',
            name='original_name',
        ),
        migrations.AddField(
            model_name='amiibo',
            name='collection_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_eu',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_jp',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_us',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='model_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_eu',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_jp',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_us',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_jp',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='name_us',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
