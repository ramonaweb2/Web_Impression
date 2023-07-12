"""
This call sends a message to one recipient.
"""
from smtplib import SMTPDataError

from django.core.mail import send_mail

from webImpression.web.forms import ContactForm


def send_email_to_recipient(request):
    form = ContactForm(request.POST)

    context = {
        'form': form,
    }

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

        try:
            send_mail(subject, message, from_email=email_from, recipient_list=["ramona.gospodinova@gmail.com"])

        except SMTPDataError as error:
            context.update({
                'message_errors': error.args[1],
            })

    return message_success
