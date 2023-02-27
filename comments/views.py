from rest_framework.request import HttpRequest
from rest_framework.views import APIView
from .serializer import CommentSerializer

# def index(request: HttpRequest):
#     return HttpResponse("HelloWorld")

class CommentView(APIView):
    def post(self, request: HttpRequest):
        serializer = CommentSerializer