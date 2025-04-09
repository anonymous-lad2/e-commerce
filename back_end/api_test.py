import requests

BASE_URL = "http://127.0.0.1:8000"
LOGIN_URL = f"{BASE_URL}/api/token/"
CART_URL = f"{BASE_URL}/api/cart/"


# Credentials
credentials = {
    "username": "admin",
    "password": "ecommerce",
}

# Step 1: Get token
response = requests.post(LOGIN_URL, data=credentials)

if response.status_code == 200:
    tokens = response.json()
    access_token = tokens["access"]
    print("✅ Access token obtained successfully.")

    # Step 2: Use token to get cart
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    cart_response = requests.get(CART_URL, headers=headers)

    if cart_response.status_code == 200:
        print("🛒 Cart contents:")
        print(cart_response.json())

    else:
        print("❌ Failed to obtain token.")
        print("Status code:", response.status_code)
        print("Response:", response.text)

