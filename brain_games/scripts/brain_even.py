import random

from brain_games.scripts import brain_games


def even_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)
        correct_answer = "yes" if number % 2 == 0 else "no"
        if not brain_games.ask_question(number, correct_answer):
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    even_game()


if __name__ == "__main__":
    main()