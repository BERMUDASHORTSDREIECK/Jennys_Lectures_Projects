# print("ctr R for run cm6 issues, \num1 for left hand tree tree")
# print(" backslash exempts double quotes etc. so you can:")
# print("e.g. " + "print" + "(\"Hello + Jannik\")")
# a = input("\"test here: ")
# print("hey " + input("what is your name?") + " how are you")
# a = "test name"
# b = len(a)
# c = 123
# print(str(b) + ' ' + str(c))
# print(int(b + c))
# floor division
# print(type(2 // 2))
"""
def most_frequent_item_count(collection):
    if not collection:
        return 0
    else:
        c = 0
        for i in collection:
            b = i
            print(collection.index(i))
            print(collection[collection.index(i) + 1])
            if collection[collection.index(i)+1] == b:
                c += 1
                print(c)
            else:
                i += 1


most_frequent_item_count([3, -1, -1])


['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
"""
import random

"""
def pig_latin(s):
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if s[0] in vowels:
        s += "way"
        return s
    else:
        s += s[0]
        s = s.replace(s[0], '', 1)
        s += "ay"
        return s



print(pig_latin("Ggiggg"))
"""

"""
def num_check():
    number = int(input("input number: "))
    if number == 1:
        no = "one"
    elif number == 2:
        no = "two"
    elif number == 3:
        no = "three"
    else:
        no = "four"
    print(f" your no is: {no}.")


num_check()

"""

# num.remove(0)
# num.pop() remove last elmt or feed index
# num.extend([]) add more than 1 value

# import random
"""
# randint, randrange, random, uniform hadntails k
listing = input("names here: ").replace(', ', '\n').splitlines()
listing_1 = input("name her: ").split(',')
print(listing_1)
print(random.choice(listing))
random_val = random.randint(0, len(listing)-1) 
if random_val < 1:
    payee = listing[0]
elif 1 < random_val < 2:
    payee = listing[1]
else:
    payee = listing[2]
print(payee)
heredas as, ds,ds
['das', 'as,', 'ds,ds']
.split(',')
"""


n = 38458215


'''def max_rot(n):  
    n = str(n)
    list_1 = [n]
    for i in range(len(n)-2):
        n += n[i]
        n.replace(n[i], '', 1)
        print(n)
        list_1.append(n)
        print(max(list_1))


max_rot(n)

'''

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
    j = ''
    list_1 = list(string)
    while len(randomized_string) < len(list_1):
        j = list_1[random.randint(0, len(string)-1)]
        if j not in randomized_string:
            randomized_string += j
    print(randomized_string)


randomize_string(final_string)
