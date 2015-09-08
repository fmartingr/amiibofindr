# coding: utf-8

# amiibo
from .models import Collection, AmiiboPrice, AmiiboCard


def collections(request):
    return {
        'COLLECTIONS_FIGURES': Collection.objects.all().order_by('name_eu'),
        'COLLECTIONS_CARDS': Collection.objects.filter(pk__in=
            AmiiboCard.objects.all().distinct('collection').order_by('collection')\
                .values_list('collection__id', flat=True)
        )
    }


def currencies(request):
    return {
        'CURRENCIES': AmiiboPrice.objects.all().distinct('currency')\
            .values_list('currency', flat=True)
    }
