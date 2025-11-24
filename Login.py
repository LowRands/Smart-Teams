import os
import time 


def add_usernames():
    usernames = set()  # Using a set to avoid duplicates automatically

    print("=== Username Registration System ===")
    print("Type 'exit' to stop adding usernames.\n")

    while True:
        username = input("Enter a new username: ").strip()

        # Exit condition
        if username.lower() == "exit":
            login_attempts = 0

            while login_attempts < 3:
                    time.sleep(0.5)
                    os.system('cls')

                    username = input ("Enter Your Username: ")
                    login_attempts += 1

                    if username in add_usernames:
                        print(f"Welcome, {username}!")
                        print("You are in")
                        login_attempts = 0
                        break
                    else:
                        print("Invalid Username, Try Again")
            break

        # Validation: non-empty and alphanumeric
        if not username:
            print("❌ Username cannot be empty.")
            continue
        if not username.isalnum():
            print("❌ Username must be alphanumeric (letters and numbers only).")
            continue
        # Check for duplicates
        if username in usernames:
            print(f"⚠️ Username '{username}' already exists.")
        else:
            usernames.add(username)
            print(f"✅ Username '{username}' added successfully.")
    # Display all usernames
    #print("\n=== Registered Usernames ===")
    #if usernames:
       # for user in sorted(usernames):
      #      print(f"- {user}")
   # else:
      #Er  print("No usernames were added.")

if __name__ == "__main__":
    try:
        add_usernames()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
os.system('cls')
def add_Passwords():
    password = set()

    print("=== Password Registration System ===")
    print("Type 'exit' to stop adding passwords.\n")

    while True:
        password = input("Enter a new Password: ").strip()

        # Exit condition
        if password.lower() == "exit":
            login_attempts = 0

            while login_attempts < 3:
                    time.sleep(0.5)
                    os.system('cls')

                    password = input ("Enter Your Password: ")
                    login_attempts += 1

                    if password in add_Passwords:
                        print("You are in")
                        login_attempts = 0
                        break
                    else:
                        print("Invalid Username, Try Again")
            break

        # Validation: non-empty and alphanumeric
        if not password:
            print("❌ Username cannot be empty.")
            continue
        if not password.isalnum():
            print("❌ Username must be alphanumeric (letters and numbers only).")
            continue
    # Display all usernames
    #print("\n=== Registered Usernames ===")
    #if usernames:
       # for user in sorted(usernames):
      #      print(f"- {user}")
   # else:
      #Er  print("No usernames were added.")

if __name__ == "__main__":
    try:
        add_usernames()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

