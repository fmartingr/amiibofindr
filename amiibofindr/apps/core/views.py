# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.shortcuts import render_to_response
from django.template import RequestContext


def error404(request):
    template = '404.html'
    response = render_to_response(
        template,
        context_instance=RequestContext(request)
    )
    response.status_code = 404
    return response


def error500(request):
    template = '500.html'
    response = render_to_response(
        template,
        context_instance=RequestContext(request)
    )
    response.status_code = 500
    return response
