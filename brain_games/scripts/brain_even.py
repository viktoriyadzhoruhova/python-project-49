import random
import prompt


def is_even(number):
    return number % 2 == 0


def main():

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_even(number) else 'no'

        if answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            correct_answers_count = 0

    print(f"Congratulations, {name}!")
