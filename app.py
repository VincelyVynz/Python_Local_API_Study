from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def return_json():
    return jsonify({
        "message": "hello world"
    })


@app.route('/expenses')
def return_expenses():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "item": row[1],
            "amount": row[2]
        })
    return jsonify(data)


@app.route('/add_data')
def add_data():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO expenses (item, amount)
            VALUES ("electricity bill", 1080);
        """)
        conn.commit()
        print("working")
        return "Data added successfully!"
    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run(debug=True)
