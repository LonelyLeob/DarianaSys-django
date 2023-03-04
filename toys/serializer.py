from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from .models import Toy, ToyImage, Material
from comments.models import Comment

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
    comments = SerializerMethodField(read_only=True)
    class Meta:
        model = Toy
        fields = ['pk', 'title', 'price', 'description', 'materials', 'photos', 'comments']

    def get_comments(self, obj):
        comment = Comment.objects.filter(toy=obj).values()
        return comment