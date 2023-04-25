from getpass import getpass
class Interface():
    
    def get_info(self, param, hide=False):
        
        if hide:
            result = getpass(f"{param}: \n")
        else:
           result = input(f"{param}: \n") 
        while True:
            if result == None or result == "":
                print(f"{param} is required")
                print("do you wana cancel? type exit")
                result = input(f"{param}: \n")
                continue
            if result != None and result != "":
                break
        return result
    
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