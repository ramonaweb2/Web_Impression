from django.urls import path

from webImpression.web.views import *

urlpatterns = [
    path('', never_cache(HomePageView.as_view()), name='homepage'),
    path('services', never_cache(ServicesView.as_view()), name='services'),
    path('about', never_cache(AboutView.as_view()), name='about'),
    path('pricing', never_cache(PricingView.as_view()), name='pricing'),
    path('contacts', never_cache(ContactsView.as_view()), name='contacts'),
    path('portfolio', never_cache(DemoView.as_view()), name='portfolio'),
]
