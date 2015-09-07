# coding: utf-8

# amiibo
from .models import Collection, AmiiboPrice


def collections(request):
    return {
        'COLLECTIONS_FIGURES': Collection.objects.all().order_by('name_eu'),
        #: Collection.objects.filter(cards
    }


def currencies(request):
    return {
        'CURRENCIES': AmiiboPrice.objects.all().distinct('currency')\
            .values_list('currency', flat=True)
    }
