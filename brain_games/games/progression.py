import random

GAME_RULE = "What number is missing in the progression?"


def generate_progression(length, start, step):

    return [start + step * i for i in range(length)]


def generate_round():

    length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    progression = generate_progression(length, start, step)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer