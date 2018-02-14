#! /usr/bin/python3.5
import cgi
import sqlite3 as db

form = cgi.FieldStorage()
name = form.getfirst("username", "default")
age = form.getfirst("age", -1)

print("Content-type: text/html\n")
print("name: " + name + ",  " + age)
db_conn = db.connect("users.db")
query = "UPDATE users SET name=?, age=? WHERE id=1"
cursor=db_conn.execute(query, (name, age))
print("Query is executed")
db_conn.commit()

print("Saved")