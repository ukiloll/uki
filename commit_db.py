import sqlite3

conn = sqlite3.connect("connect database")

def select(table:str ,**args)->any:
    if args != None:
        #handle args and exe
        pass
    return conn.execute(f"SELECT * FROM ${table}")

def end():
    conn.commit()
    conn.close()