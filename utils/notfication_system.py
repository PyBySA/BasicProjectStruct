import notifiers
from loguru import logger
from notifiers.logging import NotificationHandler


def generate_notification(message):
    params = {
        "username": "sagararoramailtester@gmail.com",
        "password": "zjznvtretcgqyljm",
        "to": "sagararora.a630@gmail.com"
    }

    # Send a single notification
    notifier = notifiers.get_notifier("gmail")
    notifier.notify(message=message, **params)

    # Be alerted on each error message

    handler = NotificationHandler("gmail", defaults=params)
    logger.add(handler, level="ERROR")
