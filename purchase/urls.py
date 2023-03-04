from django.urls import path
from .views import PurchaseAPIView

urlpatterns = [
    # path("test/", index)
    path('buy/', PurchaseAPIView.as_view())
]
