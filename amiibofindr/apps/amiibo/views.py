# coding: utf-8

# django
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.utils.translation import ugettext as _

# amiibo
from amiibofindr.apps.amiibo.models import Collection, Amiibo


class HomeModel:
    def get_absolute_url(self):
        return reverse('amiibo:collection', args=[_('all')])

class CollectionView(View):
    template = 'amiibo/collection.html'

    def get(self, request, collection='all'):
        if collection != _('all'):
            collection = get_object_or_404(Collection, slug=collection)
            amiibo_list = collection.amiibos
        else:
            collection = None
            amiibo_list = Amiibo.objects.all().order_by('name_eu')

        return render(request, self.template, {
            'selected_collection': collection,
            'amiibo_list': amiibo_list,
            'item': collection or HomeModel(),
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
            'item': amiibo_obj
        })
