# coding: utf-8

import os

from django.apps import apps
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _, get_language

from amazonify import amazonify

from amiibofindr.apps.shop.crawlers import Crawler


#
# Upload_to helpers
def image_statue_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/{}/{}{}'.format(
        self.collection.slug, self.slug, extension)

def image_box_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/{}/{}-box{}'.format(
        self.collection.slug, self.slug, extension)

def image_card_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/c/{}/{}_{}{}'.format(
        self.collection.pk, self.collection_number, self.pk, extension)

def shop_item_upload(self, filename):
    name, extension = os.path.splitext(filename)
    return 'amiibos/si/{}_{}{}'.format(
        self.shop.pk, self.pk, extension)



#
# Models
class Collection(models.Model):
    slug = models.SlugField(max_length=128)

    name_en = models.CharField(max_length=64, blank=True, null=True)
    name_es = models.CharField(max_length=64, blank=True, null=True)
    name_fr = models.CharField(max_length=64, blank=True, null=True)
    name_it = models.CharField(max_length=64, blank=True, null=True)
    name_de = models.CharField(max_length=64, blank=True, null=True)

    name_eu = models.CharField(max_length=128)
    name_jp = models.CharField(max_length=128, blank=True, null=True)
    name_us = models.CharField(max_length=128, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('amiibo:figures-list', (slugify(self.name), self.pk))

    def get_absolute_url_figures(self):
        return reverse('amiibo:figures-list', args=(slugify(self.name), self.pk))

    def get_absolute_url_cards(self):
        return reverse('amiibo:cards-list', args=(slugify(self.name), self.pk))

    @property
    def amiibos(self):
        return self.amiibos_qs.all()

    @property
    def figures(self):
        return AmiiboFigure.objects.filter(collection_id=self.pk)

    @property
    def cards(self):
        return AmiiboCard.objects.filter(collection_id=self.pk)

    @property
    def name(self):
        name = getattr(self, 'name_{}'.format(get_language()), None)

        if name:
            return name

        if self.name_en:
            return self.name_en

        return self.name_eu

    def __unicode__(self):
        return unicode(self.name_eu) or u''


class Amiibo(models.Model):
    FIGURE = 'figure'
    CARD = 'card'
    AMIIBO_TYPES = (
        (FIGURE, 'Figure'),
        (CARD, 'Card'),
    )

    collection = models.ForeignKey(Collection, related_name='amiibos_qs')
    collection_number = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=9, default=FIGURE, choices=AMIIBO_TYPES)

    model_number = models.CharField(max_length=20, blank=True, null=True)

    slug = models.SlugField(max_length=64)

    name_en = models.CharField(max_length=64, blank=True, null=True)
    name_es = models.CharField(max_length=64, blank=True, null=True)
    name_fr = models.CharField(max_length=64, blank=True, null=True)
    name_it = models.CharField(max_length=64, blank=True, null=True)
    name_de = models.CharField(max_length=64, blank=True, null=True)

    name_eu = models.CharField(max_length=64, blank=True, null=True)
    name_jp = models.CharField(max_length=64, blank=True, null=True)
    name_us = models.CharField(max_length=64, blank=True, null=True)

    # Links
    link_en = models.CharField(max_length=64, blank=True, null=True)
    link_es = models.CharField(max_length=64, blank=True, null=True)
    link_fr = models.CharField(max_length=64, blank=True, null=True)
    link_it = models.CharField(max_length=64, blank=True, null=True)
    link_de = models.CharField(max_length=64, blank=True, null=True)

    link_eu = models.CharField(max_length=255, blank=True, null=True)
    link_jp = models.CharField(max_length=255, blank=True, null=True)
    link_us = models.CharField(max_length=255, blank=True, null=True)

    release_date = models.DateField(null=True, blank=True)

    visible = models.BooleanField(default=True)

    _types = {
        'figure': 'amiibo.AmiiboFigure',
        'card': 'amiibo.AmiiboCard',
    }

    def as_type(self):
        """ Returns the amiibo as the correct type model """
        # TODO: Improve this, because queries. Change to a manager.
        model = apps.get_model(self._types[self.type])
        return model.objects.get(pk=self.pk)

    def get_all_names(self):
        result = u''
        for key, value in self.__dict__.items():
            if u'name_' in key and self.__dict__[key]:
                result += u' {}'.format(self.__dict__[key])

        return result

    @property
    def is_card(self):
        return self.type == self.CARD

    @property
    def is_figure(self):
        return self.type == self.FIGURE

    def __unicode__(self):
        return unicode(self.name_eu) or u''

    @property
    def name(self):
        name = getattr(self, 'name_{}'.format(get_language()), None)

        if name:
            return name

        if self.name_en:
            return self.name_en

        return self.name_eu


