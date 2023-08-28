from .interface import Interface as interface
from .database import database
from .generator import generator
from .help_text import help_text
from .auth_utils import require_authentication
from terminaltables import SingleTable
from .crypto.main import EncryptionManager
import hashlib
import base64
import time
import os

db = database.Database()
gen = generator.Generator()

manager = EncryptionManager()

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

        # Make the key for the password encryption     
        key = manager.generate_derived_key(m_title, b"IronKey")
        manager.initialize_encryptor(key)

        return m_check

    # Adding a (title, password) to db 
    def add(self):
        title = interface.get_info(name="title",prefix="Choose a", suffix="")
        check = db.check_password_exist(title)
        if check:
            return print("\033[93m" + "Oops, title already exists." + "\033[0m") # To print it in yellow color
        else:
            password = interface.get_info(name="password", prefix="Enter the", suffix="", hide=True)
            encrypted_password = manager.encrypt_data(password)
            db.add_password(title, encrypted_password)
    
    # Takes a title. ask you how strong to generate, and pass (title, pass) to db
    def generate(self):
        title = interface.get_info(name="title", prefix="Choose a", suffix="")
        check = db.check_password_exist(title)
        if check:
            user_ask = input("\033[93m" + "Oops, title already exists.Do you want to overwrite it? (y/n): " + "\033[0m") # To print it in yellow color
            
            if user_ask == "y" or user_ask == "Y":
                option = interface.options()
                if option:
                    password = gen.generate(option)
                    db.delete(title)
                    encrypted_new_password = manager.encrypt_data(password)
                    db.add_password(title, encrypted_new_password)
                    return
                else:
                    return
            
            elif user_ask == "n" or user_ask == "N":
                print("Redirecting to main menu.")
                return
            
            else:
                return print("\033[93m" + "Invalid Input." + "\033[0m")
        else:
            option = interface.options() # handles showing the options and choosing an option
            if option:
                password = gen.generate(option)
                encrypted_new_password = manager.encrypt_data(password)
                db.add_password(title, encrypted_new_password)
            else:
                return

    # Show all records of db
    def listall(self):
        result = db.list_all_passwords()
        if not result:
            return print("\033[93m" + "There isn't any record to display." + "\033[0m") # To print it in yellow color
        else:
            headers = ["Title", "Password"]
            new_result = []  # Create a new list to hold modified data
            
            # Decrypt every record to show
            for record in result:
                title, encrypted_password = record
                decrypted_password = manager.decrypt_data(encrypted_password)
                new_record = [title, decrypted_password]  # Create a new list with modified data
                new_result.append(new_record) 

            table = SingleTable([headers] + new_result)
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
    def update(self):
        title = interface.get_info(name="title to update", prefix="Enter the")
        check = db.check_password_exist(title)
        if check is False:
            return print("\033[93m" + "Title doesn't exists." + "\033[0m") # To print it in yellow color
        else:
            new_title = interface.get_info(name="title", prefix="Enter a new")
            check_title = db.check_password_exist(new_title)
            
            if check_title is True:
                user_ask = input("\033[93m" + "Oops, title already exists.Do you want to overwrite it? (y/n): " + "\033[0m") # To print it in yellow color
            
                if user_ask == "y" or user_ask == "Y":
                    m_choose = interface.get_info(name="a password or have one generated? \nPlease enter the number of your choice", 
                            prefix="Do you want to manually enter",
                            suffix="\n\n\t[1] Enter password\n\t[2] Generate\n> ")
                    
                    if m_choose == "1":
                        password = interface.get_info("Enter your new password", hide=True)
                        db.delete(title)
                        encrypted_new_password = manager.encrypt_data(password)
                        db.add_password(new_title, encrypted_new_password)

                    elif m_choose == "2":
                        option = interface.options()
                        if option:
                            password = gen.generate(option)
                            db.delete(title)
                            encrypted_new_password = manager.encrypt_data(password)
                            db.add_password(new_title, encrypted_new_password)
                            return
                        else:
                            return
                
                elif user_ask == "n" or user_ask == "N":
                    print("Redirecting to main menu.")
                    return
                
                else:
                    return print("\033[93m" + "Invalid Input." + "\033[0m")
            
            else:
                m_choose = interface.get_info(name="a password or have one generated? \nPlease enter the number of your choice", 
                                              prefix="Do you want to manually enter",
                                              suffix="\n\n\t[1] Enter password\n\t[2] Generate\n> ")
                
                if m_choose == "1":
                    password = interface.get_info("Enter your new password", hide=True)
                    encrypted_new_password = manager.encrypt_data(password)
                    db.add_password(new_title, encrypted_new_password)
                    db.delete(title)
                elif m_choose == "2":
                    option = interface.options()
                    if option:
                        password = gen.generate(option)
                        encrypted_new_password = manager.encrypt_data(password)
                        db.add_password(new_title, encrypted_new_password)
                        db.delete(title)
                        return
                    else:
                        return
    
    # To Delete Account
    def delete_account(self):
        danger_phrase = input("\033[1m\033[31m" + "Are you sure you want to delete account and clear the database? \nThis action cannot be undone. Type 'CONFIRM' to proceed: " + "\033[0m")
        if danger_phrase == "CONFIRM":
            db.clear()
            print("\033[1m\033[31m" + "DELETING ACCOUNT AND CLEANING PASSWORDS..." + "\033[0m")
            for i in range(0, 3):
                time.sleep(1)
                print(".")
            time.sleep(1)
            return print("\033[92mDatabase tables cleared successfully.\033[0m")
            
        else:
            return print("\033[93m" + "Process has been cancelled." + "\033[0m")

    # Show help text
    def help(self):
        return print(help_text)