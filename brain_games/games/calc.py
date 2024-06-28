
import random

GAME_RULE = 'What is the result of the expression?'


def generate_round():

    operators = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)

    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    elif operator == '*':
        correct_answer = str(num1 * num2)

    question = f"{num1} {operator} {num2}"
    return question, correct_answer
