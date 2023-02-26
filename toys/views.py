from rest_framework import generics, request
from .models import Toy
from .serializer import ToyShortSerializer, ToySerializer
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    return HttpResponse("HelloWorld")


class ToysShortAPIView(generics.ListAPIView):
    serializer_class = ToyShortSerializer

    def get_queryset(self):
        return Toy.objects.all()

class ToyAPIView(generics.ListAPIView):
    serializer_class = ToySerializer
    
    def get_queryset(self):
        return Toy.objects.filter(id=self.kwargs['id'])