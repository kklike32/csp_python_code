#9. NA
#10. NA
#11. NA
#12. NA

#13.
# matplotlib.pyplot (plt) – library used for plotting stuff in images

# numpy (np) – library used for adding arrays and other mathematical functions

# PIL – library used for image processing and image editing capabilities

#14. NA

#15.
#a.
'''Line 19 calls the function subplot from the plt library. The function
is being called with 2 argument(s): 1, 2. The function returns 2
object(s), which is/are being assigned to fig and ax.'''

#b
"""
Line 20 calls __imshow()_ on ___ax[0]____
Line 23 calls __imshow()_ on ___ax[1]___
Line 24 calls __set_xticks()_ on ___ax[1]___
Line 25 calls __set_xlim()_ on ___ax[1]___
Line 26 calls __set_ylim()_ on ___ax[1]___
Line 27 calls __savefig()_ on ___fig___

"""

#c. The coordinates are (1162, 966)

#16. The right most is 795 and left most is 700.
#    The top most is 940 and bottom most 1010.
#    The width is 95 pixels and height is 70 pixels.
#    axes[1].set_xlim(795, 700)
#    axes[1].set_ylim(1010, 940)

#17.
"""
#a
Line 30 uses the join() method from the os.path module. It is being passed
2 arguments. The value it returns is being assigned to the variable earth_file.

#b
In line 31 the open() function of the PIL. Image module returns a new PIL.
Image object, which is being assigned to the variable earth_img.

#c
The resize function takes the 2 arguments height and width. The image is resized
based on these 2 arguments. The double parentheses are there to allow the 2
argument pair.

#d
The purpose of (89, 87) in line 32 is scaling it down so the max width and
height ends on those coordinates.

#e
Line 33 calls the library matplotlib on the variables fig2 and axes 2.
Line 34 calls the imshow function on axes2[0] and displays earth_img there
Line 35 calls the imshow function on axes2[1] and displays earth_small there
Line 36 calls the savefig function on fig2 and saving it in resize_earth

#f
An additional argument that can be passed is a percentage.
The default value is 100%, which is the maximum it can be.
The optional downsampling value is 100%.

#g
The size value specifies a specific area to run a specific command.

#h
The output represents the maximum width and maximum height to run those
coordinates.

#i
The quality of the image that is resized is lower compared the the original
image. This means that the image is downsampled and minimized."""

#18
"""
It makes the original picture divided up into many 2 by 2 pixel squares. It
takes the most prominent color and converts the 3 by 2 pixel squares into one
single pixel on the the screen.
"""

#19
"""
#a
15667.2 kilobytes in student_img
726240 bytes in earth_small

#c
206 kb is student_img
18.3 kb is earth_small

#d
The difference in file size might be because of the downloading process the
computer takes or what type of image is downloaded onto the computer. PNG
images take up different amounts of space compared to other image types.

#e
If a color is used in the paste method, then the pixels in the specified area,
will all turn into that color. It basically sets multiple pixels into the same
color.

#f
The quality is lost when you save a png as a jpg.

#g
Line 40 edits the student_img. It takes the earth_small and pastes it in a
certain location in student_img.
"""
#20
"""

"""