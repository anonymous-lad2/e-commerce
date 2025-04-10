# 🛍️ E-Commerce Backend API

![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-green)
![JWT Auth](https://img.shields.io/badge/Security-JWT%20Auth-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)

A robust e-commerce backend built with Django REST Framework featuring JWT authentication, API endpoints, and comprehensive testing.

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/anonymous-lad2/e-commerce.git
cd back_end

# 2. Set up virtual environment
python -m venv env
source env/bin/activate  # Linux/Mac
# env\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure database
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver

#🔧 Developer Tools
Run custom checks:
./dev_tools.sh djcheck  # Your custom development script

#🧪 Testing the API
# Run all tests
pytest

# Test specific module
pytest store/tests/test_api.py -v

# 🔐 Authentication Flow
sequenceDiagram
    User->>API: Login with credentials
    API->>User: Return JWT Tokens
    User->>API: Include Bearer token
    API->>User: Return protected data

🛠️ Tech Stack
<div align="center"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" width="80" title="Django"> <img src="https://www.django-rest-framework.org/img/logo.png" width="120" title="DRF"> <img src="https://simpleisbetterthancomplex.com/media/series/banners/django-rest-framework-3a4d1cfe.png" width="120" title="DRF"> <img src="https://jwt.io/img/pic_logo.svg" width="80" title="JWT"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/97/Sqlite-square-icon.svg" width="60" title="SQLite"> <img src="https://faker.readthedocs.io/en/master/_static/faker.png" width="80" title="Faker"> <img src="https://postman-web-assets.s3.amazonaws.com/assets/logo-default-488b1871d5fbb193068cd2587016f9cd.png" width="120" title="Postman"> <img src="https://docs.pytest.org/en/7.4.x/_static/pytest_logo_curves.svg" width="80" title="Pytest"> </div>

🌐 API Endpoints

Endpoint	Method	Description	Auth Required
/api/auth/	POST	Get JWT tokens	❌
/api/products/	GET	List all products	❌
/api/orders/	POST	Create new order	✅
/api/users/me/	GET	Get user profile	✅

📦 Project Structure
back_end/
├── ecommerce/          # Project config
├── store/              # Main app
│   ├── migrations/     # Database migrations
│   ├── tests/          # Test suite
│   ├── models.py       # Data models
│   ├── views.py        # API controllers  
│   └── serializers.py  # Data transformers
├── manage.py           # Django CLI
└── pytest.ini          # Test configuration

🧑‍💻 Development Tips
```bash
# Generate fake test data
python manage.py shell
>>> from store.factories import ProductFactory
>>> ProductFactory.create_batch(10)
```

📜 License
MIT © Pablo727







