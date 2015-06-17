# coding: utf-8

# python
import os

# django
from django.db import models


#
# Upload_to helpers
def image_statue_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/{}/{}-statue{}'.format(
        self.collection.slug, self.slug, extension)

def image_box_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/{}/{}-box{}'.format(
        self.collection.slug, self.slug, extension)


#
# Models
class Collection(models.Model):
    slug = models.SlugField(max_length=128)
    name_eu = models.CharField(max_length=128)
    name_jp = models.CharField(max_length=128, blank=True, null=True)
    name_us = models.CharField(max_length=128, blank=True, null=True)

    @property
    def amiibos(self):
        return self.amiibos_qs.all()

    @models.permalink
    def get_absolute_url(self):
        return ('amiibo:collection', [self.slug])

    @property
    def name(self):
        return self.name_eu

    def __unicode__(self):
        return unicode(self.name_eu) or u''


class Amiibo(models.Model):
    collection = models.ForeignKey(Collection, related_name='amiibos_qs')
    collection_number = models.IntegerField(blank=True, null=True)

    model_number = models.CharField(max_length=20, blank=True, null=True)

    slug = models.SlugField(max_length=64)

    name_eu = models.CharField(max_length=64, blank=True, null=True)
    name_jp = models.CharField(max_length=64, blank=True, null=True)
    name_us = models.CharField(max_length=64, blank=True, null=True)

    # Links
    link_eu = models.CharField(max_length=255, blank=True, null=True)
    link_jp = models.CharField(max_length=255, blank=True, null=True)
    link_us = models.CharField(max_length=255, blank=True, null=True)

    release_date = models.DateField(null=True, blank=True)

    visible = models.BooleanField(default=True)

    @models.permalink
    def get_absolute_url(self):
        return ('amiibo:amiibo', [self.collection.slug, self.slug])

    @property
    def image_box(self):
        return 'images/amiibo/{}/{}-box.jpg'.format(
            self.collection.slug, self.slug
        )

    @property
    def image_statue(self):
        return 'images/amiibo/{}/{}.png'.format(
            self.collection.slug, self.slug
        )

    def __unicode__(self):
        return unicode(self.name_eu) or u''

    @property
    def name(self):
        return self.name_eu
