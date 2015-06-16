# coding: utf-8

# django
from django.conf.urls import url, patterns

# home
from .views import HomeView


urlpatterns = patterns(
    '',
    url(r'^(?P<collection>[\w\d\-]+)/$', HomeView.as_view()),
    url(r'^$', HomeView.as_view()),
)
