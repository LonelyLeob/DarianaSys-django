from rest_framework import serializers
from .models import Toy, ToyImage, Material

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('title',)

class ToyImageSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(read_only=True)
    class Meta:
        model = ToyImage
        fields = ('pk', 'photo')
    

class ToyShortSerializer(serializers.ModelSerializer):
    photos = ToyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk','title', 'price', 'photos')

class ToySerializer(serializers.ModelSerializer):
    photos = ToyImageSerializer(many=True, read_only=True)
    materials = MaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk', 'title', 'price', 'description', 'materials', 'photos')