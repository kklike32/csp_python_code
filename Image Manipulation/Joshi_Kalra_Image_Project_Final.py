from __future__ import print_function
from PIL import ImageFont, ImageDraw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import PIL
import numpy as np
import random
import Image, ImageOps

"""
'''Version 1.0 - changing the background of the logo to black and white
Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Logo.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

ax.imshow(img, interpolation='none')


print("edits")
height = len(img)
width = len(img[0])
print(height)
print(width)
print (sum(img[200][200]))

for r in range(height):
    for c in range(width):
        if sum(img[r][c]) == 440:
            img[r][c]=[0,0,0,0]
        elif sum(img[r][c]) <= 255:
            img[r][c]=[255,255,255,255]
        else:
            img[r][c]=[0,0,0,255]

print (img[r][c])

img2 = PIL.Image.fromarray(img)
img2.save('logo_background2.png')
"""

"""'''Version 1.1 - changing the background of the logo to red and blue
Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Logo.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

ax.imshow(img, interpolation='none')


print("edits")
height = len(img)
width = len(img[0])
print(height)
print(width)
print (sum(img[200][200]))

for r in range(height):
    for c in range(width):
        if sum(img[r][c]) == 440:
            img[r][c]=[0,0,0,0]
        elif sum(img[r][c]) <= 255:
            img[r][c]=[0,255,255,255]
        else:
            img[r][c]=[255,0,0,255]

print (img[r][c])

img2 = PIL.Image.fromarray(img)
img2.save('logo_background3.png')

# Crops the image so it is only the logo
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'logo_background3.png')
logo_img = PIL.Image.open(filename)
logo_img.crop((200, 205, 740, 775))
logo_img.save('logo_test3.png')
"""

"""
'''Version 1.2 - changing the background of the logo to purple and orange
Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'Logo.jpg')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)

ax.imshow(img, interpolation='none')


print("edits")
height = len(img)
width = len(img[0])
print(height)
print(width)
print (sum(img[200][200]))

for r in range(height):
    for c in range(width):
        if sum(img[r][c]) == 440:
            img[r][c]=[0,0,0,0]
        elif sum(img[r][c]) <= 255:
            img[r][c]=[255,165,10,255]
        else:
            img[r][c]=[255,0,255,255]

print (img[r][c])

img2 = PIL.Image.fromarray(img)
img2.save('logo_background4.png')

# Crops the image so it is only the logo
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'logo_background4.png')
logo_img = PIL.Image.open(filename)
logo_img.crop((200, 205, 740, 775))
logo_img.save('logo_test4.png')
"""
#All code below are cropping the images produced above

"""
#Crops the image so it is only the logo
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'logo_background2.png')
logo_img = PIL.Image.open(filename)
logo_img.crop((200, 205, 740, 775))
logo_img.save('logo_test2.png')
"""

"""
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'logo_test1.png')
# Read the image data into an array
img = plt.imread(filename)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')
print("edits")
height = len(img)
width = len(img[0])
print (width)
print (height)
for r in range(height):
    for c in range(width):
        if sum(img[r][c]) <= 250:
            img[r][c]=[255,255,255,255]
        else:
            img[r][c]=[0,0,0, 255]
ax.cla()
#img2 = PIL.Image.fromarray(img)
fig.savefig("logo_test2.png")
"""

"""
Shows the minor ticks to show us where the logo is
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'logo_background1.png')
img = plt.imread(filename)
fig, ax = plt.subplots(1, 1)
ax.imshow(img, interpolation='none')
ax.minorticks_on()
fig.savefig('logo_test.png')
"""


