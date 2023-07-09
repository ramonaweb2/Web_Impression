"""
This call sends a message to one recipient.
"""
from mailjet_rest import Client
from django.conf import settings

DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL
DEFAULT_TO_EMAIL = settings.DEFAULT_TO_EMAIL
API_KEY = settings.MAILJET_API_KEY
API_SECRET = settings.MAILJET_API_SECRET


def send_email_message(subject, message):
    mailjet = Client(auth=(API_KEY, API_SECRET), version='v3.1')

    data = {
        "Messages": [
            {
                "From": {
                    "Email": DEFAULT_FROM_EMAIL,
                },
                "To": [
                    {
                        "Email": DEFAULT_TO_EMAIL,
                        "Name": "WEB Impression Admin",
                    }
                ],
                "Subject": subject,
                "TextPart": message,
                "HTMLPart": message,
            }
        ]
    }
    result = mailjet.send.create(data=data)
    return result.status_code
