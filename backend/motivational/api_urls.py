from django.urls import path

from . import api

urlpatterns = [
    path('quote', api.QuoteAPIView.as_view()),
    path('image_address', api.ImageAddressAPIView.as_view())
]
