# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.views.generic.base import View
from django.shortcuts import render, get_object_or_404

from amiibofindr.apps.amiibo.models import UserAmiibo, AmiiboFigure, AmiiboCard


class ProfileView(View):
    template = 'profile/main.html'

    types = {
        'figures': ('figure', AmiiboFigure),
        'cards': ('card', AmiiboCard),
    }

    relations = ('own', 'want', 'trade', )

    def get(self, request, username, type='figures', relation='own'):
        user = get_object_or_404(get_user_model(), username=username)
        relation_filter = {relation: True}
        amiibo_pks = UserAmiibo.objects.filter(
            user=user,
            _amiibo__type=self.types[type][0],
            **relation_filter
        ).values_list('_amiibo__id', flat=True)

        amiibo_list = self.types[type][1].objects.filter(pk__in=amiibo_pks)

        return render(request, self.template, {
            'this_user': user,
            'amiibo_list': amiibo_list,
            'type': type,
            'relation': relation
        })
