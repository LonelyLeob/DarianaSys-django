from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from .models import Comment

class CommentHistorySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['commenter', 'comment', 'mark']

class CommentCreateSerializer(ModelSerializer):
    commenter = HiddenField(
        default=CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ['toy', 'comment', 'commenter', 'mark']
