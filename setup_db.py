import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    print("Database and table created!")
