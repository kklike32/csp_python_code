from __future__ import print_function
'''Procedure'''
#1. NA
#2. NA
#3. NA
#4. NA
#5. NA, int and float can represent the number six million
#6. Stings are values inside single or double quotation marks while integers are
#   numeric values. They won't go together.
#7. If a negative value is placed to find the index, it will find it starting
#   from the last letter. If a negative or positive value is more than the total
#   amount of characters, it will produce an error.
#8. NA, in iPython
#9. NA, in iPython
#10a. theater has 7 letters so the length of activity would be 7.
#10b. We substract one from the length of, we are taking away the last letter
#     when we splice so the output would be 'theate'.
#11. 'test goo' in the string 'Greatest good for the greatest number!'
#12.
def how_eligible(essay):
    '''This function checks if the input has a question, quote, compound
    sentence, and an exclamation.'''
    total = 0
    if '?' in essay:
        total += 1
    if '"' in essay:
        total += 1
    if ',' in essay:
        total += 1
    if '!' in essay:
        total += 1
    return total

'''Assignment Check'''
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

# I got
'''
4
1
'''
# as a result when I ran the code. Based on my result, I believe that I
# completed the assignment correctly.