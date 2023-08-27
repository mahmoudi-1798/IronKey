import sqlite3

conn = sqlite3.connect('ironkey.db')

c = conn.cursor()

class Database:

    def create_password_table():
        ''' create table named passwords to store passwords by title
        '''
        c.execute(''' CREATE TABLE IF NOT EXISTS passwords (
            title text,
            password BLOB
        )''')
        conn.commit()
    create_password_table()

    def create_user_table():
        ''' create table named user to store password of user
        '''
        c.execute(''' CREATE TABLE IF NOT EXISTS user (
            name TEXT,
            password TEXT,
            is_exist INTEGER
            ) ''')
        conn.commit()
    create_user_table()

    def add_username(self, name, password):
        c.execute('''INSERT INTO user (name, password, is_exist) VALUES (?, ?, 1)''', (name, password))
        conn.commit()
        return print("\033[92m" + "Task accomplished successfully." + "\033[0m") 
    
    def check_user_exist(self):
        c.execute('''SELECT COUNT(*) FROM user WHERE is_exist = 1''')
        result = c.fetchone()[0]
        conn.commit() 
        
        if result:
            return True
        else:
            return False

    # check if username and password is correct
    def auth_user(self, name, password):
        c.execute('''SELECT * FROM user WHERE name=?''', (name,))
        result = c.fetchone()
        
        if result and result[1] == password:
            return True
        else:
            return False

    def add_password(self, title,password):
        c.execute('''INSERT INTO passwords (title, password) VALUES (?, ?)''', (title, password))
        conn.commit()
        return print("\033[92m" + "Task accomplished successfully." + "\033[0m") # To print it in green color
    
    def check_password_exist(self,title):
        c.execute('''SELECT * FROM passwords WHERE title=?''', (title,))
        result = c.fetchone()
        if result:
            return True
        else:
            return False
    
    def list_all_passwords(self):
        c.execute('''SELECT * FROM passwords''')
        result = c.fetchall()
        return result
    
    def delete(self, title):
        c.execute('''DELETE FROM passwords WHERE title=?''', (title,))
        conn.commit()