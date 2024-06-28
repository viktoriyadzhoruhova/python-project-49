
import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate_round():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer
