from random import randint
from brain_games.scripts.engine import engine


def brain_progression():
    progression_step = randint(1, 10)
    start_num = randint(1, 30)
    progression_len = 10

    progression = list(range(start_num,
                             start_num + (progression_step * progression_len),
                             progression_step))

    hidden_index = randint(0, len(progression) - 1)
    right_answer = str(progression[hidden_index])

    progression[hidden_index] = None
    question = str(progression)[1:-1].replace('None', '..')

    return question, right_answer


def main():
    task_text = 'What number is missing in the progression?'
    engine(brain_progression, task_text)


if __name__ == '__main__':
    main()
