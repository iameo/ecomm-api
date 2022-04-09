from unicodedata import name
from django.urls import path, re_path

from . import views


urlpatterns = [
    # path('products/', views.ProductViewSet.as_view({'get':'list'}), name='home'),
    path('sellers/', views.SellerProductViewSet.as_view({'get':'list'}), name='homex'),
    path('product/<int:pk>/', views.product_detail_view),
    path('products/', views.product_list_create_view),
]