from random import randint
from text import intro, level

intro()

min, max = 1, 10
hide_number = randint(min, max)

number = int(input())

while number != hide_number:
    if number > hide_number:
        number = int(input('Number is too high, try again: '))
    elif number < hide_number:
        number = int(input('Number is too low, try again: '))
print("You guess the number, good job!!!")
