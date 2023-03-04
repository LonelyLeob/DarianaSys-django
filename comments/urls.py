from django.urls import path
from .views import CommentCreateAPIView

urlpatterns = [
    path("", CommentCreateAPIView.as_view())
]
