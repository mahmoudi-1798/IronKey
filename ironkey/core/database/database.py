import sqlite3

conn = sqlite3.connect('ironkey.db')

# create a cursor
c = conn.cursor()

def create_password_table():
    ''' create table named passwords to store passwords by title
    '''
    c.execute(""" CREATE TABLE IF NOT EXISTS passwords (
        title text,
        password text
    )""")
    conn.commit()

create_password_table()

def create_user_table():
    ''' create table named user to store user password of user
    '''
    c.execute(""" CREATE TABLE IF NOT EXISTS user (
        name text,
        password text
        ) """)
    conn.commit()

create_user_table()

def user_init():
    return




