import sqlite3

conn = sqlite3.connect('ironkey.db')

# create a cursor
c = conn.cursor()

def create_password_table():
    c.execute(""" CREATE TABLE IF NOR EXISTS passwords (
        title text,
        password text
    )""")
    conn.commit()
    conn.close()

def create_user_table():
    c.execute(""" CREATE TABLE IF NOT EXISTS user (
        name text,
        password text
        ) """)

