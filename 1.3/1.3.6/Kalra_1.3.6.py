import random
#1. NA
#2. NA
#3. NA

'''Part 1: Tuples and Syntax'''
#4. (459, -219, 3490)

#5. One  convention required by one of your teachers regarding the format for
#   submitted work is my English. He wants our name, period, and date on the
#   top right on every document.

#6a. I predict the output will be 'b' because it is the second letter in the
#    list.
#6b. I predict he output will be ('a', 'b') because it is the first two values
#    in the list.

#7a. I predict the output will be True because the a value of 10 was set right
#    before b was set; so the second value will remain 10.
#7b. I predict the output will be 10 because the a value of 10 was set right
#    before b was set; so the second value will remain 10.

'''Part 2: Lists'''
#8. I predict the output will be ['b', 3] because they are the second and last
#   value in the list.

#9. I predict the output will be False because the input was a string and the
#   output is an integer.

#10a. I predict the output will be ['a', 'b', 3, 4, 5] because 4 and 5 is
#     added to the end of the list.
#10b. I predict the output will be ['a', 'b', 3, 4, 5, 6, 7] because 6 and 7 is
#     added to the end of the list.

#11. Adding 5 to the list like that won't work because it is not inside
#    paranthesis which is the correct format.

#12. The value of a will be 18 because 6 is mulptiplied by 3.

'''Part III: Lists and the Random Module'''
#13. NA

#14.
def roll_two_dice():
    '''This function takes the sum of two random dies and displays it'''
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a + b

'''Conclusion'''
#1. a, b, and c are different because a is a variable, b is a tuple, and c is a
#   list.

#2. Computer programming launguages have a variety of variable types because
#   they don't want users to be limited to one or two things.

#3. Functions in python perform a series of commands which can vary from rolling
#   a die to telling someone's letter grade. Boolean statements are either or.
#   For example, True and False are boolean statements. If, elif, and else are
#   an important factor in functions when determining if something True or not.
#   They are all part of if-structures in functions.Programmers use glass-box
#   testing to test if their function is working smoothly. Strings are a data
#   type and can be used to define a variable. There are other types of
#   variable types such as tuples, lists, and regular variables.


#1.3.6 Function Test
print(roll_two_dice())
# I got 7 as my result. Based on the result, I believe that I completed the
# assignment correctly.