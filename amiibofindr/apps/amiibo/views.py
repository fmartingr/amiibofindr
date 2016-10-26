# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import (
    Collection, Amiibo,
    AmiiboFigure, AmiiboCard,
    UserAmiibo
)
from . import services


class CollectionView(View):
    template = 'amiibo/collection.html'
    type = Amiibo.FIGURE
    model = AmiiboFigure
    section = 'collection'

    def get(self, request, collection=None, dummy=None):
        if collection:
            collection = get_object_or_404(Collection, pk=collection)
            if self.type == self.model.FIGURE:
                amiibo_list = collection.figures.filter(visible=True)
            elif self.type == self.model.CARD:
                amiibo_list = collection.cards.filter(visible=True)
            else:
                amiibo_list = collection.amiibo.filter(visible=True)
        else:
            collection = None
            amiibo_list = self.model.objects.filter(visible=True)

        return render(request, self.template, {
            'selected_collection': collection,
            'amiibo_list': amiibo_list,
            'item': collection,
            'section': self.section,
        })


class CollectionFigureView(CollectionView):
    type = Amiibo.FIGURE
    model = AmiiboFigure


class CollectionCardView(CollectionView):
    template = 'amiibo/collection-cards.html'
    type = Amiibo.CARD
    model = AmiiboCard


class AmiiboView(View):
    section = 'amiibo'
    def get(self, request, collection=None, amiibo=None, dummy=None):
        amiibo_obj = get_object_or_404(self.model,
                                       pk=amiibo,
                                       # collection__slug=collection,
                                       type=self.type)

        return render(request, self.template, {
            'selected_collection': amiibo_obj.collection,
            'amiibo': amiibo_obj,
            'item': amiibo_obj,
            'section': self.section,
            'users_trading': UserAmiibo.objects.filter(
                trade=True, _amiibo_id=amiibo_obj.pk
            ).order_by('user__username'),
        })

class AmiiboFigureView(AmiiboView):
    template = 'amiibo/amiibo-figure.html'
    type = Amiibo.FIGURE
    model = AmiiboFigure


class AmiiboCardView(AmiiboView):
    template = 'amiibo/amiibo-card.html'
    type = Amiibo.CARD
    model = AmiiboCard


class UserAmiiboView(View):
    actions = {
        '+owned': 'add_owned',
        '-owned': 'remove_owned',
        '+wishlist': 'add_wishlist',
        '-wishlist': 'remove_wishlist',
        '+trade': 'add_trade',
        '-trade': 'remove_trade',
        '+-trade': 'toggle_trade',
    }

    ajax = {
        'detail': 'amiibo/widgets/relation_header_buttons.html',
        'list': 'amiibo/widgets/amiibo-card.html',
    }

    def get(self, request, amiibo, action):
        obj = get_object_or_404(Amiibo, pk=amiibo)
        amiibo = obj.as_type()
        if action in self.actions:
            method = getattr(self, self.actions[action], None)
            if method:
                result = method(request, amiibo)
                if result:
                    return result

        # Handle templating
        request_from = request.GET.get('from', None)
        if request_from in self.ajax:
            return render(request, self.ajax[request_from],
                          { 'amiibo': amiibo, 'request': request })

        return HttpResponseRedirect(amiibo.as_type().get_absolute_url())

    def add_wishlist(self, request, amiibo):
        services.user_add_wishlist(request.user, amiibo)
        # TODO: Add message

    def remove_wishlist(self, request, amiibo):
        services.user_remove_wishlist(request.user, amiibo)
        # TODO: Add message

    def add_trade(self, request, amiibo):
        if services.is_owned_by(amiibo, request.user):
            services.user_add_trade(request.user, amiibo)
            # TODO: Add message

    def remove_trade(self, request, amiibo):
        if services.is_owned_by(amiibo, request.user):
            services.user_remove_trade(request.user, amiibo)
            # TODO: Add message

    def toggle_trade(self, request, amiibo):
        if services.is_owned_by(amiibo, request.user):
            services.user_toggle_trade(request.user, amiibo)
            # TODO: Add message

    def add_owned(self, request, amiibo):
        services.user_add_owned(request.user, amiibo)
        # TODO: Add message

    def remove_owned(self, request, amiibo):
        services.user_remove_owned(request.user, amiibo)
        # TODO: Add message
