from rest_framework.serializers import ModelSerializer
from .models import Purchase

class PurchaseSerializer(ModelSerializer):
    model = Purchase