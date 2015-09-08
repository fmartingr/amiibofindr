# coding: utf-8

# django
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.utils.translation import ugettext as _

# amiibo
from amiibofindr.apps.amiibo.models import (
    Collection, Amiibo,
    AmiiboFigure, AmiiboCard
)


class HomeModel:
    def get_absolute_url(self):
        return reverse('amiibo:collection', args=[_('all')])


class CollectionView(View):
    template = 'amiibo/collection.html'
    type = Amiibo.FIGURE
    model = AmiiboFigure

    def get(self, request, collection='all'):
        if collection != _('all'):
            collection = get_object_or_404(Collection, slug=collection)
            if self.type == self.model.FIGURE:
                amiibo_list = collection.figures
            elif self.type == self.model.CARD:
                amiibo_list = collection.cards
            else:
                amiibo_list = collection.amiibo
        else:
            collection = None
            amiibo_list = self.model.objects.all().order_by('name_eu')

        return render(request, self.template, {
            'selected_collection': collection,
            'amiibo_list': amiibo_list,
            'item': collection or HomeModel(),
        })


class CollectionFigureView(CollectionView):
    type = Amiibo.FIGURE
    model = AmiiboFigure


class CollectionCardView(CollectionView):
    type = Amiibo.CARD
    model = AmiiboCard


class AmiiboView(View):
    def get(self, request, collection=None, amiibo=None):
        amiibo_obj = get_object_or_404(self.model,
                                       slug=amiibo,
                                       collection__slug=collection,
                                       type=self.type)

        return render(request, self.template, {
            'selected_collection': amiibo_obj.collection,
            'amiibo': amiibo_obj,
            'item': amiibo_obj
        })

class AmiiboFigureView(AmiiboView):
    template = 'amiibo/amiibo-figure.html'
    type = Amiibo.FIGURE
    model = AmiiboFigure


class AmiiboCardView(AmiiboView):
    template = 'amiibo/amiibo-card.html'
    type = Amiibo.CARD
    model = AmiiboCard
