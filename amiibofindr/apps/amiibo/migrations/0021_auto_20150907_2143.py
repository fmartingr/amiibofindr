# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import amiibofindr.apps.amiibo.models


BACKUP = {}


def backup_images(apps, schema_editor):
    Amiibo = apps.get_model("amiibo", "Amiibo")
    for amiibo in Amiibo.objects.all():
        BACKUP[amiibo.pk] = {
            'box': amiibo.box,
            'statue': amiibo.statue,
        }

def restore_images(apps, schema_editor):
    AmiiboFigure = apps.get_model("amiibo", "AmiiboFigure")
    for pk, images in BACKUP.items():
        amiibo = AmiiboFigure.objects.get(pk=pk)
        amiibo.box = images['box']
        amiibo.statue = images['statue']
        amiibo.save()


def convert_all_to_figures(apps, schema_editor):
    Amiibo = apps.get_model('amiibo', 'Amiibo')
    AmiiboFigure = apps.get_model('amiibo', 'AmiiboFigure')
    for amiibo in Amiibo.objects.all():
        figure = AmiiboFigure(amiibo_ptr=amiibo)
        for key, value in amiibo.__dict__.items():
            figure.__dict__[key] = value
        figure.save()


class Migration(migrations.Migration):

    dependencies = [
        ('amiibo', '0020_amiiboshop_type'),
    ]

    operations = [
        # From removed migrations
        migrations.RunSQL("DROP TABLE amiibo_amiibocard;"),
        migrations.RunSQL("ALTER TABLE amiibo_collection DROP COLUMN have_cards;"),
        # Fresh start
        migrations.RunPython(backup_images),
        migrations.RemoveField(
            model_name='amiibo',
            name='box',
        ),
        migrations.RemoveField(
            model_name='amiibo',
            name='statue',
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_de',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_en',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_es',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_fr',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='link_it',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_de',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_en',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_es',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_fr',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='name_it',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amiibo',
            name='type',
            field=models.CharField(default=b'figure', max_length=9, choices=[(b'figure', b'Figure'), (b'card', b'Card')]),
        ),
        migrations.CreateModel(
            name='AmiiboCard',
            fields=[
                ('amiibo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='amiibo.Amiibo')),
                ('image', models.ImageField(upload_to=amiibofindr.apps.amiibo.models.image_card_upload)),
                ('dice', models.IntegerField(default=1)),
                ('rps', models.CharField(default=1, max_length=1, choices=[(1, b'Rock'), (2, b'Paper'), (3, b'Scissors')])),
            ],
            options={
                'ordering': ('collection', 'collection_number', 'name_eu'),
            },
            bases=('amiibo.amiibo',),
        ),
        migrations.CreateModel(
            name='AmiiboFigure',
            fields=[
                ('amiibo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='amiibo.Amiibo')),
                ('statue', models.ImageField(upload_to=amiibofindr.apps.amiibo.models.image_statue_upload)),
                ('box', models.ImageField(null=True, upload_to=amiibofindr.apps.amiibo.models.image_box_upload, blank=True)),
            ],
            bases=('amiibo.amiibo',),
        ),
        migrations.RunPython(convert_all_to_figures),
        migrations.RunPython(restore_images),
    ]
