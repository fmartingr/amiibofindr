# coding: utf-8

# django
from django.conf.urls import url, patterns

# home
from .views import AmiiboView, CollectionView


urlpatterns = patterns(
    '',
    url(r'^(?P<collection>[\w\d\-]+)/$',
        CollectionView.as_view(),
        name='collection'),
    url(r'^(?P<collection>[\w\d\-]+)/(?P<amiibo>[\w\d\-]+)$',
        AmiiboView.as_view(),
        name='amiibo'),

)
