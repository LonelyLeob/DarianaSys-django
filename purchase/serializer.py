from rest_framework import serializers, response
from .models import Purchase, PurchaseItem
from toys.models import Toy
from toys.serializer import ToySerializer

class PurchaseItemSerializer(serializers.ModelSerializer):
    toy = ToySerializer(many=False)
    total_item_price = serializers.SerializerMethodField("_total_item_price")
    class Meta:
        model = PurchaseItem
        fields = ['quantity', 'toy', 'total_item_price']
        read_only_fields = ['total_item_price', 'purchase']
    
    def _total_item_price(self, obj):
        return obj.quantity * obj.toy.price


class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.SerializerMethodField("_total_price")
    class Meta:
        model = Purchase
        fields = ['id', 'status', 'user', 'created_at', 'items', 'total_price']
        read_only_fields = ['id', 'status', 'user', 'created_at', 'total_price']

    def _total_price(self, obj):
        x=0
        for i in obj.get_total():
            x+=i
        return x


class PurchaseItemBuySerializer(serializers.ModelSerializer):
    toy = serializers.IntegerField(write_only=True)
    class Meta:
        model = PurchaseItem
        fields = ['quantity', 'toy']
        write_only_fields = ['quantity', 'toy']
    
class PurchaseBuySerializer(serializers.ModelSerializer):
    items = PurchaseItemBuySerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Purchase
        fields = ['user', 'items']
        read_only_fields = ['user']

    def create(self, validated_data):
        items = validated_data.pop('items', None)
        purchase = Purchase.objects.create(**validated_data)
        if items:
            for item in items:
                toy_id = item.pop('toy', False)
                toy = Toy.objects.filter(id=toy_id).first()
                if toy:
                    PurchaseItem.objects.create(**item, purchase=purchase, toy=toy)
        return purchase