def paste_logo():
    """This function is our main function that makes changes to our images and
    endorses MTT. You control th eoutcome of your image.You can change the tint,
    ,placement of logo, color of logo, and text location.This code is made by
    Parth Joshi and Keenan Kalra."""
    print ("Hello. This program was created by Parth Joshi and Keenan Kalra.")
    print ("This function will take an image (.jpg or .png) and you will have the option to manipulate it.")
    print ("This function can insert the MTT logo in a certain place, add a tinting layer, add a border, and add some text.")
    print ()

    image_input = raw_input(str("Which image do you want to manipulate? EX. 'Obama.jpg' \n"))

    name = raw_input(str("Which name do you want the final image to have? \n"))
    #Get the inputs to identify the file that you are manipulating.
    print ()

    logo_ans = raw_input(str("Do you want 'green', 'black', 'red', or 'purple' logo? \n")).lower()
    #Chose logo color
    directory = os.path.dirname(os.path.abspath(__file__))
    # Open the files in the same directory as the Python script
    img_file = os.path.join(directory, image_input)
    #Picking the actual logo file
    if logo_ans == "green":
        logo_file = os.path.join(directory, 'logo_test1.png')
    elif logo_ans == "black":
        logo_file = os.path.join(directory, 'logo_test2.png')
    elif logo_ans == "red":
        logo_file = os.path.join(directory, 'logo_test3.png')
    elif logo_ans == "purple":
        logo_file = os.path.join(directory, 'logo_test4.png')
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'Modified_Images')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed


    #png_to_jpg(img_file)
    if ".png" in img_file and ".jpg" not in img_file:
        img = PIL.Image.open(img_file)
        img.save(img_file + ".jpg")
        img_file = os.path.join(directory, image_input + ".jpg")
        print ("Your file was a 'png'. We converted it to jpg for this program to work.")

    #Open and show the given image in a new figure window
    image_input2 = plt.imread(img_file)
    logo_img = PIL.Image.open(logo_file)

    height = len(image_input2)
    width = len(image_input2[0])

    #changing into a PIL image from a numpy
    image_input3 = PIL.Image.fromarray(image_input2)




    """Adding a tinting layer to the image"""
    print ()
    image_input4 = np.array(image_input3)
    tinting_input = str(raw_input("Do you want to add a tinting layer to the final image? (yes/no) \n")).lower()
    #tinting input optiion for user
    if tinting_input == "yes":
        tinting_input1 = str(raw_input("Do you want to choose the color - 'red', 'green', 'blue' - or 'random' choice? \n")).lower()
        #red tint
        if tinting_input1 == 'red':
            percentage_red = int(raw_input("What percentage of your color should the tint be?"))
            for r in range(height):
                for c in range(width):
                    image_input4[r][c][0] = 255*(percentage_red/100)
        #green tint
        elif tinting_input1 == 'green':
            percentage_green = int(raw_input("What percentage of your color should the tint be?"))
            for r in range(height):
                for c in range(width):
                    image_input4[r][c][1] = 255*(percentage_green/100)
        #blue tint
        elif tinting_input1 == 'blue':
            percentage_blue = int(raw_input("What percentage of your color should the tint be?"))
            for r in range(height):
                for c in range(width):
                    image_input4[r][c][2] = 255*(percentage_blue/100)
        #random tint
        elif tinting_input1 == "random":
            percent = random.randint(0, 101)
            color = random.randint(0, 2)
            for r in range(height):
                for c in range(width):
                    image_input4[r][c][color] = 255*(percent/100)
        else:
            print ("How hard is it to type in the given choices? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")

    elif tinting_input == "no":
        print("Okay, no tint for the image.")
    else:
        print ("How hard is it to type in 'yes' or 'no'? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")

    #back to a PIL image
    image_input5 = PIL.Image.fromarray(image_input4)




    """Adding a logo on the picture"""
    print ()
    print ("Which corner do you want the logo to appear?")
    print ("1 is top left")
    print ("2 is top right")
    print ("3 is bottom left")
    print ("4 is bottom right")
    corner_input = str(raw_input("Type a number from 1 through 4: \n"))
    #resize the logo
    logo_small = logo_img.resize(((width + height)/4, (width + height)/4))

    if width <= height:
        #Pasting the logo onto the given image
        if corner_input == "1":
            image_input5.paste(logo_small, (-(width/10), height - (height * 29)/27), mask=logo_small)
        elif corner_input == "2":
            image_input5.paste(logo_small, (width - (width * 1025)/2048, height - (height * 29)/27), mask=logo_small)
        elif corner_input == "3":
            image_input5.paste(logo_small, (-(width/10), (height * 19)/32), mask=logo_small)
        elif corner_input == "4":
            image_input5.paste(logo_small, (width - (width * 1025)/2048, (height * 19)/32), mask=logo_small)
        else:
            print ("How hard is it to type in 1-4? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")
    elif width > height:
        #Pasting the logo onto the given image
        if corner_input == "1":
            image_input5.paste(logo_small, (-width/15, -height/12), mask=logo_small)
        elif corner_input == "2":
            image_input5.paste(logo_small, (width - (width + height)/5, -height/12), mask=logo_small)
        elif corner_input == "3":
            image_input5.paste(logo_small, (-width/15, height - (width + height)/5), mask=logo_small)
        elif corner_input == "4":
            image_input5.paste(logo_small, (width - (width + height)/5, height - (width + height)/5), mask=logo_small)
        else:
            print ("How hard is it to type in 1-4? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")




    """Adding text to the image"""
    print ()
    text_opt = str(raw_input("Do you want to have 'I Support MTT!' in the picture? (yes/no)\n")).lower()
    if text_opt == 'yes':
        #choose font
        font = ImageFont.truetype("TMSGEO.TTF", (width)/10)
        draw = PIL.ImageDraw.Draw(image_input5)
        rect = PIL.ImageDraw.Draw(image_input5)
        text_choice = str(raw_input("Type in 'top' or 'bottom' for the placement of the text: P.S - choose the opposite side of the logo input\n")).lower()
        text_color = str(raw_input("Type in 'black', 'red', 'green', 'blue', or 'white' for the color of the text: \n")).lower()
        width_rect = int((raw_input("What should the width of the rectangle around the text be? (integer) P.S - We recommend no more than 15. \n")))
        if text_color == "black":
            col = "#000"
        elif text_color == "white":
            col = "#fff"
        elif text_color == "red":
            col = "#f00"
        elif text_color == "green":
            col = "#0f0"
        elif text_color == "blue":
            col = "#00f"
        elif text_color == "orange":
            col = "#ffa500"
        elif text_color == "purple":
            col = "#800080"
        elif text_color == "yellow":
            col = "#cc0"
        else:
            print ("How hard is it to type in the color? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")

        def draw_rectangle(draw, coordinates, color, width=1):
            for i in range(width):
                rect_start = (coordinates[0][0] - i, coordinates[0][1] - i)
                rect_end = (coordinates[1][0] + i, coordinates[1][1] + i)
                draw.rectangle((rect_start, rect_end), outline = color)

        #text on top of the image
        if height >= width:
            if text_choice == "top":
                draw.text((width * 23/100, (height*14)/200), "I Support MTT!", fill=col, font=font)

                rect = PIL.ImageDraw.Draw(image_input5)

                top_left = (width * 19/100, height * 8/200)
                bottom_right = (width * 89/100, height * 32/200)

                outline_width = width_rect
                outline_color = col

                draw_rectangle(rect, (top_left, bottom_right), color=outline_color, width=outline_width)

            #text on the bottom of the image
            elif text_choice == "bottom":
                draw.text((width * 23/100, (height*169)/200), "I Support MTT!", fill=col, font=font)

                rect = PIL.ImageDraw.Draw(image_input5)

                top_left = (width * 19/100, height * 163/200)
                bottom_right = (width * 89/100, height * 187/200)

                outline_width = width_rect
                outline_color = col

                draw_rectangle(rect, (top_left, bottom_right), color=outline_color, width=outline_width)

            else:
                print ("How hard is it to type in 'top' or 'bottom'? Press Ctrl+C and then the up",
                "arrow and then enter to run the code again.")

        #From here
        elif height < width:
            font = ImageFont.truetype("TMSGEO.TTF", (width + height)/20)
            if text_choice == "top":
                draw.text((width * 23/100, (height*14)/200), "I Support MTT!", fill=col, font=font)

                rect = PIL.ImageDraw.Draw(image_input5)

                top_left = (width * 19/100, height * 8/200)
                bottom_right = (width * 79/100, height * 39/200)

                outline_width = width_rect
                outline_color = col

                draw_rectangle(rect, (top_left, bottom_right), color=outline_color, width=outline_width)

            #text on the bottom of the image
            elif text_choice == "bottom":
                draw.text((width * 23/100, (height*150)/200), "I Support MTT!", fill=col, font=font)

                rect = PIL.ImageDraw.Draw(image_input5)

                top_left = (width * 19/100, height * 144/200)
                bottom_right = (width * 79/100, height * 180/200)

                outline_width = width_rect
                outline_color = col

                draw_rectangle(rect, (top_left, bottom_right), color=outline_color, width=outline_width)

            else:
                print ("How hard is it to type in 'top' or 'bottom'? Press Ctrl+C and then the up",
                "arrow and then enter to run the code again.")
        #to here
    elif text_opt == "no":
        print ("Okay, no text in the image.")
    else:
        print ("How hard is it to type in 'yes' or 'no'? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")



    """Adding a border around the picture"""
    print ()
    border_opt = str(raw_input("Do you want to have a frame in the picture? (yes/no)\n")).lower()
    if border_opt == "yes":
        choice1 = str(raw_input("Type in 'random' for a random color or 'choice' to pick your color for the frame: \n")).lower()
        #random color for border
        if choice1 == 'random':
            r = random.randint(0, 256)
            g = random.randint(0, 256)
            b = random.randint(0, 256)
            print (r,g,b,"is your wacky random value")
        #choosing color for border
        elif choice1 == 'choice':
            r, g, b = str(raw_input("Enter a rgb value with spaces in between each number: (Green is '0 255 0')\n")).split()
            r = int(r)
            g = int(g)
            b = int(b)
        else:
            print ("How hard is it to type in 'random' or 'choice'? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")

        #inserting border on image
        img_with_final_edits = ImageOps.expand(image_input5,border=(height/100),fill=(r, g, b))

    elif border_opt == 'no':
        print ("Okay, no border around the image.")
        img_with_final_edits = image_input5

    else:
        print ("How hard is it to type in 'yes' or 'no'? Press Ctrl+C and then the up",
            "arrow and then enter to run the code again.")

    #Display image and rename the file
    new_image_filename = os.path.join(new_directory, "final_" + name + '.png')
    #saving file
    img_with_final_edits.save(new_image_filename)
    print ("The file name is saved as")
    print ("final_" + name + '.png')

paste_logo()