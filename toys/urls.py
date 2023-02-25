from django.urls import path
from .views import ToyAPIView, index

urlpatterns = [
    path("test/", index),
    path('all/', ToyAPIView.as_view())
]
