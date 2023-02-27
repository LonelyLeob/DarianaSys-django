from django.urls import path
from .views import PurchaseView

urlpatterns = [
    # path("test/", index)
    path('buy/', PurchaseView.as_view())
]
