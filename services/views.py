
from matplotlib.style import context

from accounts.models import ProductManager
from .models import Product
from .serializers import ProductSerializer, SellerSerializer, ProductDetailSerializer
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for creating products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        quantity = serializer.validated_data.get('quantity')
        if quantity <= 0:
            raise ValueError("Product Quantity can not be less than 1")
        serializer.save()



class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint for a particular product to be viewed
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductViewSet(viewsets.ViewSet):
    """
    API endpoint that allows products to be viewed.
    """
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)


class SellerProductViewSet(viewsets.ViewSet):
    """
    API endpoint that shows sellers their products in the DB as well as customers.
    """
    def list(self, request):
        queryset = ProductManager.objects.all()
        serializer = SellerSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)

product_detail_view = ProductDetailAPIView.as_view()
product_create_view = ProductCreateAPIView.as_view()