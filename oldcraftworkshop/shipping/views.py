from rest_framework.views import APIView
from rest_framework.response import Response
import json

# Create your views here.
class ShippingCost(APIView):
    def post(self, request):
        print("==================================================================")

        print("==================================================================")
        return Response({"shippingCost":13})