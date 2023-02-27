from rest_framework.generics import ListAPIView
from .models import Toy
from .serializer import ToyShortSerializer, ToySerializer

# def index(request: HttpRequest):
#     return HttpResponse("HelloWorld")

class ToysShortAPIView(ListAPIView):
    serializer_class = ToyShortSerializer

    def get_queryset(self):
        return Toy.objects.all()

class ToyAPIView(ListAPIView):
    serializer_class = ToySerializer
    
    def get_queryset(self):
        return Toy.objects.filter(id=self.kwargs['id'])