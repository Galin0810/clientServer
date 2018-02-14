#! /usr/bin/python3.5
import cgi
import sqlite3 as db

form = cgi.FieldStorage()
name = form.getfirst("username", "default")
age = form.getfirst("age", -1)

print("Content-type: text/html\n")
print(name + ", " + str(age))

db_conn = db.connect("users.db")
query = "CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement, name text, age integer)"
cursor=db_conn.execute(query)

insert = "INSERT INTO users(name, age) values(?, ?)"
cursor = db_conn.cursor()
cursor.execute(insert, (name, age))
db_conn.commit()