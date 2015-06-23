# coding: utf-8

# python3
from __future__ import unicode_literals

# django
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print(args, kwargs)
