# Quiz-Master-using-Python

This is a console-based quiz game that allows users to test their knowledge by answering multiple-choice questions. Users can play in single-player mode or compete against a computer opponent. The game supports multiple difficulty levels, and users can track their progress, view their quiz history, and manage their accounts.

## Features
- **Single Player Mode**: Play the quiz solo with multiple-choice questions.
- **Versus Computer Mode**: Compete against a computer that answers randomly.
- **Difficulty Levels**: Choose from easy, medium, or hard questions.
- **Account Management**: Create, log in, and delete user accounts.
- **Progress Tracking**: View your quiz history and scores in a graph format.

## Project Structure
- `assets/questions.json`: JSON file storing quiz questions and answers by difficulty level.
- `assets/user_accounts.json`: JSON file for saving user account information and scores.
- `quiz.py`: The main game script that includes the quiz logic and user management.

## Requirements
- Python 3.x
- `matplotlib` for plotting user progress (install with `pip install matplotlib`)

## Setup and Installation
1. Clone the repository or download the source code.
2. Ensure `questions.json` and `user_accounts.json` files are in the `assets` folder.
3. Install required libraries:
   ```bash
   pip install matplotlib
   ```
4. Run the main script:
   ```bash
   python main.py
   ```

## Usage
1. Run the program to access the main menu.
2. **Create an Account**: Enter a unique username and password.
3. **Login**: Access your account by entering your username and password.
4. **Play Quiz**: Choose between single-player mode or versus computer mode.
5. **View Progress**: View your total score, quizzes taken, and score history in a graphical format.
6. **Logout**: Log out of the account.
7. **Delete Account**: Permanently delete your account and data.

## JSON Data Format
### Questions File (`questions.json`)
```json
[
    {
        "question": "Sample question?",
        "options": ["A) Option1", "B) Option2", "C) Option3", "D) Option4"],
        "answer": "A",
        "difficulty": "easy"
    },
    ...
]
```
- **question**: The quiz question.
- **options**: List of four options.
- **answer**: Correct answer (e.g., "A").
- **difficulty**: Difficulty level (e.g., "easy", "medium", "hard").

### User Accounts File (`user_accounts.json`)
This file stores user data, including their total score and quiz history.

Happy Quizzing!
