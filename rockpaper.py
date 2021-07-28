"""

"""
import random

ROCK = "камень"
SCISSOR = "ножницы"
PAPER = "бумага"

choices = [ROCK, SCISSOR, PAPER]

def message():
    print("choice: \n"
          "\t1-камень \n"
          "\t2-ножницы\n"
          "\t3-бумага")

def get_result(man, ai):
    if man == ai:
        return "Ничья"
    rule = {ROCK:SCISSOR, SCISSOR:PAPER, PAPER:ROCK}

    if rule[man] == ai:
        return "WIN"
    else:
        return "LOSE"


if __name__ == '__main__':
    is_run = 1
    while is_run != 0:
        message()
        choice = input()
        man = choices[int(choice) - 1]
        ai = random.choice(choices)
        print(f'you:{man.upper()} \t ai:{ai}')
        result = get_result(man, ai)
        print(result)
        is_run = int(input('0 - close, 1 - continue'))
