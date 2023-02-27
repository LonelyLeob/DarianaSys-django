from rest_framework.request import HttpRequest
from rest_framework.views import APIView
from .serializer import PurchaseSerializer

# def index(request: HttpRequest):
#     return HttpResponse("HelloWorld")

class PurchaseView(APIView):
    def post(self, request: HttpRequest):
        serializer = PurchaseSerializer