from django.shortcuts import render
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

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
        message_success = send_email_to_recipient(request, form)
        context['message_success'] = message_success
        return render(request, 'contact.html', context)


class WebDesignView(TemplateView):
    template_name = 'services/web_design.html'


class SEOView(TemplateView):
    template_name = 'services/seo_optimization.html'