class AmiiboFigure(Amiibo):
    statue = models.ImageField(upload_to=image_statue_upload)
    box = models.ImageField(upload_to=image_box_upload, blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('amiibo:figure-detail', [self.collection.slug, slugify(self.name), self.pk])

    @property
    def image_box(self):
        return 'images/amiibo/{}/{}-box.jpg'.format(
            self.collection.slug, self.slug
        )

    @property
    def image(self):
        return self.statue

    @property
    def image_statue(self):
        return 'images/amiibo/{}/{}.png'.format(
            self.collection.slug, self.slug
        )


class AmiiboCard(Amiibo):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'
    RPS_CHOICES = (
        (ROCK, _('Rock')),
        (PAPER, _('Paper')),
        (SCISSORS, _('Scissors')),
    )

    CARD_TYPE_CHOICES = (
        ('alligator', _('Alligator')),
        ('anteater', _('Anteater')),
        ('bear', _('Bear')),
        ('bird', _('Bird')),
        ('bull', _('Bull')),
        ('cat', _('Cat')),
        ('chicken', _('Chicken')),
        ('cow', _('Cow')),
        ('cub', _('Cub')),
        ('deer', _('Deer')),
        ('dog', _('Dog')),
        ('duck', _('Duck')),
        ('eagle', _('Eagle')),
        ('elephant', _('Elephant')),
        ('frog', _('Frog')),
        ('goat', _('Goat')),
        ('gorilla', _('Gorilla')),
        ('hamster', _('Hamster')),
        ('hippo', _('Hippo')),
        ('horse', _('Horse')),
        ('kangaroo', _('Kangaroo')),
        ('koala', _('Koala')),
        ('lion', _('Lion')),
        ('monkey', _('Monkey')),
        ('mouse', _('Mouse')),
        ('octopus', _('Octopus')),
        ('ostrich', _('Ostrich')),
        ('penguin', _('Penguin')),
        ('pig', _('Pig')),
        ('rabbit', _('Rabbit')),
        ('rhino', _('Rhino')),
        ('sheep', _('Sheep')),
        ('special', _('Special')),
        ('squirrel', _('Squirrel')),
        ('tiger', _('Tiger')),
        ('wolf', _('Wolf')),
    )

    image = models.ImageField(upload_to=image_card_upload)
    card_type = models.CharField(max_length=12, default='special')

    dice = models.IntegerField(default=1)
    rps = models.CharField(choices=RPS_CHOICES, default=ROCK, max_length=12)

    class Meta:
        ordering = ('collection', 'collection_number', 'name_eu', )

    def get_card_type_display(self):
        return dict(self.CARD_TYPE_CHOICES)[self.card_type]

    @models.permalink
    def get_absolute_url(self):
        return ('amiibo:card-detail',
                [slugify(self.collection.name), slugify(self.name), self.pk])

    def __unicode__(self):
        return u"{} {}".format(self.collection_number, self.slug)


class AmiiboShop(models.Model):
    FIGURE = '1'
    PACK = '2'

    ITEM_TYPES = (
        (FIGURE, 'Figure'),
        (PACK, 'Pack'),
    )

    amiibo = models.ManyToManyField(Amiibo, related_name='shops_set')
    shop = models.ForeignKey('shop.Shop', related_name='amiibos_set')
    type = models.CharField(choices=ITEM_TYPES, default=FIGURE, max_length=1)
    url = models.TextField()
    item_id = models.CharField(max_length=64)
    check_price = models.BooleanField(default=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=shop_item_upload,
                              null=True, blank=True)

    class Meta:
        ordering = ('shop__name', )

    def get_url(self):
        if self.shop.referer_id:
            return amazonify(self.url, self.shop.referer_id)
        return self.url

    def update_price(self, price, currency):
        price_obj, is_new = AmiiboPrice.objects.get_or_create(
            amiibo_shop_id=self.pk)

        price_obj.price = price
        price_obj.stock = price is not None

        if is_new and currency:
            price_obj.currency = currency

        price_obj.save()

    @property
    def last_price(self):
        return self.price_set.first()

    @property
    def is_pack(self):
        return self.type == self.PACK

    def __unicode__(self):
        return u'{} in {}'.format(self.shop_name, self.shop.name)


class AmiiboPrice(models.Model):
    amiibo_shop = models.ForeignKey(AmiiboShop, related_name='price_set')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    stock = models.BooleanField(default=False)
    currency = models.CharField(default='EUR', max_length=3)
    date = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(AmiiboPrice, self).__init__(*args, **kwargs)
        self.old_price = self.price
        self.old_stock = self.stock

    def __unicode__(self):
        return u'{} price for {}: {}{}'.format(
            self.amiibo_shop.amiibo.name,
            self.amiibo_shop.shop.name,
            self.price,
            self.currency
        )

    def fetch(self):
        crawler = Crawler(self.amiibo_shop.shop.slug)
        price = crawler.fetch_from_id(self.amiibo_shop.item_id)
        return price

    def save_history(self, old_price, new_price):
        if new_price is None or old_price is None:
            diff = 0
        else:
            diff = new_price-old_price

        if diff > 0:
            history = AmiiboPriceHistory(
                amiibo_shop_id=self.amiibo_shop_id,
                price=self.price,
                currency=self.currency,
                diff=diff
            )
            return history.save()


class AmiiboPriceHistory(models.Model):
    amiibo_shop = models.ForeignKey(AmiiboShop,
                                    related_name='price_history_set')
    stock = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    currency = models.CharField(default='EUR', max_length=3)
    date = models.DateTimeField(auto_now_add=True)
    diff = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ('-date', )

    def __unicode__(self):
        return u'{} price for {}: {}{} [{}{}] ({})'.format(
            self.amiibo_shop.amiibo.name,
            self.amiibo_shop.shop.name,
            self.price, self.currency,
            self.diff, self.currency,
            self.date
        )


class UserAmiibo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    _amiibo = models.ForeignKey(Amiibo)

    want = models.BooleanField(default=False)
    own = models.BooleanField(default=False)
    trade = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    @property
    def amiibo(self):
        return self._amiibo.as_type()
