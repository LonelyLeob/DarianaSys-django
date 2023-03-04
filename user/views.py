from rest_framework.generics import CreateAPIView
from .serializer import UserRegisterSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer