from .models import Image
from rest_framework import serializers

class titleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields  = ("image", "title")

