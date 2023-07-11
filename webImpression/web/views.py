
import os

from django.conf import settings
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from webImpression.utils.emails import send_email_to_recipient
from webImpression.web.forms import ContactForm


class HomePageView(View):
    """
    Home page view
    """

    @staticmethod
    def get(request, *args, **kwargs):
        form = ContactForm()

        context = {
            'form': form,
        }

        return render(request, 'index.html', context)

    @staticmethod
    def post(request):
        message_success = send_email_to_recipient(request)
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'message_success': message_success,
        }
        return render(request, 'index.html', context)


class ServicesView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'services.html')


class ContactsView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        form = ContactForm()

        context = {
            'form': form,
        }
        return render(request, 'contacts.html', context)

    @staticmethod
    def post(request):
        message_success = send_email_to_recipient(request)
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'message_success': message_success,
        }
        return render(request, 'contacts.html', context)


class TestView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        connection = EmailBackend(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            useername=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
            fail_silently=False,
        )
        send_mail(
            subject="Subject here",
            message="Here is the message test.",
            from_email=os.environ.get('MAIL_FROM_EMAIL'),
            recipient_list=["ramona.gospodinova@gmail.com"],
            connection=connection,
            fail_silently=False,
        )
        return HttpResponse("Success")