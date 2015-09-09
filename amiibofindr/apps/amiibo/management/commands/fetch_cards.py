# coding: utf-8

from __future__ import unicode_literals

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from amiibofindr.apps.amiibo.models import AmiiboCard, Collection


class Command(BaseCommand):
    collection_slug = 'animal-crossing'
    url = 'https://api.import.io/store/data/d7057867-dd48-4f5a-80ba-7051daf72bf4/_query?input/webpage/url=http%3A%2F%2Fanimalcrossingworld.com%2Fanimal-crossing-happy-home-designer-amiibo-cards%2F&_user=4519bdcf-aa0b-4b78-b014-e51476ba977c&_apikey=4519bdcfaa0b4b78b014e51476ba977c42d9d75fd621c0ccd433708c1f742487e763cb6a68202c4a5c7aa32c3ef0c99bc18dbc96548bc0c4fd1470abd0418732c82cf53dba34076decc64b68c504026e'
    dice = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    }

    def handle_image(self, image_url):
        image = requests.get(image_url)
        f = ContentFile(image.content, image_url.split('/')[-1])
        return f

    def handle(self, *args, **kwargs):
        collection = Collection.objects.get(slug=self.collection_slug)
        data = requests.get(self.url).json()

        for item in data['results']:
            amiibo, created = AmiiboCard.objects.get_or_create(
                collection_id=collection.pk,
                collection_number=int(item['number_number'])
            )
            print(' => {} {}'.format(collection.slug, amiibo.collection_number))
            amiibo.type = AmiiboCard.CARD
            if created:
                amiibo.name_en = item['name_value']
                amiibo.name_eu = amiibo.name_en
                amiibo.name_us = amiibo.name_en

                # amiibo.collection_number = int(item['number_number'])
                amiibo.collection = collection

                # amiibo.image = self.handle_image(item['cardphoto_link'])

            amiibo.dice = self.dice[item['dice_value'].lower()]
            amiibo.rps = item['rps_value'].lower()

            amiibo.card_type = item['type_value'].lower()

            amiibo.slug = slugify(amiibo.name_en)

            amiibo.save()
