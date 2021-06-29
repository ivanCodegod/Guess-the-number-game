def intro():
    print(
        f'Welcome to the "Guess the number" game!!!\n\nYou have only 5 attempts to find the number\nMake a suggestion: ')


def level():
    print("Choose complexity of the game:\n\t1 - easy\n\t2 - medium\n\t3 - hardcore")
    return int(input())
