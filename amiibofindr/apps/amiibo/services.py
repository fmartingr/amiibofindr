# -*- coding: utf-8 -*-

from . import models


def is_owned_by(amiibo, user):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    return relation.owned

def user_add_owned(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.own = True
    relation.want = False
    relation.save()

def user_remove_owned(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.own = False
    relation.trade = False
    relation.save()

def user_add_wishlist(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.own = False
    relation.want = True
    relation.save()

def user_remove_wishlist(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.want = False
    relation.save()

def user_add_trade(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.trade = True
    relation.save()

def user_remove_trade(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.trade = False
    relation.save()

def user_toggle_trade(user, amiibo):
    relation, created = models.UserAmiibo.objects.get_or_create(
        _amiibo=amiibo, user=user)
    relation.trade = not relation.trade
    relation.save()
