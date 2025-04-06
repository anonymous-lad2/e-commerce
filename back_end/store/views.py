from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # Publicly visible


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required

    def perform_create(self, serializer):
        # Auto-assign the logged-in user.
        serializer.save(user=self.request.user)

    # Custom action to update order status
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        order.status = request.data.get('status', order.status)
        order.save()
        return Response({'status': order.status})

def index(request):
    return HttpResponse("Hello from the store app!")