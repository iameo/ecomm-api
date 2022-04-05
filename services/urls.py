from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.ProductViewSet.as_view({'get':'list'}), name='home'),
    path('sellers/', views.SellerProductViewSet.as_view({'get':'list'}), name='homex'),
    path('<int:pk>/', views.product_detail_view),
    path('product/', views.product_create_view),
]