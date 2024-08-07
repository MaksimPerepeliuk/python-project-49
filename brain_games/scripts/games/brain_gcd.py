from random import randint
from brain_games.scripts.engine import engine


def gcd(num1, num2):
    less_num = num1 if num1 < num2 else num2
    more_num = num1 if num1 > num2 else num2

    if more_num % less_num == 0:
        return less_num

    for n in range(less_num//2, 0, -1):
        if less_num % n == 0:
            if more_num % n == 0:
                return n


def brain_gcd():
    num1 = randint(1, 30)
    num2 = randint(1, 30)

    question = f'{num1} {num2}'
    right_anwer = str(gcd(num1, num2))

    return question, right_anwer


def main():
    engine(brain_gcd)


if __name__ == '__main__':
    main()
