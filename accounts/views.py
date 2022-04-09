from .models import ProductBuyer, ProductManager, SellerRating, CustomUser
from .serializers import ProductSellerSerializer, ProductBuyerSerializer, ProductSellerRatingSerializer
from .auth_serializers import CustomerRegistrationSerializer, SellerRegistrationSerializer
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductSellerViewSet(viewsets.ViewSet):
    """
    API endpoint that allows product sellers to be viewed (and their products and customers)
    """
    def list(self, request):
        queryset = ProductManager.objects.all()
        serializer = ProductSellerSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

class ProductBuyerViewSet(viewsets.ViewSet):
    """
    API endpoint that allows customers to be viewed.
    """
    def list(self, request):
        queryset = ProductBuyer.objects.all()
        serializer = ProductBuyerSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

class ProductSellerRatingViewSet(viewsets.ViewSet):
    """
    API endpoint that shows product sellers' ratings.
    """
    def list(self, request):
        queryset = SellerRating.objects.all()
        serializer = ProductSellerRatingSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

class CustomerCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating customer accounts
    """
    queryset = CustomUser
    serializer_class = CustomerRegistrationSerializer

class SellerCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating seller accounts
    """
    queryset = CustomUser
    serializer_class = SellerRegistrationSerializer

customer_register_view = CustomerCreateAPIView.as_view()
seller_register_view = SellerCreateAPIView.as_view()