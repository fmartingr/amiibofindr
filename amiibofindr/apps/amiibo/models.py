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


class AmiiboShop(models.Model):
    amiibo = models.ForeignKey(Amiibo, related_name='shops_set')
    shop = models.ForeignKey('shop.Shop', related_name='amiibos_set')
    url = models.TextField()
    item_id = models.CharField(max_length=64)

    class Meta:
        ordering = ('shop__name', )

    @property
    def last_price(self):
        return self.price_set.first()

    def __unicode__(self):
        return u'{} in {}'.format(self.amiibo.name, self.shop.name)


class AmiiboPrice(models.Model):
    amiibo_shop = models.ForeignKey(AmiiboShop, related_name='price_set')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(default='EUR', max_length=3)
    date = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(AmiiboPrice, self).__init__(*args, **kwargs)
        self.old_price = self.price

    def __unicode__(self):
        return u'{} price for {}: {}{}'.format(
            self.amiibo.name,
            self.shop.name,
            self.price, self.currency
        )

    def save_history(self, old_price, new_price):
        history = AmiiboPriceHistory(
            amiibo=self.amiibo,
            shop_id=self.shop_id,
            price=self.price,
            currency=self.currency,
            diff=new_price-old_price
        )
        return history.save()


class AmiiboPriceHistory(models.Model):
    amiibo_shop = models.ForeignKey(AmiiboShop,
                                    related_name='price_history_set')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(default='EUR', max_length=3)
    date = models.DateTimeField(auto_now_add=True)
    diff = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-date', )

    def __unicode__(self):
        return u'{} price for {}: {}{} [{}{}] ({})'.format(
            self.amiibo.name,
            self.shop.name,
            self.price, self.currency,
            self.diff, self.currency,
            self.date
        )
