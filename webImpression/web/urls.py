from django.urls import path

from webImpression.web.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('services', ServicesView.as_view(), name='services'),
    path('about', AboutView.as_view(), name='about'),
    path('pricing', PricingView.as_view(), name='pricing'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('portfolio', DemoView.as_view(), name='portfolio'),
    path('validate', SubscriptionView.as_view(), name='validate'),
    path('newsletter', SubscriptionView.as_view(), name='newsletter'),
    path('robots.txt', RobotsTxtView.as_view(content_type="text/plain"), name='robots'),
]
