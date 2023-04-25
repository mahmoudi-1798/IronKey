from .interface import Interface as interface
from .database import database
from .generator import generator

db = database.Database()
gen = generator.Generator()
class Commands:
    
    def init(self):
        check = db.check_user_exist()
        if check:
            return print("User already exist")
        else:
            name = interface.get_info(name="username", prefix="choose a")
            if name == "ex" or name == "exit":
                return print("mission has been terminated")
            
            password = interface.get_info(name="password", prefix="choose a",hide=True)
            db.add_username(name, password)
    
    def add(self):
        title = interface.get_info(name="title", prefix="choose a", suffix="ex: github.com")
        check = db.check_password_exist(title)
        if check:
            return print("Oops this title already exist")
        else:
            password = interface.get_info(name="password", prefix="inter the")
            db.add_password(title, password)
    
    def generate(self):
        title = interface.get_info(name="title", prefix="choose a", suffix="ex: github.com")
        check = db.check_password_exist(title)
        if check:
            return print("Oops this title already exist")
        else:
            option = interface.options()
            if option:
                password = gen.generate(option)
                db.add_password(title, password)
            else:
                return
    
    def listall(self):
        result = db.list_all_passwords()
        if not result:
            return print("There is nothing here")
        else:
            return print(result)
    
    def delete(self):
        title = interface.get_info(name="title", prefix="inter specific")
        check = db.check_password_exist(title)
        if check:
            db.delete(title)
            return print("mission was successful")
        else:
            return print("it doesn't exist")