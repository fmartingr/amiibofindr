# -*- coding: utf-8 -*-

from django.views.generic.base import View
from django.shortcuts import render


class HomeView(View):
    template = 'home/home.html'

    def get(self, request):
        return render(request, self.template, {})
