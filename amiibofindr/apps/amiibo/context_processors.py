# coding: utf-8

# amiibo
from .models import Collection, AmiiboPrice, AmiiboCard, UserAmiibo


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


def user_amiibo(request):
    owned = []
    wishlisted = []
    trading = []
    if request.user.is_authenticated():
        owned  = UserAmiibo.objects.filter(own=True).values_list('id', flat=True)
        wishlisted = UserAmiibo.objects.filter(want=True).values_list('id', flat=True)
        trading = UserAmiibo.objects.filter(trade=True).values_list('id', flat=True)

    return {
        'USER_AMIIBO_OWNED': owned,
        'USER_AMIIBO_WISHLIST': wishlisted,
        'USER_AMIIBO_TRADE': trading
    }
