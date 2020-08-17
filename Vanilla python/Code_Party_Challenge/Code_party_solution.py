# The programs below is the solution of the code party challenges


"""
# 1.------------------------- This code reverse a given sentence and word----------------------------------

def reverse_word_and_sentence(word):
    '''
    :param word:'Pass in a string or value'
    :return: 'The reversed value and sentence'
    '''
    numbers = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    for charc in word:
        if charc in numbers and len(word) == 1:
            return f'{word}  is a single digit!The reverse version is still {word} !'
        return word[::-1]

print(reverse_word_and_sentence(input('Enter the sentence')))

"""

""" 
#1b.------------------------------ Returns the maximum and minimum numbers of a list-----------------------------
def min_max(num):
    numbers=num.split()
    maximum= max(numbers)
    minimun=min(numbers)
    print (maximum,' ', minimun ,end=' ')


no= input('Enter the numbers')

min_max(no)
"""

"""
#------------------------------------- 2.  Decryting-------------------------------------------
def decrypt(num):
    numbers = ''
    decm = [0, 1]
    binary = num.split()
    for no in binary:
        for x in no:
            if int(x) in decm:
                numbers=numbers + x
    print(int(numbers,2))

lists = input('Enter the numbers')

decrypt(lists)
"""

"""
# ------------------------------3. Ticket robot----------------------------------------

def robot(ticket):
    checking = sum(ord(tickets) for tickets in ticket)
    design = 'x'
    print(f'curently checking {design * 10}, kindly wait!')
    print('Okay,found!')

    if checking % 2 == 0:
        print('ENTER!')
    else:
        print('SORRY!')


tf = input('Enter your ticket number')
robot(tf)

"""

"""
#-----------------------------------------------------------------4. Trafficator------------------

def timetaken(A, B):
    # Time taken Without traffic
    routes_l = 12
    routes_s = 5
    time_of_ab = {}

    if A[1:3] == 'LS':
        time_of_ab['A'] = routes_l + int(A[3]) + routes_s + int(A[-1])
    elif A[1:3] == 'SS':
        time_of_ab['A'] = routes_s + int(A[3]) + routes_s + int(A[-1])
    elif A[1:3] == 'SL':
        time_of_ab['A'] = routes_s + int(A[3]) + routes_l + int(A[-1])
    else:
        time_of_ab['A'] = routes_l + int(A[3]) + routes_l + int(A[-1])

    if B[1:3] == 'LS':
        time_of_ab['B'] = routes_l + int(B[3]) + routes_s + int(B[-1])
    elif B[1:3] == 'SS':
        time_of_ab['B'] = routes_s + int(B[3]) + routes_s + int(B[-1])
    elif B[1:3] == 'SL':
        time_of_ab['B'] = routes_s + int(B[3]) + routes_l + int(B[-1])
    else:
        time_of_ab['B'] = routes_l + int(B[3]) + routes_l + int(B[-1])

    maximum_time = max(time_of_ab.values())

    if time_of_ab['A'] == maximum_time:
        max_bus = 'A'
    else:
        max_bus = 'B'

    print(f'The bus is --->{max_bus} it spent {maximum_time} minutes on the route')


x = input('Enter A')

y = input('Enter B')

timetaken(x, y)

"""

"""
#5.================= Word frequency=====================================================

from collections import Counter

def most_common_letter(words):

    c = Counter(words)
    if c.most_common()[0][1] != 1:
        print(c.most_common()[0][0])
    else:
        print('None')


letters = input('Enter the word')

most_common_letter(letters)
"""
