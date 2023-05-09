from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .logic import calculate_postage

# Create your views here.
class ShippingCost(APIView):
    def post(self, request):
        print(request.data)
        location_id = request.data["pk"]
        weight = request.data["weight"]
        subtotal = 144.2
        return Response({"shippingCost":calculate_postage(location_id, weight, subtotal)})