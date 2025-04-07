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
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({'error': 'Product ID is required.'}, status=400)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found.'}, status=404)
        
        cart = self.get_cart()
        item, created = CartItem.objects.get_or_create(cart=cart,
                                                        product=product)
        
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return Response({'message': 'Item added to the cart.'}, status=200)
    

    @action(detail=False, methods=['post'], url_path='remove')
    def remove_from_cart(self, request):
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({'error': 'Product ID is required.'}, status=400)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product no found.'}, status=404)
        
        cart = self.get_cart()
        try:
            item = CartItem.objects.get(cart=cart, product=product)
            item.delete()
            return Response({'message': 'Item removed from cart.'}, status=200)
        except CartItem.DoesNotExist:
            return Response({'error': 'Item not in cart.'}, status=404)



            

