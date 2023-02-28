from rest_framework import serializers
from .models import Toy, Material
class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('pk','title')

class ToyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('pk','title', 'price')

class ToySerializer(serializers.ModelSerializer):
    materials = MaterialsSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk', 'title', 'price', 'description', 'materials')

