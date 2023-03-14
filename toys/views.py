from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Toy
from .serializer import ToyShortSerializer, ToySerializer

class ToysShortAPIView(ListAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToyShortSerializer

class ToyAPIView(RetrieveAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    lookup_field = 'id'
