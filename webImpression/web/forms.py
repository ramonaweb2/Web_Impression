
from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):

    name = forms.CharField(max_length=50, label='Име')
    email = forms.EmailField(max_length=50, validators=[EmailValidator], label='Имейл')
    subject = forms.CharField(max_length=50, label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Съобщение')

