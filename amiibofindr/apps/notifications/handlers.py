# coding: utf-8

# py3
from __future__ import unicode_literals
from datetime import timedelta

# django
from django.utils import timezone

# notifications
from .services.twitter import TwitterService


def launch_notifications(sender, instance, amiibo, old_price, new_price, **kwargs):
    notifications = amiibo.notifications.all()

    for notification in notifications:
        shops_count = notification.shops.count()
        if (
            (
                shops_count > 0
                and notification.shops.filter(pk__in=[instance.amiibo_shop.pk])
            )
            or shops_count == 0
        ):
            notify = True

            # Check if new price is lower than the notification price
            if new_price > notification.max_price:
                notify = False

            if instance.stock is False:
                notify = False

            # Check if we already posted a notification in the given interval
            print(notification.__dict__)
            print(timezone.now()-timedelta(seconds=notification.interval))
            if (
                notification.last_notification
                and notification.last_notification > timezone.now() - timedelta(seconds=notification.interval)
            ):
                notify = False

            print(notify)

            if notify:
                message = "{} {} {}{} - {}".format(
                    amiibo.name_eu,
                    instance.amiibo_shop.shop.name,
                    new_price,
                    instance.currency,
                    instance.amiibo_shop.get_url(),
                )

                if notification.notify_twitter:
                    twitter = TwitterService()
                    twitter.send(message)

                notification.last_notification = timezone.now()
                notification.save()
