import json
import os

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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


class TestView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'send_email.html')

    @staticmethod
    def post(request, *args, **kwargs):
        if request.method == 'POST':
            try:
                subject = request.POST['subject']
                message = request.POST['message']
                from_email = request.POST['from']
                html_message = bool(request.POST.get('html-message', False))
                recipient_list = [request.POST.get('to', settings.DEFAULT_TO_EMAIL)]

                email = EmailMessage(subject, message, from_email, recipient_list)
                if html_message:
                    email.content_subtype = 'html'
                email.send()
            except KeyError:
                return HttpResponse('Please fill in all fields')

            return HttpResponse('Email sent :)')


class SendEmailAnymail(TemplateView):
    template_name = 'send_email.html'

    def get(self, request, **kwargs):
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
                    "email": "ramonaweb2@gmail.com",
                    "name": "Jimmy"
                }
            ],
            "htmlContent": "<!DOCTYPE html> <html> <body> <h1>Test headings</h1> </html>",
            "subject": "Test",
            "replyTo": {
                "email": "ramonaweb2@gmail.com",
                "name": "Ann"
            },
            "tags": [
                "tag1",
                "tag2"
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "api-key": os.environ.get("APY_KEY")
        }
        response = requests.post(url=url, json=json_obj, headers=headers)
        print(response.text)

        return HttpResponse('OK')
