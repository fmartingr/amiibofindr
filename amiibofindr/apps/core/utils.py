# coding: utf-8

# py3
from __future__ import unicode_literals


def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    http://stackoverflow.com/a/312464
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
