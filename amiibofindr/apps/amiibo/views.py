# coding: utf-8

# django
from django.shortcuts import render
from django.views.generic.base import View

# amiibo
from amiibofindr.apps.amiibo.models import Collection, Amiibo


class CollectionView(View):
    template = 'amiibo/collection.html'

    def get(self, request, collection='all'):
        if collection != 'all':
            collection = Collection.objects.get(slug=collection)
            amiibo_list = collection.amiibos
        else:
            collection = None
            amiibo_list = Amiibo.objects.all()

        return render(request, self.template, {
            'selected_collection': collection,
            'amiibo_list': amiibo_list,
        })


class AmiiboView(View):
    template = 'amiibo/amiibo.html'

    def get(self, request, collection=None, amiibo=None):
        amiibo_obj = Amiibo.objects.get(slug=amiibo,
                                        collection__slug=collection)

        return render(request, self.template, {
            'selected_collection': amiibo_obj.collection,
            'amiibo': amiibo_obj,
        })
