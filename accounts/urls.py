from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('sellers/', views.ProductSellerViewSet.as_view({'get':'list'}), name='home'),
    path('customers/', views.ProductBuyerViewSet.as_view({'get':'list'}), name='homex'),
    path('sellers/ratings/all', views.ProductSellerRatingViewSet.as_view({'get':'list'}), name='homexb'),
]