
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from webImpression.web.forms import ContactForm

import requests


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


class SendEmailAnymail(View):

    @staticmethod
    def get(request, **kwargs):
        # send_mail("It works!",
        #           "111 This will get sent through Brevo 222",
        #           "Anymail Sender <ramonaweb2@gmail.com>",
        #           ["ramonaweb2@gmail.com"],
        #           fail_silently=False)

        url = "https://api.brevo.com/v3/smtp/email"
        json_obj = {
            "sender": {
                "name": "Mary from MyShop",
                "email": "ramonaweb2@gmail.comm"
            },
            "to": [
                {
                    "email": "ramona.gospodinova@gmail.com",
                    "name": "RG"
                }
            ],
            "htmlContent": "<!DOCTYPE html> <html> <body> <h1>Test headings</h1> </html>",
            "subject": "Test",
            "replyTo": {
                "email": "ramonaweb2@gmail.com",
                "name": "Ann"
            },
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "api-key": settings.APY_KEY,
        }
        response = requests.post(url=url, json=json_obj, headers=headers)
        response_text = response.text + f"APY_KEY: {settings.APY_KEY}"

        return HttpResponse(response_text)

