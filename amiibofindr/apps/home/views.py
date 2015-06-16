# coding: utf-8

# django
from django.shortcuts import render
from django.views.generic.base import View

# amiibo
from amiibofindr.apps.amiibo.models import Amiibo


class HomeView(View):
    template = 'home/home.html'

    def get(self, request):
        return render(request, self.template, {
            'amiibo_list': Amiibo.objects.all()
        })
