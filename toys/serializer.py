from rest_framework import serializers
from .models import Toy

class ToyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('title', 'price')

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('title', 'price', 'description', 'materials')