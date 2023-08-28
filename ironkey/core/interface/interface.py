from getpass import getpass

class Interface():
    
    # To get input from User
    # name: what we want as input from User
    # prefix: part of prompt before the name
    # suffix: part of prompt after the name
    def get_info(name, prefix='', suffix='', hide=False):
        if hide:
            result = getpass(f"{prefix} {name}: {suffix}")
        else:
           result = input(f"{prefix} {name}: {suffix}") 
        while True:
            if result == None or result == "":
                print(f"{name} is required")
                print("Do you want to cancel? Type 'exit' to abort the operation")
                result = input(f"{prefix} {name}: {suffix} \n")
                continue
            if result != None and result != "":
                break
        return result
    
    def options():
        options = ["Very Strong", "Strong", "Medium", "Weak"]
        print("Enter the number of your choice:")
        for index, option in enumerate(options):
            print(f"{index + 1}. {option}")
        choice = input()
        choice = int(choice)
        if 1 <= choice <= len(options):
            print(f"You choose {options[choice - 1]}")
            return options[choice - 1]
        else:
            print("Invalid choice")
            return False
