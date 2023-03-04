from rest_framework.serializers import ModelSerializer, CharField, DateTimeField, SerializerMethodField
from .models import Purchase, PurchaseItem
from toys.serializer import ToySerializer

class PurchaseItemHistorySerializer(ModelSerializer):
    toy_obj = SerializerMethodField(read_only=True)
    total_item_price = SerializerMethodField()
    class Meta:
        model = PurchaseItem
        fields = ['pk', 'toy_obj', 'quantity', 'total_item_price']

    def get_total_item_price(self, obj):
        return obj.toy.price * obj.quantity

    def get_toy_obj(self, obj):
        return ToySerializer(obj.toy, many=False, read_only=True).data

class PurchaseHistorySerializer(ModelSerializer):
    items = PurchaseItemHistorySerializer(many=True, read_only=False)
    status = CharField(read_only=True, default="WAIT")
    created_at = DateTimeField(read_only=True)
    total_price = SerializerMethodField(read_only=True)
    class Meta:
        model = Purchase
        fields = ['pk', 'user', 'status', 'created_at', 'items', 'total_price']

    def get_total_price(self, obj):
        x=0
        for i in obj.get_total():
            x+=i
        return x