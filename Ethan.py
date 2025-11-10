import os
import time 
allowed_usernames = ["Ethan", "Franklin", "Daniel", "Sami", "Rio"]

login_attempts = 0
def scan_username():
    global login_attempts

while login_attempts < 3:
    time.sleep(0.5)
    os.system('cls')

    username = input ("Enter Your Username: ")
    login_attempts += 1

    if username in allowed_usernames:
        print(f"Welcome, {username}!")
        print("You are in")
        login_attempts = 0
        break

    else:
        print("Invalid Username, Try Again")       
        uiwhfuiwhfiuwefuiheefgwefjqfgoshvuhhwqifuwefgqchwegferugwd