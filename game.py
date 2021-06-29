from text import *

intro()  # How to play
low, high = None, None  # tmp values
attempt = 5  # Default value

level = int(input(" Choose complexity of the game:\n\t1 - easy\n\t2 - medium\n\t3 - hardcore\n"))
print(f'You chose the <<{level}>> level of complexity, GOOD LUCK')

if level == 1: low, high = 1, 10
elif level == 2: low, high, attempt = 1, 50, 4
elif level == 3: low, high = 1, 1000

print(f'Try to guess the number between <<{low}>> and <<{high}>>\n You have only {attempt} attempt')
hide_number = random_number(low, high)
number = int(input())

while number != hide_number and attempt:
    if number > hide_number:
        number = int(input('Number is too high, try again: '))
        attempt -= 1
        if attempt:
            print(f'You have {attempt} more attempt')

    elif number < hide_number:
        number = int(input('Number is too low, try again: '))
        attempt -= 1
        if attempt:
            print(f'You have {attempt} more attempt')

print(f'You guess the number, good job!!!' if attempt else f'You lose')
