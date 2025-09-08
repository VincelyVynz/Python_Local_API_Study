import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute("""
select * from expenses
""")
cursor.execute("""
INSERT INTO expenses (id, item, amount) VALUES (1, "electicity bill", 1080);
""")
conn.commit()
print("working")