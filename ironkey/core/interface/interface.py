import sys
class Commands():
    
    def init(self):
        name = input("username:\n")
        while True:
            if name == None or name == "":
                print("name is required")
                name = input("username: \n")
                continue
            if name != None and name != "":
                break
        return print(name)
    
    def generate(self):
        pass
    
    def add(self):
        pass
    
    def delete(self):
        pass
    
    def backup(self):
        pass
    
    def list(self):
        pass
    
    def help(self):
        pass