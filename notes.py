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

import string
import secrets
a_string = ''.join(secrets.choice(string.digits) for i in range(5))
print(''.join(secrets.choice(string.digits) for i in range(5)))
print(string.digits)
print(''.join(random.choice('234') for i in range(2)))