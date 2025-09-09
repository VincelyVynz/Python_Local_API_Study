import requests


try:
    response = requests.get("http://127.0.0.1:5000/products")
    response.raise_for_status()
    data = response.json()
    for product in data:
        print(f"Name: {product['name']}\nPrice: {product['price']}\nStock: {product['stock']}\n")
except requests.exceptions.RequestException as err:
    print(err)


try:
    response = requests.get("http://127.0.0.1:5000/stock")
    response.raise_for_status()
    data = response.json()
    for product in data:
        print(f"Name: {product['name']}\nPrice: {product['price']}\nStock: {product['stock']}\n")
except requests.exceptions.RequestException as err:
    print(err)

