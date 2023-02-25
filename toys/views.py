from rest_framework import generics
from .models import Toy
from .serializer import ToySerializer
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    return HttpResponse("HelloWorld")


class ToyAPIView(generics.ListAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer