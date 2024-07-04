
import random

GAME_RULE = "What number is missing in the progression?"


def generate_progression():

    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    progression = [str(start + step * i) for i in range(length)]
    return progression


def generate_round():

    progression = generate_progression()
    missing_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    question = " ".join(progression)
    return question, correct_answer
