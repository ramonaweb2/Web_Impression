from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

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
        form = ContactForm(request.POST)

        context = {
            'form': form,
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
        form = ContactForm(request.POST)

        context = {
            'form': form,
        }
        return render(request, 'contacts.html', context)


class TestView(View):

    @staticmethod
    def get(request, *args, **kwargs):
        send_mail("Subject here",
                  "Here is the message test.",
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.DEFAULT_TO_EMAIL])

        return HttpResponse("Success")
