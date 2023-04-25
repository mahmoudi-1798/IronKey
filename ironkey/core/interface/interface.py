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
    
    def options():
        options = ["very_strong", "strong", "medium", "weak"]
        print("Choose an option:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
        choice = input()
        choice = int(choice)
        if 1 <= choice <= len(options):
            print(f"You chose {options[choice - 1]}")
            return options[choice - 1]
        else:
            print("Invalid choice")
            return False