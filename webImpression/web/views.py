from smtplib import SMTPDataError

from django.conf import settings

from django.shortcuts import render
from django.views import View

from webImpression.web.forms import ContactForm

from django.core.mail import send_mail


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

            try:
                send_mail(
                    subject,
                    message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[email],
                    fail_silently=False)
            except SMTPDataError as error:
                context.update({
                    'message': error.args[1],
                })

        return render(request, 'index.html', context)

