from rest_framework import viewsets
from .models import Product, Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, OrderSerializer



class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def get_cart(self):
        """Ensure the user has a cart(create one if not)."""
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    
    @action(detail=False, methods=['post'], url_path='add')
    def add_to_cart(self, request):
        """
        Custom action to add a product to the user's shopping cart.
    
        This action allows an authenticated user to add a product to their cart.
        If the product is already in the cart, it will update the quantity.
    
        Args:
        request (Request): Contains the 'product_id' and 'quantity' in the
        request body.
        
        Returns:
        Response: A message confirming the item was added to cart or an error.
        
        Request Body Example:
        {
        "product_id": 1,
        "quantity": 2
        }

        Response Example (Success):
        {
        "message": "Item added to the cart."
        }

        Response Example (Failure):
        {
        "error": "Product ID is required."
        }
        """
        # Retrieve product ID from the request body
        product_id = request.data.get('product_id') 

        # Retrieve quantity, default 1 if not specified 
        quantity = int(request.data.get('quantity', 1)) 

        # If no product ID is provided, return an error
        if not product_id:  
            return Response({'error': 'Product ID is required.'}, status=400)
        
        # Try to fetch the product from the database
        try:
            product = Product.objects.get(id=product_id) 
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=404)
        
        # Retrieve or create a cart for the logged-in user
        cart = self.get_cart()  

        # Check if the product is already in the cart
        item, created = CartItem.objects.get_or_create(cart=cart,
                                                       product=product)
        
        # If the product is already in the cart, increase the quantity
        if not created:
            item.quantity += quantity

        # If the product is new, set the quantity    
        else:
            item.quantity = quantity
        # Save the updated or new cart item
        item.save()

        return Response({'message': 'Item added to the cart.'}, status=200)
    

    @action(detail=False, methods=['post'], url_path='remove')
    def remove_from_cart(self, request):
        """
        Custom action to remove a product from the user's shopping cart.
    
        This action allows an authenticated user to remove a specific product 
        from their cart.
    
        Args:
        request (Request): Contains the 'product_id' in the request body.
        
        Returns:
        Response: A message confirming the item was removed from the cart or an error.
        
        Request Body Example:
        {
        "product_id": 1
        }

        Response Example (Success):
        {
        "message": "Item removed from cart."
        }

        Response Example (Failure):
        {
        "error": "Product ID is required."
        }
        """

        # Retrieve product ID from the request body
        product_id = request.data.get('product_id')
        
        # If no product ID is provided, return an error
        if not product_id:
            return Response({'error': 'Product ID is required.'}, status=400)
        
        # Try to fetch the product from the database
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product no found.'}, status=404)
        
        # Retrieve the user's cart
        cart = self.get_cart()
        try:
            # Find the cart item to delete
            item = CartItem.objects.get(cart=cart, product=product)

            # Remove item from the cart
            item.delete()
            
            return Response({'message': 'Item removed from cart.'}, status=200)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not in cart.'}, status=404)



            

