# coding: utf-8

# django
from django.conf.urls import url, patterns
from django.utils.translation import ugettext_lazy as _

# home
from .views import AmiiboView, CollectionView


urlpatterns = patterns(
    '',
    url(_(r'^(?P<collection>[\w\d\-]+)/$'),
        CollectionView.as_view(),
        name='collection'),
    url(_(r'^cards/(?P<collection>[\w\d\-]+)/$'),
        CollectionView.as_view(),
        name='cards-list'),
    url(_(r'^figures/(?P<collection>[\w\d\-]+)/$'),
        CollectionView.as_view(),
        name='figures-list'),

    url(r'^(?P<collection>[\w\d\-]+)/(?P<amiibo>[\w\d\-]+)$',
        AmiiboView.as_view(),
        name='amiibo'),
    url(r'^cards/(?P<collection>[\w\d\-]+)/(?P<amiibo>[\w\d\-]+)$',
        AmiiboView.as_view(),
        name='card-detail'),
    url(r'^figures/(?P<collection>[\w\d\-]+)/(?P<amiibo>[\w\d\-]+)$',
        AmiiboView.as_view(),
        name='figure-detail'),
)
