# coding: utf-8

# amiibo
from .models import Collection


def collections(request):
    return {
        'collections': Collection.objects.all().order_by('name_eu')
    }
