# -*- coding: utf-8 -*-
import hashlib

from django import template

register = template.Library()

@register.simple_tag
def gravatar(user, size=200):
    return 'https://www.gravatar.com/avatar/{}?s={}&d=mm'.format(
        hashlib.md5(user.email).hexdigest(),
        size
    )
