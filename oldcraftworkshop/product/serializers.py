from rest_framework import serializers
from .models import Product
from gallery.serializers import titleImageSerializer



class ProductSerializer(serializers.ModelSerializer):
    titlePhoto = titleImageSerializer()
    class Meta:
        model = Product
        fields = ("slug", "title", 'rating', 'isActive', 'weight','price',
                  'voluametricWeight', 'productionTime', 'gpostCode', 'titlePhoto', 'description',
                  'isCounatable', 'availableQuantity', 'subsection', 'section')

