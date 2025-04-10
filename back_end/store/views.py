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
        # Auto-assign the logged-in user
        serializer.save()

    # Custom action to update order status
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        """
        Custom action to update the status of an order.
        This action allows an authenticated user (typically an admin) to update the 
        status of an existing order.

        Args:
        request (Request): Contains the new 'status' in the request body.
        pk (int): The primary key (ID) of the order to update.

        Returns:
        Response: A response containing the updated order status.
        
        Response Example (Success):
        {
        "status": "shipped"
        }

        Response Example (Failure):
        {
        "error": "Invalid status value."
        }
        """

        # Retrieve the order based on the provided pk
        order = self.get_object() 

        # Update the order's status with the status provided in request body,
        # defaulting to current status
        order.status = request.data.get('status', order.status)
        
        # Save the updated order to the database
        order.save()  

        # Return the udpated status in the response
        return Response({'status': order.status})
                                                   

def index(request):
    """
    A simple view for the store app's index page.
    
    Returns:
        HttpResponse: A basic response indicating the app is running.
    
    Response Example:
    "Hello from the store app!"
    """
    return HttpResponse("Hello from the store app!")