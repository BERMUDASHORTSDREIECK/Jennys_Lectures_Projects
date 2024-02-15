# ideas:
# safer random generator and mimic apple password generator format

import random

final_string = ''
print('welcome padawan')
letter_count = int(input('insert letter count '))
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(letter_count):
    final_string += letters[random.randint(0, len(letters)-1)]
print(final_string)

symbol_count = int(input('insert symbols count '))
symbols = list("~`!@#$%^&*()_-+={[}]|'\':;\"<,>.?/")
for i in range(symbol_count):
    final_string += symbols[random.randint(0, len(symbols)-1)]
print(final_string)

number_count = int(input('insert numbers count '))
for i in range(number_count):
    final_string += str(random.randint(0, 9))
print(final_string)


def randomize_string(string):
    randomized_string = ''
    list_1 = list(string)
    while len(randomized_string) < len(list_1):
        j = list_1[random.randint(0, len(string)-1)]
        if j not in randomized_string:
            randomized_string += j
    print(randomized_string)


randomize_string(final_string)