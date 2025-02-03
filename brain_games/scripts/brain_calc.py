import random

from brain_games.scripts import brain_games


def calc_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    operations = ['+', '-', '*']
    
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(operations)
        question = f"{num1} {operation} {num2}"
        
        if operation == '+':
            correct_answer = str(num1 + num2)
        elif operation == '-':
            correct_answer = str(num1 - num2)
        else:  # operation == '*'
            correct_answer = str(num1 * num2)

        if not brain_games.ask_question(question, correct_answer):
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    calc_game()


if __name__ == "__main__":
    main()