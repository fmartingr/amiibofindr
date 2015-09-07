# coding: utf-8

# django
from django.conf.urls import url, patterns

# home
from .views import HomeView


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='redirect'),
)
