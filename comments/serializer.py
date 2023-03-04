from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from .models import Comment

class CommentHistorySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'user',]

class CommentCreateSerializer(ModelSerializer):
    commenter = HiddenField(
        default=CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ['toy', 'positive', 'negative', 'comment', 'commenter']
