from rest_framework import serializers
from .models import Product, Product_option
from gallery.serializers import titleImageSerializer


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_option
        fields = ("slug", "title", "price")
class ProductSerializer(serializers.ModelSerializer):
    titlePhoto = titleImageSerializer()

    #options = serializers.StringRelatedField(many=True, read_only=True)
    options = ProductOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ("slug", "title", 'rating', 'isActive', 'weight','price',
                  'voluametricWeight', 'productionTime', 'gpostCode', 'titlePhoto', 'description',
                  'isCounatable', 'availableQuantity', 'subsection', 'section', "options")


