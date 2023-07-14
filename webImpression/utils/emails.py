"""
This call sends a message to one recipient.
"""
import requests
from django.conf import settings

SEND_TRANSACTIONAL_EMAIL_URL = "https://api.brevo.com/v3/smtp/email"


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
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email_from = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        form_message = form.cleaned_data.get('message')

        message = f"<div>Message: {form_message}</div>"
        message += f"<div>From email: {email_from}</div>"
        message += f"<div>Name: {first_name} {last_name}</div>"

        message_success = 'Email sent successfully'

        _send_email_message(subject, message)

    return message_success
