import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="user1", password="password123")


@pytest.fixture
def auth_client(api_client, user):
    response = api_client.post('/api/token/', {"username": "user1",
                                                "password": "password123"})
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.mark.django_db
def test_product_list(api_client):
    Product.objects.create(name="Videogame", description="Cool game", price=99.99,
                           stock=10)
    response = api_client.get('/api/products/')
    assert response.status_code == 200
    assert len(response.data) > 0


@pytest.mark.django_db
def test_create_order_requires_auth(api_client):
    response = api_client.post('/api/orders/', {})
    assert response.status_code == 401


@pytest.mark.django_db
def test_create_order_success(auth_client, user):
    product = Product.objects.create(
        name="Gamepad", description="Game controller", price=69.99, stock=15)
    response = auth_client.post('/api/orders/', {
        "products": [product.id],
        "total_price": "69.99",
        "user": user.id, 
        "email": "user1@example.com",
        "payment_method": "credit_card", 
        "order_date": timezone.now().isoformat(),
        "discount": "0.00",
        "payment_status": "pending" 
    })

    print("Response data:", response.data)

    assert response.status_code == 201
    assert response.data['status'] == "pending"
