from __future__ import print_function # must be first in file

'''Procedure'''
#1 - N/A
#2 - N/A
#3 - N/A
#4 - N/A

'''PART 1: Nested if structures and testing'''
#1
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'

#1a. It came from line 17( mine is from line 25)

#1b. line 15 - Orange
#    line 17 - Apple
#    line 20 - Potato
#    line 22 - It's a bug

#1c The program will never run line number 20 will never result in bananas being
#   reported as starchy because bananas are also in the fruits category.

#2
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    # Add tests so that all lines of code are visited during test
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()'

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

#3
def f(n):
    '''Number 3; creating a flowchart that takes a number and runs different
    tests and chooses which category should it go in'''
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print("The input is a multiple of 6.")
                return "The input is a multiple of 6."
            else:
                print ("The input is an even integer.")
                return "The input is an even integer."
        else:
            print ("The input is an odd integer.")
            return "The input is an odd integer."
    else:
        print ("The input is not an integer.")
        return "The input is not an integer."

#4 You can use 12 to test the multiple of 6, you could use 1 to test the odd
#  integer, you could use 2 to test the even integer, and type in a decimal to
#  test if it is an integer.

#5
def number_id_test():
    ''' Unit test for f(n)
    returns True if good, returns False and prints error if not
    good
    '''
    works = True
    if f(6) != 'The input is a multiple of 6.':
        works = 'multiple of 6 bug in f()'
    if f(2) != 'The input is an even integer.':
        works = 'even integer bug in f()'
    if f(1) != 'The input is an odd integer.':
        works = 'odd integer bug in f()'
    if f(2.5) != 'The input is not an integer.':
        works = 'not an integer bug in f()'

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

'''PART 2: The raw_input() function, type casting, and print() from Python 3'''

#7 Addition in concatenation does not take the sum of the numbers; it combines
#  them by writing the digits together. For example, '2' + '34' is not 36, it is
#  '234'. Addition in numeric addtion adds numbers the way we expect it to. The
#  sum of 2 and 34 would return 36.

#8
import random

def guess_once():
    '''Guessing game for question number 8. The range of the numbers are 1
    through 4. guess variable is how the user will input the data'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
            if guess > secret:
                print('Too high, my number was ', secret, '.', sep='')
            else:
                print('Too low - my number was ', secret, '.', sep='')
    else:
        print('Right on! I was number ', guess, end='!\n')
#8a. In line 11, it prints the string 'Right, my number is', the guess, and and
#    exclamation mark. \n stands for a new indented line.

#9
def quiz_decimal(low, high):
    '''Quiz to test how well you know your decimals. you first enter two
    numbers, after that, you have to type a number in between, if you do, you
    get it correct. If you don't, it will tell your guess is either higher or
    lower than the first input.'''
    print('Type a number between', str(low), 'and', str(high), ':')
    guess = float(raw_input('Guess: '))
    if guess > low and guess < high:
        print('Good! ', str(low), ' < ', str(guess), ' < ', str(high), sep='')
    elif guess == low:
        print('No', str(guess), 'is equal to', str(low))
    elif guess == high:
        print('No', str(guess), 'is equal to', str(high))
    else:
        if guess > high:
            print('No, ', str(guess), ' is greater than ', str(high), sep='')
        else:
            print('No, ', str(guess), ' is less than ', str(low), sep='')

'''CONCLUSION'''
#1 If-structures can be tested by glass-box testing. Glass-box testing runs
#  ever possible situation that the user can input into the if-structure. It
#  makes the if structere works.

#2 In if-else block structures, only one if, elif, or else can be excecuted in
#  one command. All of them can not be run at once.

#3 Test suite ensures that an function runs properly. Programmers write them
#  before they write the actual functions so they have an idea on how it is
#  going to look like.

#4 You could make a function for each output case.
def f_6(n):
    '''takes the f(n) function and breaks it down to individual parts; this part
    checks if the integer is a multiple of 6'''
    if int(n) == n and n % 2 == 0 and n % 3 == 0:
        return True

def f_even(n):
    '''takes the f(n) function and breaks it down to individual parts; this part
    checks if the integer is even'''
    if int(n) == n and n % 2 == 0:
        return True

def f_odd(n):
    '''takes the f(n) function and breaks it down to individual parts; this part
    checks if the integer is odd'''
    if int(n) == n and n % 2 != 0:
        return True


def f_int(n):
    '''takes the f(n) function and breaks it down to individual parts; this part
    checks if the input is an integer'''
    if int(n) != n:
        return True


'''CHALLENGE'''
def f_challenge(n):
    '''challenge; breaks apart the f(n) function into four different functions;
    the four functions are run if the input is true under the fuction'''
    if f_6(n) == True:
        print("The input is a multipe of 6.")
    elif f_even(n) == True:
        print ("The input is an even integer.")
    elif f_odd(n) == True:
        print ("The input is an odd integer.")
    else:
        print ("The input is not an integer.")

'''Assignment Check'''
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
number_id_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

#The result that I got were
'''
NOT Citrus, Fruit
All good!
The input is not an integer.
The input is an even integer.
The input is an odd integer.
The input is a multiple of 6.
The input is a multiple of 6.
The input is an even integer.
The input is an odd integer.
The input is not an integer.
All good!
I have a number between 1 and 4 inclusive.
Guess: 2
Too low - my number was 3.
I have a number between 1 and 4 inclusive.
Guess: 3
Too high, my number was 2.
Type a number between 4 and 4.1 :
Guess: 4.05
Good! 4 < 4.05 < 4.1
Type a number between 4 and 4.1 :
Guess: 4
No, 4.0 is less than 4
The input is not an integer.
True
The input is an even integer.
The input is an even integer.
True
The input is an odd integer.
The input is an odd integer.
True
The input is a multipe of 6.
None

In [36]: %run Kalra_1.3.4.py
NOT Citrus, Fruit
All good!
The input is not an integer.
The input is an even integer.
The input is an odd integer.
The input is a multiple of 6.
The input is a multiple of 6.
The input is an even integer.
The input is an odd integer.
The input is not an integer.
All good!
I have a number between 1 and 4 inclusive.
Guess: 2
Too low - my number was 3.
I have a number between 1 and 4 inclusive.
Guess: 2
Too high, my number was 1.
Type a number between 4 and 4.1 :
Guess: 4
No, 4.0 is less than 4
Type a number between 4 and 4.1 :
Guess: 4.05
Good! 4 < 4.05 < 4.1
The input is not an integer.
True
The input is an even integer.
The input is an even integer.
True
The input is an odd integer.
The input is an odd integer.
True
The input is a multipe of 6.
The input is a multipe of 6.
True
'''
# Based on the results I got, I believe I did the assignment correctly because
# all my functions run properly and the glass box testing also works perfectly.