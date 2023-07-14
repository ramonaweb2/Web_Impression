from django.shortcuts import render
from django.views import View
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
        send_email_to_recipient(request, form)
        return render(request, 'contacts.html', context)


class WebDesignView(TemplateView):
    template_name = 'services/web_design.html'
