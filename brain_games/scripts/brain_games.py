from brain_games.cli import welcome_user


def main():
    welcome_user()


def ask_question(question, correct_answer):
    print(f"Question: {question}")
    user_answer = input("Your answer: ")
    
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False


if __name__ == "__main__":
    main()