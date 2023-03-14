from django.urls import path
from .views import ToysShortAPIView, ToyAPIView

urlpatterns = [
    path('', ToysShortAPIView.as_view()),
    path('<int:id>/', ToyAPIView.as_view()),
]
