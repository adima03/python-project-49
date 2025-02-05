import random

from brain_games.scripts import brain_games


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):  
        number = random.randint(1, 100)
        question = f'{number}'
        correct_answer = "yes" if is_prime(number) else "no"
        
        if not brain_games.ask_question(question, correct_answer):
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    prime_game()


if __name__ == "__main__":
    main()
