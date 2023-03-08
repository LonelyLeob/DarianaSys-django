from django.urls import path
from .views import PurchaseAPIView, PurchaseBuyAPIView

urlpatterns = [
    path('history/', PurchaseAPIView.as_view()),
    path('buy/', PurchaseBuyAPIView.as_view()),
]
