from .interface import Interface as interface
from .database import database

db = database.Database()

class Commands:
    
    def init(self):
        check = db.check_user_exist()
        if check:
            print("User already exist")
        else:
            name = interface.get_info(self, "username")
            if name == "ex" or name == "exit":
                return print("mission has been terminated")
            
            password = interface.get_info(self, "password", hide=True)
            db.add_username(name, password)