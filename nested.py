"""
CSci 127 Teaching Staff
February 2018, Updated for Spring 2025
A template for a program that draws nested triangles 
Modified by:  ADD YOUR NAME HERE
ADD YOUR EMAIL
"""

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def triangle(t, length, scale):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than scale,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2, scale).
    """
    
     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################    


def nestedTriangle(t, length, scale):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than scale,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, scale/2).
    """

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################       


def main():
    n = int(input('Enter length: '))
    s = int(input('Enter scale: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    triangle(tom, n, s)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedTriangle(tess, n, s)

if __name__ == "__main__":
     main()
     
          
