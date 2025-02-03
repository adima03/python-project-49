import math
import random

from brain_games.scripts import brain_games


def gcd_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        question = f'{num1},{num2}'
        
        correct = math.gcd(num1, num2)
        correct_answer = str(correct)
        if not brain_games.ask_question(question, correct_answer):
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    gcd_game()


if __name__ == "__main__":
    main()
