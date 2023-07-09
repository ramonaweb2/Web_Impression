from smtplib import SMTPDataError


from django.shortcuts import render
from django.views import View

from webImpression.utils.emails import send_email_message
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
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email_from = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            form_message = form.cleaned_data.get('message')

            message = f"<div>Message: {form_message}</div>"
            message += f"<div>From email: {email_from}</div>"
            message += f"<div>Name: {first_name} {last_name}</div>"

            try:
                status_code = send_email_message(subject, message)
                if status_code:
                    message_success = 'Email sent successfully'
                else:
                    message_success = 'Email not sent successfully'

                context.update({
                    'message_success': message_success
                })
            except SMTPDataError as error:
                context.update({
                    'message_errors': error.args[1],
                })

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
