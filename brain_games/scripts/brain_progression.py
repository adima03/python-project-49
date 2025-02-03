import random

from brain_games.scripts import brain_games


def generate_progression(length=10, start=1, step=2):
    return [start + step * i for i in range(length)]


def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_value


def progression_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    for _ in range(3):
        length = random.randint(5, 10)  
        progression = generate_progression(length)
        hidden_value = hide_element(progression)
        print("What number is missing in the progression?")
        question = f'{' '.join(map(str, progression))}'

        correct_answer = str(hidden_value) 

        if not brain_games.ask_question(question, correct_answer):
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main():
    progression_game()


if __name__ == "__main__":
    main()
