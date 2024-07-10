import random

GAME_RULE = "What number is missing in the progression?"


def generate_progression(start, step, length, missing_index):

    progression = [str(start + step * i) for i in range(length)]
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    question = " ".join(progression)
    return question, correct_answer


def generate_round():

    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    missing_index = random.randint(0, length - 1)
    question, correct_answer = generate_progression(start, step, length, missing_index)
    return question, correct_answer
