# coding: utf-8

# django
from django.views.generic.base import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


class HomeView(View):
    def get(self, request):
        return redirect(reverse('amiibo:collection', args=['all']))
