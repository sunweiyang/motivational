
from django.urls import path
from . import views

app_name = "motivational"

urlpatterns = [
    path('quote/', views.QuoteAPIView.as_view()),
    path('image_address/', views.ImageAddressAPIView.as_view())
]
