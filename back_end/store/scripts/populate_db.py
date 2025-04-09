import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# Set DJANGO_SETTINGS_MODULE environment variable to point to settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Set up Django
import django
django.setup()

import random
from faker import Faker
from store.models import Product
from video_game_provider import VideoGameProvider
from store.models import Product


fake = Faker()
fake.add_provider(VideoGameProvider)

def create_video_game_products(n=25):
    for _ in range(n):
        title = fake.video_game_title()
        category = fake.video_game_category()
        description = fake.video_game_description()
        price = round(random.uniform(10, 500), 2)
        stock = random.randint(5, 100)

        Product.objects.create(
            name=title, description=description, price=price, stock=stock,
            category=category)
        print(f"Created game: {title} - {category}")


# Example usage
if __name__ == '__main__':
    create_video_game_products(25)