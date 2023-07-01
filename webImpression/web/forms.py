from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, validators=[EmailValidator])
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

