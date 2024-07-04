

import random

GAME_RULE = "What is the result of the expression?"


def calculate(a, b, operator):

    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def generate_round():

    operators = ['+', '-', '*']
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(operators)
    question = f"{a} {operator} {b}"
    correct_answer = str(calculate(a, b, operator))
    return question, correct_answer
