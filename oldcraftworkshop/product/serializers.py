from rest_framework import serializers
from .models import Product




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("slug", "title", 'rating', 'isActive', 'weight','price',
                  'voluametricWeight', 'productionTime', 'gpostCode', 'titlePhoto', 'description',
                  'isCounatable', 'availableQuantity', 'subsection', 'section')

