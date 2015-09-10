# coding: utf-8

# django
from django.conf.urls import url, patterns
from django.utils.translation import ugettext_lazy as _

# home
from .views import ProfileView


urlpatterns = patterns(
    '',
    url(_(r'^profile/(?P<username>[\w\d\-]+)/$'),
          ProfileView.as_view(),
          name='main'),
    url(_(r'^profile/(?P<username>[\w\d\-]+)/(?P<type>\w+)/(?P<relation>\w+)/$'),
          ProfileView.as_view(),
          name='main-filter'),

)
