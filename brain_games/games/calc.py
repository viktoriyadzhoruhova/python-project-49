

import random

GAME_RULE = "What is the result of the expression?"


def calculate(num1, num2, operator):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():

    operators = ['+', '-', '*']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    correct_answer = str(calculate(num1, num2, operator))
    return question, correct_answer
