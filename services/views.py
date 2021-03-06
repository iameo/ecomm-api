from accounts.models import ProductManager
from .models import Product, ProductOrder
from .serializers import (
    ProductSerializer, SellerSerializer, ProductDetailSerializer, ProductOrderSerializer
    )
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.utils.text import slugify
from rest_framework import serializers

from permissions import SellerProductEditOrCreate

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint for creating and listing products

    GET:
        returns a list of products (including the sellers' info)
    POST:
        create a new product instance
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        quantity = serializer.validated_data.get('quantity')
        slug = serializer.validated_data.get('slug', None)
        product_name = serializer.validated_data.get('name')

        if quantity < 1:
            raise serializers.ValidationError("Product Quantity can not be less than 1")

        if slug is None:
            serializer.validated_data['slug'] = slugify(product_name)
        
        serializer.save()
    
    def list(self, request):
        queryset = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)


class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for a particular product to be viewed
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class SellerProductViewSet(viewsets.ViewSet):
    """
    API endpoint that shows sellers their products in the DB as well as customers.
    """
    def list(self, request):
        queryset = ProductManager.objects.all().order_by('-acc_type__joined')
        serializer = SellerSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)



product_detail_view = ProductRUDAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer)