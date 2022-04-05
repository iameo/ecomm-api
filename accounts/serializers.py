from rest_framework import serializers

from .models import ProductManager, ProductBuyer, SellerRating


class ProductSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManager
        fields = ['availability', 'ratings', 'products', 'acc_type', 'last_service', 'rendered_services']


class ProductBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBuyer
        fields = ['acc_type', 'purchased_counts']


class ProductSellerRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerRating
        fields = ['seller', 'customer', 'rate']
