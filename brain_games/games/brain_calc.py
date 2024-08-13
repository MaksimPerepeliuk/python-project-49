from random import randint
from random import choice
from brain_games.scripts.engine import engine


def brain_calc():
    operations = {
        '+': lambda n1, n2: n1 + n2,
        '-': lambda n1, n2: n1 - n2,
        '*': lambda n1, n2: n1 * n2
    }
    num1 = randint(1, 30)
    num2 = randint(1, 30)
    operation = choice(list(operations.keys()))
    right_answer = str(operations[operation](num1, num2))
    question = f'{num1} {operation} {num2}'

    return question, right_answer


def main():
    task_text = 'What is the result of the expression?'
    engine(brain_calc, task_text)


if __name__ == '__main__':
    main()
