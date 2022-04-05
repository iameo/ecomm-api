from .models import ProductBuyer, ProductManager, SellerRating
from .serializers import ProductSellerSerializer, ProductBuyerSerializer, ProductSellerRatingSerializer
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductSellerViewSet(viewsets.ViewSet):
    """
    API endpoint that allows product sellers to be viewed.
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