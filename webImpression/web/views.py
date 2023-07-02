from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from webImpression.web.forms import ContactForm


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

        context = { 'form': form,}
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            # Send email:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email='info@web-impression.net',
                to=['ramona.gospodinova@gmail.com'],
                reply_to=[email]    # Email from the form to get back to
            )
            email.send()
        else:
            return render('homepage', context)

        return redirect('homepage')
