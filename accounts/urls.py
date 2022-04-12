# from auth.views import MyObtain
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path('sellers/', views.ProductSellerViewSet.as_view({'get':'list'}), name='home'),
    path('customers/', views.ProductBuyerViewSet.as_view({'get':'list'}), name='homex'),
    path('sellers/ratings/all', views.ProductSellerRatingViewSet.as_view({'get':'list'}), name='homexb'),
    path('register/customer', views.customer_register_view),
    path('register/seller', views.seller_register_view),
    path('rate/', views.rate_seller_view),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view())
]