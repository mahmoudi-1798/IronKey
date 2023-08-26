from .interface import Interface as interface
from .database import database
from .generator import generator
from .help_text import help_text
from .auth_utils import require_authentication
from terminaltables import SingleTable
import hashlib
import os

db = database.Database()
gen = generator.Generator()

# user: test
# pass: test1234

class Commands:
    
    # Creating a User
    def init(self):
        check = db.check_user_exist()
        if check is True:
            print("User already exist")
            return 
        else:
            name = interface.get_info(name="username", prefix="Choose a")
            if name == "ex" or name == "exit":
                return print("Mission has been terminated")
            
            password = interface.get_info(name="password", prefix="Choose a",hide=True)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            db.add_username(name, hashed_password)
    
    # authentication
    def auth(self):
        m_title = interface.get_info(name="username", prefix="Enter your")
        m_pass = interface.get_info(name="password", prefix="Enter your", hide=True)
        hashed_pass = hashlib.sha256(m_pass.encode()).hexdigest()
        m_check = db.auth_user(m_title, hashed_pass) 
        if m_check == "User not found":
            print("User not found in the database.")
        return m_check

    # Adding a (title, password) to db 
    def add(self):
        title = interface.get_info(name="title",prefix="Choose a", suffix="")
        check = db.check_password_exist(title)
        if check:
            return print("\033[93m" + "Oops, title already exists." + "\033[0m") # To print it in yellow color
        else:
            password = interface.get_info(name="password", prefix="Enter the", suffix="", hide=True)
            db.add_password(title, password)
    
    # Takes a title. ask you how strong to generate, and pass (title, pass) to db
    def generate(self):
        title = interface.get_info(name="title", prefix="Choose a", suffix="")
        check = db.check_password_exist(title)
        if check:
            return print("\033[93m" + "Oops, title already exists." + "\033[0m") # To print it in yellow color
        else:
            option = interface.options() # handles showing the options and choosing an option
            if option:
                password = gen.generate(option)
                db.add_password(title, password)
            else:
                return

    # Show all records of db
    def listall(self):
        result = db.list_all_passwords()
        if not result:
            return print("\033[93m" + "There isn't any record to display." + "\033[0m") # To print it in yellow color
        else:
            headers = ["Title", "Password"]
            table = SingleTable([headers] + result)
            print("\n" + table.table)
    
    # Delete a record of db by title
    def delete(self):
        title = interface.get_info(name="title", prefix="Enter the specific")
        check = db.check_password_exist(title)
        if check:
            db.delete(title)
            return print("\033[92m" + "Task accomplished successfully." + "\033[0m") # To print it in green color
        else:
            return print("\033[93m" + "There isn't a record with this title." + "\033[0m") # To print it in yellow color
    
    # Changing the title. after asking to choose an option to genrerate. add (title, pass) to db
    # PROBLEM: it should ask User's password to authenticate.
    # TODO(COMPLETED): add an authentication
    # TODO(COMPLETED): When update a title the old one stays in db
    # TODO(COMPLETED): Ask if you want to insert your new password or generate a new for you.
    # TODO: There should be a option to change the password without changing the title
    def update(self):
        title = interface.get_info(name="title to update", prefix="Enter the")
        check = db.check_password_exist(title)
        if check is False:
            return print("\033[93m" + "Title doesn't exists." + "\033[0m") # To print it in yellow color
        else:
            new_title = interface.get_info(name="title", prefix="Enter a new")
            check_title = db.check_password_exist(new_title)
            if check_title is True:
                return print("\033[93m" + "Oops, title already exists." + "\033[0m") # To print it in yellow color
            else:
                m_choose = interface.get_info(name="a password or have one generated? \nPlease enter the number of your choice", 
                                              prefix="Do you want to manually enter",
                                              suffix="\n\n\t[1] Enter password\n\t[2] Generate\n> ")
                
                if m_choose == "1":
                    password = interface.get_info("Enter your new password", hide=True)
                    db.add_password(new_title, password)
                    db.delete(title)
                elif m_choose == "2":
                    option = interface.options()
                    if option:
                        password = gen.generate(option)
                        db.add_password(new_title, password)
                        db.delete(title)
                        return
                    else:
                        return
    
    # Show help text
    def help(self):
        return print(help_text)