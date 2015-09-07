# coding: utf-8

# django
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.utils.translation import gettext as _

# amiibo
from amiibofindr.apps.amiibo.models import Collection, Amiibo


class CollectionView(View):
    template = 'amiibo/collection.html'
    all_word = _('all')

    def get(self, request, collection='all'):
        if collection != self.all_word:
            collection = get_object_or_404(Collection, slug=collection)
            amiibo_list = collection.amiibos
        else:
            collection = None
            amiibo_list = Amiibo.objects.all().order_by('name_eu')

        return render(request, self.template, {
            'selected_collection': collection,
            'amiibo_list': amiibo_list,
        })


class AmiiboView(View):
    template = 'amiibo/amiibo.html'

    def get(self, request, collection=None, amiibo=None):
        amiibo_obj = get_object_or_404(Amiibo,
                                       slug=amiibo,
                                       collection__slug=collection)

        return render(request, self.template, {
            'selected_collection': amiibo_obj.collection,
            'amiibo': amiibo_obj,
        })
