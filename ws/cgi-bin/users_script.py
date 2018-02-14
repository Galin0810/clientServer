#! /usr/bin/python3.5
import sqlite3 as db

print("Content-type: text/html\n")

db_conn = db.connect("users.db")
cursor = db_conn.cursor()
query = "SELECT * FROM users"
users = cursor.execute(query)
print(list(users))