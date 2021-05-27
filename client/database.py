import os
import sqlite3

dir = os.path.dirname(__file__)

def create_table():
    conn = sqlite3.connect(os.path.join(dir, "data", "sqlite3.db"))
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS neos (id INTEGER PRIMARY KEY, name TEXT, jpl_url TEXT, is_hazardous INTEGER, next_approach TEXT)"
    )
    conn.commit()
    conn.close()

def insert(id, name, jpl_url, is_hazardous, next_approach):
    conn = sqlite3.connect(os.path.join(dir, "data", "sqlite3.db"))
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO neos VALUES(?,?,?,?,?)",
        (id, name, jpl_url, is_hazardous, next_approach),
    )
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect(os.path.join(dir, "data", "sqlite3.db"))
    cur = conn.cursor()
    cur.execute("SELECT * FROM neos")
    rows = cur.fetchall()
    conn.close()
    return rows