from django.urls import path
from .views import PurchaseAPIView

urlpatterns = [
    path('history/', PurchaseAPIView.as_view())
]
