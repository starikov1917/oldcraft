from django.shortcuts import render
from rest_framework import generics
from .models import Image
from .serializers import titleImageSerializer
# Create your views here.
class titleImageApiView(generics.RetrieveAPIView):
    queryset = Image
    serializer_class = titleImageSerializer