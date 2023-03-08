from rest_framework import serializers
from .models import Toy, ToyImage
from comments.serializer import CommentHistorySerializer

class ToyImageSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(read_only=True)
    class Meta:
        model = ToyImage
        fields = ['photo']

class ToyShortSerializer(serializers.ModelSerializer):
    photos = ToyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ('id','title', 'price', 'photos')

class ToySerializer(serializers.ModelSerializer):
    comments = CommentHistorySerializer(many=True, read_only=True)
    materials = serializers.StringRelatedField(many=True, read_only=True)
    photos = ToyImageSerializer(many=True, read_only=True)
    class Meta:
        model = Toy
        fields = ['id', 'title', 'price', 'description', 'materials', 'photos', 'comments']
        depth=1