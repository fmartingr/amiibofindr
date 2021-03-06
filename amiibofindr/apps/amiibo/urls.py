# coding: utf-8

# django
from django.conf.urls import url, patterns
from django.utils.translation import ugettext_lazy as _

# home
from .views import (
    AmiiboView, AmiiboCardView, AmiiboFigureView,
    CollectionView, CollectionCardView, CollectionFigureView,
    UserAmiiboView
)

urlpatterns = patterns(
    '',
    url(_('^cards$'),
        CollectionCardView.as_view(),
        name='cards-all'),
    url(_(r'^figures$'),
        CollectionFigureView.as_view(),
        name='figures-all'),

    url(_(r'^cards/(?P<dummy>[\w\d\-]+)?\-(?P<collection>\d+)$'),
        CollectionCardView.as_view(),
        name='cards-list'),
    url(_(r'^figures/(?P<dummy>[\w\d\-]+)?\-(?P<collection>\d+)$'),
        CollectionFigureView.as_view(),
        name='figures-list'),

    url(_(r'^cards/(?P<collection>[\w\d\-]+)?/(?P<dummy>[\w\d\-]+)?-(?P<amiibo>[\w\d\-]+)$'),
        AmiiboCardView.as_view(),
        name='card-detail'),
    url(_(r'^figures/(?P<collection>[\w\d\-]+)?/(?P<dummy>[\w\d\-]+)?-(?P<amiibo>[\w\d\-]+)$'),
        AmiiboFigureView.as_view(),
        name='figure-detail'),

    url(_(r'^amiibo/(?P<amiibo>\d+)/(?P<action>[\w\+\-\=]+)$'),
        UserAmiiboView.as_view(),
        name='user-action'),
)
