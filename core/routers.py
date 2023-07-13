from rest_framework import routers

from core.usermanagement.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.restaurant.viewsets import RestaurantViewSets, BusinessHourViewSets
from core.product.viewsets import ProductViewSets
from core.product_categories.viewsets import ProductCategoriesViewsets
from core.orders.viewsets import OrdersViewsets, UserOrderViewsets
from django.urls import re_path
from core.product.viewsets import ProductSearchViewsets

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='register')
router.register(r'auth/login', LoginViewSet, basename='login')
router.register(r'auth/refresh', RefreshViewSet, basename='refresh')
router.register(r'restaurant', RestaurantViewSets, basename='restaurant')
router.register(r'restaurant/business-hour', BusinessHourViewSets, basename='business_hour')
router.register(r'products', ProductViewSets, basename='product')
router.register(r'product-categories', ProductCategoriesViewsets, basename='product_categories')
router.register(r'orders', OrdersViewsets, basename='orders')
router.register(r'order/user', UserOrderViewsets, basename='user_order')
router.urls.append(re_path('search_products/', ProductSearchViewsets.as_view(), name='search_products'))

urlpatterns =[
    *router.urls
]