from django.conf import settings
from django.core.mail import EmailMessage
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
