from django.urls import path

from webImpression.web.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('services', ServicesView.as_view(), name='services'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('send-email', TestView.as_view(), name='send_email'),
    path('anymail', SendEmailAnymail.as_view(), name='anymail'),
]
