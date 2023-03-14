from rest_framework import serializers
from .models import Purchase, PurchaseItem
from toys.models import Toy


class PurchaseItemSerializer(serializers.ModelSerializer):
    toy = serializers.PrimaryKeyRelatedField(queryset=Toy.objects.all())
    total_item_price = serializers.SerializerMethodField("_total_item_price", read_only=True)
    class Meta:
        model = PurchaseItem
        fields = ['quantity', 'toy', 'total_item_price']
        read_only_fields = ['total_item_price', 'purchase']
        depth=1
    
    def _total_item_price(self, obj):
        return obj.quantity * obj.toy.price


class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.SerializerMethodField("_total_price", read_only=True)
    class Meta:
        model = Purchase
        fields = ['id', 'status', 'user', 'created_at', 'items', 'total_price']
        read_only_fields = ['id', 'status', 'user', 'created_at', 'total_price']

    def create(self, validated_data):
        items = validated_data.pop('items', None)
        purchase = Purchase.objects.create(**validated_data)
        pur_items = []
        if items:
            for item in items:
                purchase_item = PurchaseItem.objects.create(**item)
                pur_items.append(purchase_item)
        purchase.items.set(pur_items)
        return purchase

    def _total_price(self, obj):
        x=0
        for i in obj.get_total():
            x+=i
        return x