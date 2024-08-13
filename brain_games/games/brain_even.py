from random import randint
from brain_games.scripts.engine import engine


def is_even(num):
    return num % 2 == 0


def brain_even():
    num = randint(1, 30)
    right_answer = 'yes' if is_even(num) else 'no'
    return num, right_answer


def main():
    task_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(brain_even, task_text)


if __name__ == '__main__':
    main()
