import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Procedure'''
#1. NA
#2. NA
#3. NA

'''Part I: Working with a Filesystem'''
#4. The absolute file name for nice.jpg is
#   C:/Users/Student_Login/Desktop/nice.jpg

#5. If I was currently working in the admin directory, the relative filename for
#   nice.jpg would be
#   ../Student_Login/Desktop/nice.jpg

#6. When you use pwd the file C:\\Windows\\Cursors\\cursor1.png was returned,
#   it is an absolute filename because the beggining of the chain is 'C:\\'.
#   You do not have to be in a particular directory for it to make sense:
#   you can go from any directory you want to any other random directory.
#   Because Cloud9 is a different system than Window system, it creates
#   different outputs for ls and pwd.

'''Part II: Rendering an Image on Screen'''
#7.
"""Single Plot of Woman Image"""
"""
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
# Show the figure on the screen
# fig.show()
fig.savefig('women_plot')
"""

# The old code did not work, however, the new cord(above) worked.
# The differences were importing matplotlib, which creates an aggregator, and
# instead of saving it by 'fig.show', you have to save it by
# 'fig.savefig('women_plot')'.

#7a. The woman's nose is about (300,400).

#7b.
"""Single Plot of Cat Image"""
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot')
"""
#7b. The tip of the cat's nose is about (64, 40).

'''Part III: Objects and Methods'''
#8

#8a.
#   fig is an instance of the class Figure
#   ax is an instance of the class AxesSubplot

#8b.
# Similarly, in line 25, the method savefig is being called on the object
# fig. That method is being given 1 argument. That method is a method of
# the class Figure.

#8c. The comments are fine

#9
'''Two pictures of the Woman'''
"""
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('two_woman.png')
"""

#9b
"""
'''5 pictures of the Cats'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
for num in range(0, 5):
    ax[num].imshow(img, interpolation='none')

# Show the figure on the screen
# fig.show()
fig.savefig('five_cats.png')
"""


'''Part V: Keyword = Value Pairs'''
#10
"""
'''2 Pictures of Woman's Earings'''
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')
"""

#11a
"""
'''Three Closeup Code of the Cat'''
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1)
# Show the image data in the first subplot
ax.imshow(img, interpolation='none') # Override the default
ax.set_xlim(25, 95)
ax.set_ylim(50, 10)

ax.set_title('TITLE')
ax.set_ylabel('str')
ax.set_xlabel('X-AXIS')

# Show the figure on the screen
# fig.show()
fig.savefig('experiment')
"""

#11b
"""
'''Three Closeup Code of the Cat'''
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1,3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[2].imshow(img)
ax[0].set_xlim(35, 45)
ax[0].set_ylim(80, 70)
ax[1].set_xlim(45, 55)
ax[1].set_ylim(80, 70)
ax[2].set_xlim(55, 65)
ax[2].set_ylim(80, 70)

# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup')
"""

#12
# Set_visible is an additional method of AxesSubplot. The argument for
# set_visible has to be a boolean so true or false. The default value for
# set_visible is True but it van be changed to False.

#13
"""
'''Red Eyes on the Mice'''
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an array of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')

ax[1].plot(37, 48, 'ro')
ax[1].plot(118, 42, 'ro')
ax[1].plot(141, 42, 'ro')

# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice.png')
"""