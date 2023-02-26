from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializer import UserSerializer
from .models import User
import jwt
from datetime import timedelta, datetime

class RegisterView(APIView):
    def post(self, request: HttpRequest):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request: HttpRequest):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("Пользователь не найден")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Неверный пароль")

        return Response({
            "message":"Пользователь вошел",
        })

class RefreshView(APIView):
    def get(self, request: HttpRequest):
        pass