from random import randint
import prompt


def is_even(num):
    return num % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    right_answer_count = 0

    while right_answer_count < 3:
        num = randint(1, 30)
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')
        right_answer = 'yes' if is_even(num) else 'no'

        if user_answer != right_answer:
            print((f"'{user_answer}' is wrong answer ;(. "
                   f"Correct answer was '{right_answer}'"))
            print(f"Let's try again, {user_name}!")
            return
        else:
            right_answer_count += 1
            print('Correct!')

    print(f'Congratulations, {user_name}')


if __name__ == '__main__':
    main()
