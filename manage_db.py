import sqlite3
conn = sqlite3.connect("connect database")

conn.execute("CREATE TABLE USER")

conn.commit()