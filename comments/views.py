from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import CommentCreateSerializer

# def index(request: HttpRequest):
#     return HttpResponse("HelloWorld")

class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,]