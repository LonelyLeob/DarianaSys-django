from django.urls import path
from .views import RegisterView, LoginView, RefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', RefreshView.as_view())
]
