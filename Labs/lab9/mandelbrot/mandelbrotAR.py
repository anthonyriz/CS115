# mandelbrot.py
# Lab 9
#
# Name: Anthony Rizzuto
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    """ 
    mult uses only a loop and addition
    to multiply c by the integer n
    """
    result = 0
    
    for x in range(n):
        result += c
    return result

print(mult(2,5))
def update( c, n ):
    """ 
    update starts with z=0 and runs z = z**2 + c
    for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c,n):
    """ inMSet takes in 
            c for the update step of z = z**2+c 
            n, the maximum number of times to run that step
        Then, it should return 
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    for i in range ( n ):
        z = z**2 + c
        if abs(z) > 2:
            return False
    else: return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file

    image.saveFile()

    ''' if you changed the line if col % 10 == 0 and row % 10 == 0: to if col % 10 == 0 or row % 10 == 0:
    the image would change which pixels are plotted on the graph, meaning instead of every 10th row and 10th column
    being plotted, pixels would be plotted in either every 10th row or 10th column. So, more pixels would be plotted 
    if you changed the and to or
    '''

def scale( pix, pixMax, floatMin, floatMax):
    """ scale takes in 
            pix, the CURRENT pixel column (or row)
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that corresponds to pix
    """

    return floatMin + pix * ((floatMax - floatMin)/ pixMax)


def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x = scale(col, 300, -2, 1)
            y = scale(row, 200, -1, 1)

            c = x + y*1j
            n = 25

            if inMSet( c, n ) == True:
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file
    
    image.saveFile()


mset()