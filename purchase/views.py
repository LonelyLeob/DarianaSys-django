from rest_framework.generics import ListCreateAPIView
from .models import Purchase
from .serializer import PurchaseSerializer
from rest_framework.permissions import IsAuthenticated

class PurchaseAPIView(ListCreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)