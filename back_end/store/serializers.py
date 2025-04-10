from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Order
from .constants import ORDER_STATUS_CHOICES, PAYMENT_METHOD_CHOICES



class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    category = serializers.CharField(max_length=30)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)
    rating = serializers.DecimalField(max_digits=4, decimal_places=1)
    stock = serializers.IntegerField()
    image_url = serializers.URLField()

    class Meta:
        model = Product
        
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    email = serializers.EmailField()
    payment_method = serializers.ChoiceField(choices=PAYMENT_METHOD_CHOICES)
    order_date = serializers.DateTimeField()
    discount = serializers.DecimalField(max_digits=5, decimal_places=2, 
                                        required=False, default=0.0)
    payment_status = serializers.ChoiceField(choices=ORDER_STATUS_CHOICES)

 
    class Meta:
        model = Order
        fields = '__all__'
    

    def create(self, validated_data):
        # Get the logged-in user
        user = self.context['request'].user
        
        # Inject user into validated data
        validated_data['user'] = user

        # Ensure discount is set to 0.0 if not provided
        if 'discount' not in validated_data:
            validated_data['discount'] = 0.0
            
        return super().create(validated_data)
    
    def validate_discount(self, value):
        if value > 0.1:
            raise serializers.ValidationError("Discount cannot be"
            " greater than 10%.")
        if value < 0:
            raise serializers.ValidationError("Discount cannot be negative.")
        
