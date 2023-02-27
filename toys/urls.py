from django.urls import path
from .views import ToysShortAPIView, ToyAPIView

urlpatterns = [
    # path("test/", index),
    path('all/', ToysShortAPIView.as_view()),
    path('concrete/<int:id>', ToyAPIView.as_view()),
]
