from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/show_products")
def show_products():
    try:
        response = requests.get("http://localhost:5000/products")
        products = response.json()
        print(products)
        return jsonify(products)
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)})

@app.route("/show_stock")
def show_stock():
    try:
        response = requests.get("http://localhost:5000/stock")
        response.raise_for_status()
        stock = response.json()
        return jsonify(stock)
    except requests.exceptions.RequestException as err:
        return jsonify({"error": str(err)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)