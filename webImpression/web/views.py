from smtplib import SMTPDataError

from django.conf import settings

from django.core.mail import EmailMessage, get_connection
from django.shortcuts import render, redirect
from django.views import View

from webImpression.web.forms import ContactForm


class HomePageView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        form = ContactForm()

        context = {
            'form': form,
        }
        return render(request, 'index.html', context)

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)

        context = {
            'form': form,
        }
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS) as connection:

                    # Send email:
                    email = EmailMessage(
                        subject=subject,
                        body=message,
                        from_email='info@web-impression.net',
                        to=['ramona.gospodinova@gmail.com'],
                        reply_to=[email],    # Email from the form to get back to,
                        connection=connection
                    )
                    try:
                        email.send()
                    except SMTPDataError as error:
                        context.update({
                            'message': error.args[1],
                        })
        return render('homepage', context)

