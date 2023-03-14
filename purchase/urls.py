from django.urls import path
from .views import PurchaseAPIView

urlpatterns = [
    path('', PurchaseAPIView.as_view()),
]
