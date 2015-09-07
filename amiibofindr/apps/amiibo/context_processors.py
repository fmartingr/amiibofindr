# coding: utf-8

# amiibo
from .models import Collection, AmiiboPrice


def collections(request):
    return {
        'COLLECTIONS_FIGURES': Collection.objects.all().order_by('name_eu'),
        # 'COLLECTIONS_CARDS': Collection.objects.filter(have_cards=True).order_by('name_eu'),
    }


def currencies(request):
    return {
        'CURRENCIES': AmiiboPrice.objects.all().distinct('currency')\
            .values_list('currency', flat=True)
    }
