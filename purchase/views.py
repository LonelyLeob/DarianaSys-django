from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Purchase
from .serializer import PurchaseSerializer, PurchaseBuySerializer
from rest_framework.permissions import IsAuthenticated

class PurchaseAPIView(ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Purchase.objects.all()

class PurchaseBuyAPIView(CreateAPIView):
    serializer_class = PurchaseBuySerializer
    permission_classes = (IsAuthenticated, )
