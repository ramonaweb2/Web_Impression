from django.urls import path

from webImpression.web.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('services', ServicesView.as_view(), name='services'),
    path('izrabotka-wordpress-website', WordpressWebsiteView.as_view(), name='wordpress'),
    path('izrabotka-custom-website', CustomWebsiteView.as_view(), name='custom_website'),
    path('about', AboutView.as_view(), name='about'),
    path('pricing', PricingView.as_view(), name='pricing'),
    path('contact', ContactsView.as_view(), name='contact'),
    path('project', ProjectView.as_view(), name='project'),
    path('validate', SubscriptionView.as_view(), name='validate'),
    path('newsletter', SubscriptionView.as_view(), name='newsletter'),
    path('robots.txt', RobotsTxtView.as_view(content_type="text/plain"), name='robots'),
    path('sitemap.xml', SitemapView.as_view(content_type="text/plain"), name='sitemap')
]
