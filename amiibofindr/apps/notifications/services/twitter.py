# coding: utf-8

# py3
from __future__ import unicode_literals

# django
from django.conf import settings

# 3rd party
import tweepy

class TwitterService(object):
    def __init__(self):
        self.auth = tweepy.OAuthHandler(
            settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        self.auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
        self.api = tweepy.API(self.auth)

    def send(self, message):
        try:
            self.api.update_status(status=message)
        except tweepy.error.TweepError:
            pass
