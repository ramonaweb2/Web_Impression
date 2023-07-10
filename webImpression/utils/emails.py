"""
This call sends a message to one recipient.
"""
from smtplib import SMTPDataError

from mailjet_rest import Client
from django.conf import settings

from webImpression.web.forms import ContactForm

DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL
DEFAULT_TO_EMAIL = settings.DEFAULT_TO_EMAIL
API_KEY = settings.MAILJET_API_KEY
API_SECRET = settings.MAILJET_API_SECRET


def send_email(request):
    form = ContactForm(request.POST)

    context = {
        'form': form,
    }
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

        try:
            status_code = compose_email_message(subject, message)
            if not status_code:
                message_success = 'Email not sent successfully'

        except SMTPDataError as error:
            context.update({
                'message_errors': error.args[1],
            })
    else:
        message_success = 'Email not sent successfully'

    return message_success


def compose_email_message(subject, message):
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
