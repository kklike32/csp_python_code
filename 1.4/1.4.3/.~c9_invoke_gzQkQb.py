from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import PIL

'''Procedure'''
#1. NA
#2. NA
#3. NA

'''Part I: Using Arrays of Pixels'''
#4. Both arrays and lists cantain multiple values. However, arrays only contain
#   one type of value, intergers, strings, e.t.c, while list can contain
#   multiple types.


#5
""" Tells the pixel color of the woman's image
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')

# Image Type
print(type(img))

# Height
print(len(img))

# Width
print(len(img[0]))

# Green Color
print (img[5][9][1])

# Red Color
print (img[4][10][0])

# Red Color 2.0
print (img[49][24][0])

# The height is 960 pixels.
# The width is 584 pixels.
# The green intensity is 94.
# The red intensity is 62.
# The red intensity at 25th pixel on the 50th row is 71.
"""

'''Part II: Manipulating Pixels'''

#6
"""
Turns Woman's Earring to Green color
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
height = len(img)
width = len(img[0])
for row in range(420, 471):
    for column in range(125, 166):
        img[row][column] = [0, 255, 0]
fig.savefig('green_earing.png')
"""

#7
"""Makes the sky change color
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure

###
# Change a region if condition is True (SKY)
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta

#b
###
# Change a region if condition is True (EARRING)
###
for r in range(420,471):
    for c in range(125,162):
        if sum(img[r][c])>375: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,0,255] # R + B = magenta


###
# Show the image data
###
fig.savefig('woman_magenta_sky.png')
"""

#7a. The for loop checks only until the 155th row. It checks the brightness of
#    each pixel in that area, and if it is bright enough, it changes it to
#    magenta.

#7b. Above

#8.
"""
This is a creative image we made.
def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''

    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(0,rows,stripe_width):
        for width in range(stripe_width):
            for column in range(columns):
                image[row][column] = [255, 255, 255, 127.5]

    for column in range(0,columns, stripe_width):
        for height in range(stripe_width):
            for row in range(rows):
                image[row][column] = [255, 255, 255, 127.5]

    return image

if __name__ == "__main__":
    image = make_mask(100,100,10)

    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')
"""

#9
def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''

    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(0,rows,stripe_width):
        for width in range(stripe_width):
            for column in range(columns):
                image[row][column] = [255, 255, 255, 127.5]
                i

    for column in range(0,columns, stripe_width):
        for height in range(stripe_width):
            for row in range(rows):
                image[row][column] = [255, 255, 255, 127.5]
    if sum(img[rows, columns]) > 
    y = rows
    x = columns

    line = (x **2 )/36 + (y ** 2)/36

    if sum(image[rows][columns]) > 300:
        if rows == line and columns == line:
            image[rows][columns] = [0, 0, 255, 255]

    return image


'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
#
fig, ax = plt.subplots(1, 2)
###
# Change a region if condition is True (SKY)
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta

#b
###
# Change a region if condition is True (EARRING)
###
for r in range(420,471):
    for c in range(125,162):
        if sum(img[r][c])>375: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,0,255] # R + B = magenta

image = make_mask(100,100,10)
ax(0).imshow(img, interpolation="none")
ax(1).imshow(image)
fig.savefig("woman_mask.png")