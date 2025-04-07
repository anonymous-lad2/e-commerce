from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet
from .views_user import UserViewSet
from .views_cart import CartViewSet



router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'users', UserViewSet)
router.register(r'cart', CartViewSet)


urlpatterns = [
    # Register the router with URLs
    path('', include(router.urls)),
]