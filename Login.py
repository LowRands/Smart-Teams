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
                    if login_attempts > 3:
                        print("You are locked out for 30 seconds!")
                        time.sleep(30)
                        break

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
           
    if not username.isalnum():
            print("❌ Username must be alphanumeric (letters and numbers only).")
          
        # Check for duplicates
    if username in usernames:
            print(f"⚠️ Username '{username}' already exists.")
    else:
            usernames.add(username)
            print(f"✅ Username '{username}' added successfully.")
def analyze_logins(total_attempts, failed_attempts):
    if failed_attempts == 0:
        print("No failed attempts recorded.")
        return

    ratio = total_attempts / failed_attempts
    print(f"Login attempt ratio: {ratio:.2f}")

    threshold = 3.0
    if ratio > threshold:
        print("Unusual login activity detected! Investigate further.")
        run_verification_game()
    else:
        print("Login activity within normal range.")
    # Previous Code above

def run_verification_game():
    print("\n Verification Game ")
    print("To verify you're human, answer this question: ")

    # Simple addition verification question
    question = "\nWhat is 5 + 7? "
    correct_answer = "\n12"

    user_answer = input(question)

    if user_answer.strip() == correct_answer:
        print("Verification successful. Access granted!")
    else:
        print("Verification failed. Access denied.")

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

