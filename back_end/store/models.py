from django.db import models
from django.contrib.auth.models import User
from .constants import ORDER_STATUS_CHOICES, PAYMENT_METHOD_CHOICES


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)
    image_url = models.URLField(default='http://example.com/placeholder_image.jpg')

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(default='default@example.com')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES,
                               default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20,
                                       choices=PAYMENT_METHOD_CHOICES,
                                       default='credit_card')
    payment_status = models.CharField(max_length=20, default="pending")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


