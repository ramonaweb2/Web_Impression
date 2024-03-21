import os

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from webImpression.utils.emails import send_email_to_recipient, validate_email
from webImpression.web.forms import ContactForm
from webImpression.web.models import UserSubscriber


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

        email = request.POST.get('email', None)
        if email:
            validate_email(email)

        form = ContactForm(request.POST)
        context = {
            'form': form,
        }
        send_email_to_recipient(request, form)
        return render(request, 'index.html', context)


class ServicesView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'services.html')


class AboutView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'about.html')


class PricingView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'pricing.html')


class DemoView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'portfolio.html')


class ContactsView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        form = ContactForm()

        context = {
            'form': form,
        }
        return render(request, 'contact.html', context)

    @staticmethod
    def post(request):
        form = ContactForm(request.POST)
        context = {
            'form': form,
        }

        # Check the Recaptcha
        captcha_response = request.POST.get('g-recaptcha-response')
        if not captcha_response:
            context['message_error'] = 'Невалидна ReCaptcha. Проверете и опитайте отново.'
        else:
            message_success = send_email_to_recipient(request, form)
            context['message_success'] = message_success

        return render(request, 'contact.html', context)


class SubscriptionView(View):

    @staticmethod
    def post(request):
        email = request.POST.get('email', None)
        res = validate_email(email)

        if res.status_code == 200:
            user_subscriber = UserSubscriber()
            user_subscriber.email = email
            user_subscriber.save()
            res = JsonResponse({'msg_success': 'Благодарим ви! Успешно се регистрирахте за нашият бюлетин.'})

        return res


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"


class SitemapView(TemplateView):
    template_name = "sitemap.xml"
