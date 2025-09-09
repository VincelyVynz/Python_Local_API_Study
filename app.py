from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def working():
    return "Working"

@app.route('/products')
def get_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    products = []
    for row in rows:
        products.append({"id": row[0], "name": row[1], "price": row[2], "stock": row[3]})
    conn.close()
    return jsonify(products)

@app.route('/stock')
def get_stock():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE stock > 30")
    rows = cursor.fetchall()
    stock = []
    for row in rows:
        stock.append({"id": row[0], "name": row[1], "price": row[2], "stock": row[3]})
    conn.close()
    return jsonify(stock)

if __name__ == '__main__':
    app.run(debug=True, port=5000)