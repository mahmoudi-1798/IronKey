from getpass import getpass
class Interface():
    
    def get_info(name, prefix='', suffix='', hide=False):
        
        if hide:
            result = getpass(f"{prefix}{name}: {suffix} \n")
        else:
           result = input(f"{prefix} {name}: {suffix} \n") 
        while True:
            if result == None or result == "":
                print(f"{name} is required")
                print("do you wanna cancel? type exit")
                result = input(f"{prefix} {name}: {suffix} \n")
                continue
            if result != None and result != "":
                break
        return result