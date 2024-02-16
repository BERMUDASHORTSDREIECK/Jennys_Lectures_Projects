# a password generator
# tried various methods for string generation and randomization
# naming schemes and spacing is off at times


import random
import secrets
import string


final_string = ''

def iterator(final_string, letter_whatever_count, symbols_whatever):
    for i in range(letter_whatever_count):
        final_string += final_string.join(symbols_whatever[random.randint(0, len(symbols_whatever)-1)])
    print(final_string)
    return final_string


def main():
    final_string = ''

    print('welcome padawan')
    letter_count = int(input('insert letter count '))
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    final_string = iterator(final_string, letter_count, letters)


    symbol_count = int(input('insert symbols count '))
    symbols = list("~`!@#$%^&*()_-+={[}]|'\':;\"<,>.?/")
    final_string = iterator(final_string, symbol_count, symbols)


    number_count = int(input('insert numbers count '))
    final_string += ''.join(secrets.choice(string.digits) for i in range(number_count))
    print(final_string)
    return final_string


def randomize_string(string):
    randomized_string = ''
    list_1 = list(string)
    while len(randomized_string) < len(list_1):
        j = list_1[random.randint(0, len(string)-1)]
        if j not in randomized_string:
            randomized_string += j
    print(randomized_string)


randomize_string(main())