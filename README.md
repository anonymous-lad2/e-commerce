# 🛍️ E-Commerce Backend API

<div align="center">
  <img src="https://cdn.worldvectorlogo.com/logos/django.svg" width="100">
  <img src="https://www.django-rest-framework.org/img/logo.png" width="180" style="margin:0 20px">
  <img src="https://jwt.io/img/logo-asset.svg" width="100" style="background:#000;padding:10px;border-radius:5px">
</div>

## 🚀 Quick Start
```bash
git clone https://github.com/anonymous-lad2/e-commerce.git
cd e-commerce/back_end
python -m venv env
source env/bin/activate  # Linux/Mac
# env\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔐 Authentication Flow
```mermaid
Copy
Edit
sequenceDiagram
    participant User
    participant API
    User->>API: POST /api/auth/
    API->>User: JWT Tokens
    User->>API: Authorization: Bearer <token>
    API->>User: Protected Data
```
## 🌐 API Endpoints
Endpoint	Method	Description	Auth Required
/api/auth/	POST	Obtain JWT tokens	❌ No
/api/products/	GET	List all products	❌ No
/api/orders/	POST	Create new order	✅ Yes
/api/users/me/	GET	Get user profile	✅ Yes

## 🔧 Developer Tools
```bash
Copy
Edit
./dev_tools.sh djcheck  # Run custom Django checks
pytest                  # Run all tests
python manage.py shell  # Open Django shell
```
Example for test data in shell:

```python
Copy
Edit
from store.factories import ProductFactory
ProductFactory.create_batch(5)
```
## 📦 Project Structure
```bash
Copy
Edit
e-commerce/
└── back_end/
    ├── ecommerce/       # Django project config
    ├── store/           # Main app
    │   ├── migrations/  # Database migrations
    │   ├── tests/       # Test suite
    │   ├── models.py    # Data models
    │   ├── views.py     # Business logic
    │   └── serializers/ # Data transformers
    ├── manage.py        # Django CLI
    └── pytest.ini       # Pytest config
```
## 📜 License
MIT © Pablo727

