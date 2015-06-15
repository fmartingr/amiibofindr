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
    name = models.CharField(max_length=128)

    @property
    def amiibos(self):
        return self.amiibos_qs.all()

    def __unicode__(self):
        return self.name


class Amiibo(models.Model):
    collection = models.ForeignKey(Collection, related_name='amiibos_qs')

    original_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    statue = models.ImageField(upload_to=image_statue_upload)
    box = models.ImageField(upload_to=image_box_upload, blank=True, null=True)

    name_es = models.CharField(max_length=64)

    release_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def name(self):
        return self.original_name
