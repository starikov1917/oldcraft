from django.shortcuts import render
from rest_framework import generics
from .models import Location
from .serializers import LocationListSerializer
# Create your views here.



class BookListView(generics.ListCreateAPIView):
    model = Location
    queryset = Location.objects.all()
    serializer_class = LocationListSerializer