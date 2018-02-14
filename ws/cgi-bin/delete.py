#! /usr/bin/python3.5
import sqlite3 as db

print("Content-type: text/html\n")
db_conn = db.connect("users.db")
query = "DELETE FROM users WHERE id=1"
cursor=db_conn.execute(query)
db_conn.commit()
print("User removed")
