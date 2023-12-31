from ironkey import Commands
from ironkey.core.help_text import header_text
import time
import sys
import os

def header(text):
    os.system("clear")
    print(text)
    
if __name__ == "__main__":
    ironkey = Commands()

    if len(sys.argv) == 2 and sys.argv[1] == 'init':
        ironkey.init()
        time.sleep(3)
        running = False
    elif ironkey.auth():
        running = True
    else:
        running = False
        print("\033[91m" + "Authentication failed. Incorrect username or password." + "\033[0m")

    while (running):
        header(header_text)
        choose = input("IronKey> ")

        if choose == "add":
            ironkey.add()
            time.sleep(3)
        elif choose == "generate":
            ironkey.generate()
            time.sleep(3)
        elif choose == "delete":
            ironkey.delete()
            time.sleep(3)
        elif choose == "listall":
            ironkey.listall()
            input("\nPress Enter to continue...\n\n")
        elif choose == "update":
            ironkey.update()
            time.sleep(3)
        elif choose == "about":
            ironkey.help()
            input("\nPress Enter to continue...\n\n")
        elif choose == "purge":
            if ironkey.auth():
                ironkey.delete_account()
            else:
                print("\033[91m" + "Authentication failed. Incorrect username or password." + "\033[0m")
            
            input("Press Enter to exit.\n")
            running = False
        elif choose == "backup":
            ironkey.back_up()
            time.sleep(3)
        elif choose == "exit":
            os.system("clear")
            running = False
        else:
            print("\033[93m" + "Invalid command. Please enter a valid command." + "\033[0m") 
            time.sleep(3)