from rest_framework.serializers import ModelSerializer, ImageField
from .models import Toy, ToyImage, Material

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = ('title',)

class ToyImageSerializer(ModelSerializer):
    photo = ImageField(read_only=True)
    class Meta:
        model = ToyImage
        fields = ('photo',)
    

class ToyShortSerializer(ModelSerializer):
    photos = ToyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk','title', 'price', 'photos')

class ToySerializer(ModelSerializer):
    photos = ToyImageSerializer(many=True, read_only=True)
    materials = MaterialSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('pk', 'title', 'price', 'description', 'materials', 'photos')