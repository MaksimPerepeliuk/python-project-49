import prompt


def engine(game, task_text):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_text)

    right_answer_count = 0

    while right_answer_count < 3:
        question, right_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print((f"'{user_answer}' is wrong answer ;(. "
                   f"Correct answer was '{right_answer}'"))
            print(f"Let's try again, {user_name}!")
            return
        else:
            right_answer_count += 1
            print('Correct!')

    print(f'Congratulations, {user_name}!')
