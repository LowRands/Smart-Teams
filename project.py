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