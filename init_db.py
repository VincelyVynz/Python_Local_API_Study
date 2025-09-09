import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    stock INTEGER
    )""")

products_stock = [
    {"name": "Laptop", "price": 35000, "stock": 22},
    {"name": "Wireless Mouse", "price": 890, "stock": 47},
    {"name": "Mechanical Keyboard", "price": 1200, "stock": 50},
    {"name": "Headphones", "price": 1500, "stock": 34},
    {"name": "Cooling Pad", "price": 750, "stock": 8}
]

for product in products_stock:
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
                   (product["name"], product["price"], product["stock"]))

conn.commit()
conn.close()