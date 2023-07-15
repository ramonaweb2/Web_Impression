from django.urls import path

from webImpression.web.views import *

urlpatterns = [
    path('', never_cache(HomePageView.as_view()), name='homepage'),
    path('services', never_cache(ServicesView.as_view()), name='services'),
    path('contacts', never_cache(ContactsView.as_view()), name='contacts'),
    path('web-design', never_cache(WebDesignView.as_view()), name='web-design'),
    path('seo', never_cache(SEOView.as_view()), name='seo'),
]
