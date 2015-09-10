# coding: utf-8

from __future__ import unicode_literals

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from amiibofindr.apps.amiibo.models import AmiiboCard, Collection

CARD_IMAGES = """
/amiibo-cards/assets/img/cards/NVL-C-MAAA-USZ-F0(0)001.png
/amiibo-cards/assets/img/cards/NVL-C-MAAB-USZ-F0(0)002.png
/amiibo-cards/assets/img/cards/NVL-C-MAAC-USZ-F0(0)003.png
/amiibo-cards/assets/img/cards/NVL-C-MAAD-USZ-F0(0)004.png
/amiibo-cards/assets/img/cards/NVL-C-MAAE-USZ-F0(0)005.png
/amiibo-cards/assets/img/cards/NVL-C-MAAF-USZ-F0(0)006.png
/amiibo-cards/assets/img/cards/NVL-C-MAAG-USZ-F0(0)007.png
/amiibo-cards/assets/img/cards/NVL-C-MAAH-USZ-F0(0)008.png
/amiibo-cards/assets/img/cards/NVL-C-MAAJ-USZ-F0(0)009.png
/amiibo-cards/assets/img/cards/NVL-C-MAAK-USZ-F0(0)010.png
/amiibo-cards/assets/img/cards/NVL-C-MAAL-USZ-F0(0)011.png
/amiibo-cards/assets/img/cards/NVL-C-MAAM-USZ-F0(0)012.png
/amiibo-cards/assets/img/cards/NVL-C-MAAN-USZ-F0(0)013.png
/amiibo-cards/assets/img/cards/NVL-C-MAAP-USZ-F0(0)014.png
/amiibo-cards/assets/img/cards/NVL-C-MAAQ-USZ-F0(0)015.png
/amiibo-cards/assets/img/cards/NVL-C-MAAR-USZ-F0(0)016.png
/amiibo-cards/assets/img/cards/NVL-C-MAAS-USZ-F0(0)017.png
/amiibo-cards/assets/img/cards/NVL-C-MAAT-USZ-F0(0)018.png
/amiibo-cards/assets/img/cards/NVL-C-MAAU-USZ-F0(0)019.png
/amiibo-cards/assets/img/cards/NVL-C-MAAV-USZ-F0(0)020.png
/amiibo-cards/assets/img/cards/NVL-C-MAAW-USZ-F0(0)021.png
/amiibo-cards/assets/img/cards/NVL-C-MAAX-USZ-F0(0)022.png
/amiibo-cards/assets/img/cards/NVL-C-MAAY-USZ-F0(0)023.png
/amiibo-cards/assets/img/cards/NVL-C-MAAZ-USZ-F0(0)024.png
/amiibo-cards/assets/img/cards/NVL-C-MABA-USZ-F0(0)025.png
/amiibo-cards/assets/img/cards/NVL-C-MABB-USZ-F0(0)026.png
/amiibo-cards/assets/img/cards/NVL-C-MABC-USZ-F0(0)027.png
/amiibo-cards/assets/img/cards/NVL-C-MABD-USZ-F0(0)028.png
/amiibo-cards/assets/img/cards/NVL-C-MABE-USZ-F0(0)029.png
/amiibo-cards/assets/img/cards/NVL-C-MABF-USZ-F0(0)030.png
/amiibo-cards/assets/img/cards/NVL-C-MABG-USZ-F0(0)031.png
/amiibo-cards/assets/img/cards/NVL-C-MABH-USZ-F0(0)032.png
/amiibo-cards/assets/img/cards/NVL-C-MABJ-USZ-F0(0)033.png
/amiibo-cards/assets/img/cards/NVL-C-MABK-USZ-F0(0)034.png
/amiibo-cards/assets/img/cards/NVL-C-MABL-USZ-F0(0)035.png
/amiibo-cards/assets/img/cards/NVL-C-MABM-USZ-F0(0)036.png
/amiibo-cards/assets/img/cards/NVL-C-MABN-USZ-F0(0)037.png
/amiibo-cards/assets/img/cards/NVL-C-MABP-USZ-F0(0)038.png
/amiibo-cards/assets/img/cards/NVL-C-MABQ-USZ-F0(0)039.png
/amiibo-cards/assets/img/cards/NVL-C-MABR-USZ-F0(0)040.png
/amiibo-cards/assets/img/cards/NVL-C-MABS-USZ-F0(0)041.png
/amiibo-cards/assets/img/cards/NVL-C-MABT-USZ-F0(0)042.png
/amiibo-cards/assets/img/cards/NVL-C-MABU-USZ-F0(0)043.png
/amiibo-cards/assets/img/cards/NVL-C-MABV-USZ-F0(0)044.png
/amiibo-cards/assets/img/cards/NVL-C-MABW-USZ-F0(0)045.png
/amiibo-cards/assets/img/cards/NVL-C-MABX-USZ-F0(0)046.png
/amiibo-cards/assets/img/cards/NVL-C-MABY-USZ-F0(0)047.png
/amiibo-cards/assets/img/cards/NVL-C-MABZ-USZ-F0(0)048.png
/amiibo-cards/assets/img/cards/NVL-C-MACA-USZ-F0(0)049.png
/amiibo-cards/assets/img/cards/NVL-C-MACB-USZ-F0(0)050.png
/amiibo-cards/assets/img/cards/NVL-C-MACC-USZ-F0(0)051.png
/amiibo-cards/assets/img/cards/NVL-C-MACD-USZ-F0(0)052.png
/amiibo-cards/assets/img/cards/NVL-C-MACE-USZ-F0(0)053.png
/amiibo-cards/assets/img/cards/NVL-C-MACF-USZ-F0(0)054.png
/amiibo-cards/assets/img/cards/NVL-C-MACG-USZ-F0(0)055.png
/amiibo-cards/assets/img/cards/NVL-C-MACH-USZ-F0(0)056.png
/amiibo-cards/assets/img/cards/NVL-C-MACJ-USZ-F0(0)057.png
/amiibo-cards/assets/img/cards/NVL-C-MACK-USZ-F0(0)058.png
/amiibo-cards/assets/img/cards/NVL-C-MACL-USZ-F0(0)059.png
/amiibo-cards/assets/img/cards/NVL-C-MACM-USZ-F0(0)060.png
/amiibo-cards/assets/img/cards/NVL-C-MACN-USZ-F0(0)061.png
/amiibo-cards/assets/img/cards/NVL-C-MACP-USZ-F0(0)062.png
/amiibo-cards/assets/img/cards/NVL-C-MACQ-USZ-F0(0)063.png
/amiibo-cards/assets/img/cards/NVL-C-MACR-USZ-F0(0)064.png
/amiibo-cards/assets/img/cards/NVL-C-MACS-USZ-F0(0)065.png
/amiibo-cards/assets/img/cards/NVL-C-MACT-USZ-F0(0)066.png
/amiibo-cards/assets/img/cards/NVL-C-MACU-USZ-F0(0)067.png
/amiibo-cards/assets/img/cards/NVL-C-MACV-USZ-F0(0)068.png
/amiibo-cards/assets/img/cards/NVL-C-MACW-USZ-F0(0)069.png
/amiibo-cards/assets/img/cards/NVL-C-MACX-USZ-F0(0)070.png
/amiibo-cards/assets/img/cards/NVL-C-MACY-USZ-F0(0)071.png
/amiibo-cards/assets/img/cards/NVL-C-MACZ-USZ-F0(0)072.png
/amiibo-cards/assets/img/cards/NVL-C-MADA-USZ-F0(0)073.png
/amiibo-cards/assets/img/cards/NVL-C-MADB-USZ-F0(0)074.png
/amiibo-cards/assets/img/cards/NVL-C-MADC-USZ-F0(0)075.png
/amiibo-cards/assets/img/cards/NVL-C-MADD-USZ-F0(0)076.png
/amiibo-cards/assets/img/cards/NVL-C-MADE-USZ-F0(0)077.png
/amiibo-cards/assets/img/cards/NVL-C-MADF-USZ-F0(0)078.png
/amiibo-cards/assets/img/cards/NVL-C-MADG-USZ-F0(0)079.png
/amiibo-cards/assets/img/cards/NVL-C-MADH-USZ-F0(0)080.png
/amiibo-cards/assets/img/cards/NVL-C-MADJ-USZ-F0(0)081.png
/amiibo-cards/assets/img/cards/NVL-C-MADK-USZ-F0(0)082.png
/amiibo-cards/assets/img/cards/NVL-C-MADL-USZ-F0(0)083.png
/amiibo-cards/assets/img/cards/NVL-C-MADM-USZ-F0(0)084.png
/amiibo-cards/assets/img/cards/NVL-C-MADN-USZ-F0(0)085.png
/amiibo-cards/assets/img/cards/NVL-C-MADP-USZ-F0(0)086.png
/amiibo-cards/assets/img/cards/NVL-C-MADQ-USZ-F0(0)087.png
/amiibo-cards/assets/img/cards/NVL-C-MADR-USZ-F0(0)088.png
/amiibo-cards/assets/img/cards/NVL-C-MADS-USZ-F0(0)089.png
/amiibo-cards/assets/img/cards/NVL-C-MADT-USZ-F0(0)090.png
/amiibo-cards/assets/img/cards/NVL-C-MADU-USZ-F0(0)091.png
/amiibo-cards/assets/img/cards/NVL-C-MADV-USZ-F0(0)092.png
/amiibo-cards/assets/img/cards/NVL-C-MADW-USZ-F0(0)093.png
/amiibo-cards/assets/img/cards/NVL-C-MADX-USZ-F0(0)094.png
/amiibo-cards/assets/img/cards/NVL-C-MADY-USZ-F0(0)095.png
/amiibo-cards/assets/img/cards/NVL-C-MADZ-USZ-F0(0)096.png
/amiibo-cards/assets/img/cards/NVL-C-MAEA-USZ-F0(0)097.png
/amiibo-cards/assets/img/cards/NVL-C-MAEB-USZ-F0(0)098.png
/amiibo-cards/assets/img/cards/NVL-C-MAEC-USZ-F0(0)099.png
/amiibo-cards/assets/img/cards/NVL-C-MAED-USZ-F0(0)100.png
""".split('\n')


class Command(BaseCommand):
    collection_slug = 'animal-crossing'
    url = 'https://api.import.io/store/data/d7057867-dd48-4f5a-80ba-7051daf72bf4/_query?input/webpage/url=http%3A%2F%2Fanimalcrossingworld.com%2Fanimal-crossing-happy-home-designer-amiibo-cards%2F&_user=4519bdcf-aa0b-4b78-b014-e51476ba977c&_apikey=4519bdcfaa0b4b78b014e51476ba977c42d9d75fd621c0ccd433708c1f742487e763cb6a68202c4a5c7aa32c3ef0c99bc18dbc96548bc0c4fd1470abd0418732c82cf53dba34076decc64b68c504026e'
    dice = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    }
    card_image_domain = 'http://animal-crossing.com/amiibo-cards/'

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
            else:
                if amiibo.image:
                    amiibo.image.delete()
                amiibo.image = self.handle_image('{}{}'.format(self.card_image_domain,
                                                               CARD_IMAGES[int(item['number_number'])]))

            amiibo.dice = self.dice[item['dice_value'].lower()]
            amiibo.rps = item['rps_value'].lower()

            amiibo.card_type = item['type_value'].lower()

            amiibo.slug = slugify(amiibo.name_en)

            amiibo.save()
