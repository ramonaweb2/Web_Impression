"""
This call sends a message to one recipient.
"""
import re

import requests
from django.conf import settings
from django.http import JsonResponse

from webImpression.web.models import UserSubscriber

SEND_TRANSACTIONAL_EMAIL_URL = "https://api.brevo.com/v3/smtp/email"


def validate_email(email):
    user_subscriber = UserSubscriber.objects.filter(email=email)
    if email is None:
        res = JsonResponse({'msg_error': 'Имейл е задължителен.'}, status=400)
    elif user_subscriber:
        res = JsonResponse({'msg_error': 'Този имейл адрес вече е регистриран за нашия бюлетин.'}, status=400)
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({'msg_error': 'Имейла е невалиден.'}, status=400)
    else:
        res = JsonResponse({'msg_success': ''}, status=200)

    return res


def _send_email_message(subject, message):
    json_obj = {
        "sender": {
            "name": "WEB Impression",
            "email": "ramonaweb2@gmail.com",
        },
        "to": [
            {
                "name": "WEB Impression",
                "email": "ramona.gospodinova@gmail.com",
            }
        ],
        "htmlContent": f"<!DOCTYPE html> <html> <body> {message} </html>",
        "subject": subject,
        "replyTo": {
            "email": "ramonaweb2@gmail.com",
            "name": "WEB Impression",
        },
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api-key": settings.APY_KEY,
    }
    response = requests.post(url=SEND_TRANSACTIONAL_EMAIL_URL, json=json_obj, headers=headers)
    return response


def send_email_to_recipient(request, form):

    message_success = 'Email not sent successfully'
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email_from = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        form_message = form.cleaned_data.get('message')

        message = f"<div>Message: {form_message}</div>"
        message += f"<div>From email: {email_from}</div>"
        message += f"<div>Name: {name} </div>"

        message_success = 'Your message has been sent. Thank you!'

        _send_email_message(subject, message)

    return message_success
