from django.urls import include, path
from rest_framework import routers
from .views import ShortenURLView, redirector
from django.views.generic import RedirectView
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'shorten', ShortenURLView, basename="ShortenURL")

urlpatterns = [
    path('', RedirectView.as_view(url=settings.ROOT_REDIRECT)),
    path('', include(router.urls)),
    path('<slug:slug>', redirector)
]
