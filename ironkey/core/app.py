from .interface import Interface as interface
from .database import database
from .generator import generator
from .help_text import text
from .auth_utils import require_authentication
import os

db = database.Database()
gen = generator.Generator()

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
            db.add_username(name, password)
    
    # authentication
    def auth(self):
        m_title = interface.get_info(name="username", prefix="Enter your")
        m_pass = interface.get_info(name="password", prefix="Enter your", hide=True)

        m_check = db.auth_user(m_title, m_pass) 
        return m_check

    # Adding a (title, password) to db 
    @require_authentication
    def add(self):
        title = interface.get_info(name="title",prefix="Choose a", suffix="ex: github.com")
        check = db.check_password_exist(title)
        if check:
            return print("Oops, title already exists.")
        else:
            password = interface.get_info(name="password", prefix="Enter the ", hide=True)
            db.add_password(title, password)
    
    # Takes a title. ask you how strong to generate, and pass (title, pass) to db
    @require_authentication
    def generate(self):
        title = interface.get_info(name="title", prefix="Choose a", suffix="ex: github.com")
        check = db.check_password_exist(title)
        if check:
            return print("Oops, title already exists.")
        else:
            option = interface.options() # handles showing the options and choosing an option
            if option:
                password = gen.generate(option)
                db.add_password(title, password)
            else:
                return

    # Show all records of db
    # TODO: Create a beutiful list of passwords 
    @require_authentication
    def listall(self):
        result = db.list_all_passwords()
        if not result:
            return print("No data to display.")
        else:
            return print(result)
    
    # Delete a record of db by title
    @require_authentication
    def delete(self):
        title = interface.get_info(name="title", prefix="Enter the specific")
        check = db.check_password_exist(title)
        if check:
            db.delete(title)
            return print("Task accomplished successfully.")
        else:
            return print("It doesn't exist")
    
    # Changing the title. after asking to choose an option to genrerate. add (title, pass) to db
    # PROBLEM: it should ask User's password to authenticate.
    # TODO(COMPLETED): add an authentication
    # TODO(COMPLETED): When update a title the old one stays in db
    # TODO: Ask if you want to insert your new password or generate a new for you.
    # TODO: There should be a option to change the password without changing the title
    @require_authentication
    def update(self):
        title = interface.get_info(name="title to update", prefix="Enter the")
        check = db.check_password_exist(title)
        if check is False:
            return print("This title doesn't exist")
        else:
            new_title = interface.get_info(name="title", prefix="Enter a new")
            check_title = db.check_password_exist(new_title)
            if check_title is True:
                return print("This title already exist")
            else:
                m_choose = interface.get_info(name="a password or have one generated?", 
                                              prefix="Do you want to manually enter",
                                              suffix="\n[1] Enter password\n[2] Generate")
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
        return print(text)