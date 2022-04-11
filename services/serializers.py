from rest_framework import serializers

from accounts.models import ProductManager

from .models import Product, ProductOrder
from accounts.serializers import ProductSellerSerializer



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ('slug',)
        fields = [
            'id', 'name', 'slug','description', 'quantity', 'price', \
            'ratings', 'details', 'seller'
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


class ProductOrderSerializer(serializers.ModelSerializer):
    model = ProductOrder
    fields = [
        'id', 'address', 'ordered', 'reference_code', 'order_date', 'products'
    ]
