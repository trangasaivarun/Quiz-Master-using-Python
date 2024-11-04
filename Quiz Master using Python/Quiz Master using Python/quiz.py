import json
import random
import matplotlib.pyplot as plt
import os

user = []
initial_menu = True

def load_questions(difficulty):
    try:
        with open("assets/questions.json", 'r') as f:
            questions = json.load(f)
            return [q for q in questions if q["difficulty"] == difficulty]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading questions:", e)
        return []

def load_users():
    if not os.path.exists('assets/user_accounts.json'):
        return {}
    with open('assets/user_accounts.json', 'r') as user_accounts:
        return json.load(user_accounts)

def save_users(users):
    with open('assets/user_accounts.json', 'w') as user_accounts:
        json.dump(users, user_accounts, indent=4)

def play():
    if len(user) == 0:
        print("Please log in first to play the quiz.")
        return

    mode = input("Choose game mode (single player or vs Computer): ").lower()
    if mode == "vs computer":
        play_with_ai()
    else:
        single_player_quiz()

def play_with_ai():
    print("\n========== PLAYING VS COMPUTER ==========")
    user_score, computer_score = run_quiz(is_computer=True)

    print(f"\nYour Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You beat the Computer!")
    elif user_score < computer_score:
        print("The Computer wins this time. Better luck next time!")
    else:
        print("It's a tie!")

    update_progress(user[0], user_score)

def single_player_quiz():
    print(f"\n========== SINGLE PLAYER QUIZ START ========== ")
    score, _ = run_quiz()
    update_progress(user[0], score)

def run_quiz(is_computer=False):
    user_score = 0
    computer_score = 0
    difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
    questions = load_questions(difficulty)

    if not questions:
        print("No questions available for this difficulty level.")
        return user_score, computer_score

    for i in range(10):
        if not questions:
            print("No more questions available in this difficulty level.")
            break

        question = random.choice(questions)
        questions.remove(question)

        print(f'\nQ{i + 1}: {question["question"]}\n')
        for option in question["options"]:
            print(option)

        # User's answer
        answer = input("\nEnter your answer (A, B, C, D): ").strip().upper()
        if question["answer"][0].upper() == answer:
            print("Correct!")
            user_score += 1
        else:
            print(f"Incorrect. The correct answer was: {question['answer'][0]}")

        # Computer's answer (random choice)
        if is_computer:
            computer_answer = random.choice(['A', 'B', 'C', 'D'])
            print(f"Computer's answer: {computer_answer}")
            if question["answer"][0].upper() == computer_answer:
                computer_score += 1

    print(f'\n========== FINAL SCORE: {user_score} ==========\n')
    return user_score, computer_score

def update_progress(username, score):
    users = load_users()

    users[username]["total_score"] += score
    users[username]["quizzes_taken"] += 1

    if "history" not in users[username]:
        users[username]["history"] = []
    users[username]["history"].append(score)

    save_users(users)

    user[1] = users[username]["total_score"]
    user[2] = users[username]["quizzes_taken"]

def createAccount():
    print("\n========== CREATE ACCOUNT ========== ")
    username = input("Enter your USERNAME: ")
    password = input('Enter your PASSWORD (will be visible): ')

    users = load_users()

    if username in users:
        print("An account with this username already exists. Please log in instead.")
    else:
        users[username] = {
            "password": password,
            "total_score": 0,
            "quizzes_taken": 0,
            "history": []
        }
        save_users(users)
        print("Account created successfully!")

def loginAccount():
    print('\n========== LOGIN PANEL ========== ')
    username = input("USERNAME: ")
    password = input('PASSWORD: ')

    users = load_users()

    if username not in users:
        print("An account with that name doesn't exist. Please create an account first.")
    elif users[username]["password"] != password:
        print("Incorrect password. Please try again.")
    else:
        print("You have successfully logged in.\n")
        user.clear()
        user.append(username)
        user.append(users[username]["total_score"])
        user.append(users[username]["quizzes_taken"])
        global initial_menu
        initial_menu = False

def logout():
    global user
    if len(user) == 0:
        print("You are already logged out.")
    else:
        user.clear()
        print("You have been logged out successfully.")
        global initial_menu
        initial_menu = True

def deleteAccount():
    if len(user) == 0:
        print("Please log in first to delete your account.")
        return

    confirmation = input(f"Are you sure you want to delete your account, {user[0]}? This action cannot be undone. (yes/no): ").lower()

    if confirmation == 'yes':
        users = load_users()
        if user[0] in users:
            del users[user[0]]
            save_users(users)
            print("Your account has been deleted successfully.")
            user.clear()
            global initial_menu
            initial_menu = True
    else:
        print("Account deletion canceled.")

def view_progress():
    if len(user) == 0:
        print("Please log in first to view your progress.")
        return

    users = load_users()

    print(f"\n========== YOUR PROGRESS ========== ")
    print(f"Hi {user[0]}, your total score is {users[user[0]]['total_score']} and you've taken {users[user[0]]['quizzes_taken']} quizzes.")

    score_history = users[user[0]].get("history", [])

    if score_history:
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(score_history) + 1), score_history, marker='o', color='b', linestyle='-', linewidth=2)
        plt.title(f"{user[0]}'s Score History")
        plt.xlabel("Quizzes Taken")
        plt.ylabel("Scores")
        plt.xticks(range(1, len(score_history) + 1))
        plt.grid()
        plt.show()

    # Additional options after viewing progress
    while True:
        print("\n========== VIEW PROGRESS MENU ==========")
        print("1. Return to User Menu")
        print("2. Play a Quiz")
        print("3. Logout")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            break  # Exit to main menu
        elif choice == '2':
            play()
            break
        elif choice == '3':
            logout()
            break
        else:
            print("Invalid choice, please try again.")

# Main Menu Loop
while True:
    if initial_menu:
        print("\n========== MAIN MENU ==========")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            createAccount()
        elif choice == '2':
            loginAccount()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")
    else:
        print("\n========== USER MENU ==========")
        print("1. Play")
        print("2. View Progress")
        print("3. Logout")
        print("4. Delete Account")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            play()
        elif choice == '2':
            view_progress()
        elif choice == '3':
            logout()
        elif choice == '4':
            deleteAccount()
        elif choice == '5':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please try again.")
