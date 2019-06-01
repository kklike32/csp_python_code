from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

'''Procedure'''
#1. NA
#2. NA
#3. NA

'''Part I: for loops, range(), and help()'''
#4.
def days():
    '''The output is each letter 'MTWRFSS' combined with day.
       The output is a number between 5 and 8 combined with 'th'.
    '''
    for day in 'MTWRFSS':
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

#5.
def picks():
    lst = [] # make an empty list
    # Why all the brackets below?
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    lst += [random.choice([1, 3, 10])]
    for choice in range(5):
        lst += [random.choice([1, 3, 10])]

    plt.hist(lst)
    plt.savefig('1.3.7/picks')

#6a.
def roll_hundred_pair():
    '''Prodces the sum for 100 six-sided die'''
    lst = []
    for choice in range(0, 100):
        lst += [random.randint(1, 6)] + [random.randint(1, 6)]

    plt.hist(lst)
    plt.savefig('1.3.7/roll_hundred_pair')

#6b.
def dice(n):
    '''Produces the sum for n number of six-sided die'''
    total = 0
    total += random.choice([1, 2, 3, 4, 5, 6])
    for choice in range(1, n):
        total += random.choice([1, 2, 3, 4, 5, 6])

    print ("The range was", total, ".")

'''Part 3: While Loops'''
#7.
def validate():
    '''This function checks if a certain letter is in the phrase
    'hangman word'.'''
    guess = '2' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
#7. Line 2 is neccesary so the while loop will run.

#8.
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    Chooses a random person from four people that may have a chance to
    win the lottery. User tries to guesss which person is it going to be.
    '''
    winner = random.choice(players)

    ####
    # User has to guess which person won the lottery.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # chooses the list of people
        print(p+', ', end='')
    print(players[len(players)-1]) # prints all the players

    ####
    # while loop runs until a match is found and returns how many times it ran
    # through the guesses variable
    ####
    guesses = 1
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses


#9
def goguess(range1=range(1, 21)):
    '''takes a number between 1 and 20 which the user has to guess that
    number, user will get how many times it took them'''
    winner = random.choice(range1)

    ####
    # User has to guess which person won the lottery.
    ####
    print('Guess a number between 1 and 20: ')

    ####
    # while loop runs until a match is found and returns how many times it ran
    # through the guesses variable
    ####
    guesses = 1
    answer = int(raw_input())
    while answer != winner:
        if answer > winner:
            print (answer, 'is too high.')
        else:
            print (answer, 'is too low.')
        print('Guess again!')
        answer = int(raw_input())
        guesses += 1
    print('Right, my number was', winner, 'You guessed in', guesses, 'guesses!')
    return guesses

#10. After 12 guesses you can gaurantee to know the right answer. This is
#    possible because 6000 can be halved 12 times before you get 1.3. When you
#    get less than 2, you are gauranteed to know the number.

'''Part 3: Practice'''
#11.
#a
def matches(ticket, winners):
    '''takes two randomly generated lists and decides whether there is/are
    common number(s) between them'''
    count = 0
    for t in winners:
        if t in ticket:
            count += 1
    return count
#b
def report(guess, secret):
    '''checks if the colors in two lists are in the same place, if so it adds
    one to it, if it is in the wrong place but is still there, it finds the
    difference of the lined up ones and the ones in the right place'''
    right_place = 0

    for color in range(len(guess)):
        right_place += 1 if guess[color] == secret[color] else 0

    list1 = sorted(guess)
    list2 = sorted(secret)
    lined_up = 0

    for lined in range(len(list1)):
        lined_up += 1 if list1[lined] == list2[lined] else 0

    wrong_place = lined_up - right_place
    result = [right_place, wrong_place]

    print (result)


'''Conclusion'''
#1. Having multiple lines that run the same code would be a huge problem if you
#   had to edit one part of it, you would have to change everything.

#2. Iteration usually happens to a large piece of data. This is because the
#   large piece of data has to be changed and iteration is the best option.

#3. While loops run until the statement after it becomes false. For loops run
#   until there is no more data points.

#4. We could save more time at home figuring out other possible ways we could
#   solve the problems. The positives were that we both we curious and asked
#   lots of questions.

'''1.3.7 Function Test'''
days()
picks()
roll_hundred_pair()
dice(50)
validate()
guess_winner()
goguess()

ticket_list = [11, 12, 13, 14, 15]
winner_list = [3, 8, 12, 13, 17]
matches(ticket_list, winner_list)

guess = ['red','red','red','green','yellow']
secret = ['red','red','red','yellow','black']
report(guess, secret)

# Based on the results I got, I believe that I completed this assignment
# correctly.