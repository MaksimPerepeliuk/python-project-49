from random import randint
from brain_games.scripts.engine import engine


def is_prime(num):
    if num <= 1:
        return False

    for d in range(2, num):
        if num % d == 0:
            return False

    return True


def generate_rand_odd(start, stop):
    num = randint(start, stop)
    return num + 1 if num % 2 == 0 else num


def brain_prime():
    num = generate_rand_odd(1, 1000)
    right_answer = 'yes' if is_prime(num) else 'no'
    question = str(num)
    return question, right_answer


def main():
    task_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    engine(brain_prime, task_text)


if __name__ == '__main__':
    main()
