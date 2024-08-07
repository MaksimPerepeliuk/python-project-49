from random import randint
from brain_games.scripts.engine import engine


def is_even(num):
    return num % 2 == 0


def brain_even():
    num = randint(1, 30)
    right_answer = 'yes' if is_even(num) else 'no'
    return num, right_answer


def main():
    engine(brain_even)


if __name__ == '__main__':
    main()
