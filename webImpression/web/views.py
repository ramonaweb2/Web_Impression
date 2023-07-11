from django.core.mail import send_mail
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

        send_mail(
            "Subject here",
            "Here is the message.",
            "ramona.gospodinova@gmail.com",
            ["ramona.gospodinova@gmail.com"],
            fail_silently=False,
        )

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
        send_mail(
            "Subject here",
            "Here is the message test.",
            "info@web-impreession.net",
            ["ramona.gospodinova@gmail.com"],
            fail_silently=False,
        )
        return HttpResponse("Success")