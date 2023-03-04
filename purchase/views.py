from rest_framework.generics import ListAPIView
from .models import Purchase
from .serializer import PurchaseHistorySerializer

class PurchaseAPIView(ListAPIView):
    serializer_class = PurchaseHistorySerializer

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)