from __future__ import print_function # use Python 3.0 printing
#has to be up top for the code to work ^

'''PART 1: Procedure'''
#1 N/A
#2 N/A
#3 N/A
#4 N/A
#5 N/A


'''PART 2: Conditionals'''
# 6a. Prediction:
# a**2 >= 9 and not a>3 - TRUE


# 6b. Prediction:
#a+2 == 5 or a-1 != 3 - TRUE

#Predictions were correct

#7 N/A - work on iPython

#8 N/A - work on iPython


'''PART 2: if-else Structures & the print() function!!!!'''
#9
def age_limit_output(age):
    '''Step 9a if-else example, checks if the age is below 13, the output
    depends on whether the age is above or below 13'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print('Minimum age is', AGE_LIMIT)
#9a. 10 is less than 13 so it is going to say "10 is below the age limit"
    # and "Minimus age is 13"

#9b.
def report_grade(percent):
    '''Step 9b if-els, checks if the percent is below 80, the output
    depends on whether the age is above or below 80'''
    percentage = 80
    if percent < percentage:
        print ('A grade of', percent, 'does not indicate mastery.')
        print ('Seek extra practice or help.')
    else:
        print ('A grade of', percent, 'indicates mastery.')
        print ('Keep up the good work!')


'''PART 3:  The in operator and an introduction to collections'''
#10 N/A - work on iPython

#11
def vowel(letter):
    '''Checks if there is a vowel in a word'''
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
# should check len(letter)==1

def  letter_in_word(guess, word):
    '''Checks if there is a letter in a word, returns true or false depends on
    the guess'''
    if guess in word:
        return True
    else:
        return False

#12
def hint(color, secret):
    '''Checks if there is a certain color in the order, returns a statement
    depending on the color given'''
    if color in secret:
        print ('The color', color, 'IS in the secret sequence of colors.')
    else:
        print ('The color', color, 'IS NOT in the secret sequence of colors.')

'''Conclusion'''
#1
#The indendented blocks after the colon in if, elif, and/or else are there to
#show us which blocks are going to run if an action is true.

#2 Some operaters that create boolean expressions are AND, OR, and NOT. One
#  other one that I found on the web is NAND. It returns false if both the
#  statements are true.

#3 Jayla and Kendra are both correct while Ira is not. There is not going to be
#  a huge difference between the run times. Jayla is correct because you can
#  edit that piece of code at one place. Kendra is correct because every
#  character takes up some part of the memory.

'''Assignment Check'''
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)