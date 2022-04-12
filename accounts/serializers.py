from rest_framework import serializers

from .models import ProductManager, ProductBuyer, SellerRating
from rest_framework.permissions import IsAuthenticated


class ProductSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManager
        fields = ['acc_type', 'availability', 'ratings', 'products', 'last_service', 'rendered_services']

  
class ProductBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBuyer
        fields = ['acc_type', 'purchased_counts']


class RateSellerSerializer(serializers.ModelSerializer):
    """Rate a Product Owner as a Customer"""
    rate = serializers.FloatField(required=True)
    class Meta:
        model = SellerRating
        fields = ['seller', 'customer', 'rate']
        extra_kwargs = {
            'seller': {'required':True},
            'customer': {'required':True},
        } 
    
    def validate(self, attrs):
        rate_ = attrs['rate']
        if rate_ < 0 or rate_ > 5: #FloatField already makes sure null is not allowed
            raise serializers.ValidationError("You can only rate a seller 0-5 stars")
        return attrs

