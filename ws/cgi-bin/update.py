#! /usr/bin/python3.5
import sqlite3 as db

print("Content-type: text/html\n")

db_conn = db.connect("users.db")
cursor = db_conn.cursor()
query = "SELECT name, age FROM users WHERE id=1"
users = cursor.execute(query)
users = list(users)
print(users)
user = users[0]
print(user)
name = user[0]
print(name)
age = user[1]
print(age)

print('<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title></title><script src="//code.jquery.com/jquery-1.11.1.js"></script><script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script><script src="//cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script><style type="text/css"></style></head><body><form action="/cgi-bin/save.py"><input placeholder="Name" type="text" name="username" value="{}"><input type="text" placeholder="Age" name="age" value="{}"><input type="submit" value="Save" name="save"></form></body></html>'.format(name, age))


