from django.urls import path

from webImpression.web.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
]
