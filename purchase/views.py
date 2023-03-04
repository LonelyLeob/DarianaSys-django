from rest_framework.generics import ListCreateAPIView
from .models import Purchase
from .serializer import PurchaseHistorySerializer

# def index(request: HttpRequest):
#     return HttpResponse("HelloWorld")

class PurchaseAPIView(ListCreateAPIView):
    serializer_class = PurchaseHistorySerializer

    def get_queryset(self):
        return Purchase.objects.filter(user="1")