import sqlite3
from flask import g
from os import remove 

DATABASE = 'db/db.db'

def init_db():
    # Remove and recreate file
    try:
        remove(DATABASE)
    except:
        pass
    open(DATABASE, 'w+').close()

    # Connect to DB and create cursor
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    # Create table users with field name and password
    cur.execute('CREATE TABLE users (id int primary key, name string default "", password string default "");')
    cur.execute('INSERT INTO users VALUES (0, "admin", "lkjasdlkfjzvm"), (1, "pupa", "alsdjflasdjkf"), (2, "lupa", "alsdjflasdjkf")') 

    # Commit and close the connection
    conn.commit()
    conn.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
