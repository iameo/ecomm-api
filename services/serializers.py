from rest_framework import serializers

from accounts.models import ProductManager

from .models import Product
from accounts.serializers import ProductSellerSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # read_only_fields = ('seller',)
        fields = [
            'id', 'name', 'slug','description', 'quantity', 'price', \
            'ratings', 'details'
            ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name','slug', 'created_at', 'updated_at', \
            'description', 'quantity', 'price', 'ratings', 'details', \
            'seller', 'product_images'
            ]
        depth = 1


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManager
        fields = [
            'acc_type', 'ratings', 'last_service', 'availability',\
            'rendered_services', 'products']
        