from rest_framework import serializers
from .models import Toy, ToyImage, Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('title',)

class ToyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToyImage
        fields = ('pk',)
    

class ToyShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('pk','title', 'price')

class ToySerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk', 'title', 'price', 'description', 'materials')

