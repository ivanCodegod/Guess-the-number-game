def intro():
    print(
        f'Welcome to the "Guess the number" game!!!\n\nYou have only 5 attempts to find the number\nTry to guess the '
        f'number')


def random_number(l, h):
    from random import randint
    return randint(l, h)

