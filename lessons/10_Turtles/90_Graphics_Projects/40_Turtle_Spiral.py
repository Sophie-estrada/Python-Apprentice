"""Penta Spiral

This program already works. See if you can change it to make it draw a different pattern.
"""

import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))
def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")

# Make a new turtle
myTurtle = turtle.Turtle()

# This code sets our shape to a turtle
myTurtle.shape("turtle")

# Set your turtle's speed
myTurtle.speed(0)

# Set your turtle's color
myTurtle.color("medium slate blue")
colors = ("turquoise", "sky blue", "violet", "blue violet", "cornflower blue")
# Use a loop to repeat the code below 50 times

for i in range(1000):
    myTurtle.pensize(1)
    # Set the turtle color to a random color
    myTurtle.pencolor(getNextColor(i))

    # Move the turtle (5*i) pixels. 'i' is the loop variable
    myTurtle.forward(1 * i)

    # Turn the turtle (360/7) degrees to the right
    myTurtle.right(360 / 7)

    # Change the turtle width to 'i' (the loop variable)
    myTurtle.width(i)

    # Check the pattern against the picture in the recipe. If it matches, you are done!

turtle.done()

# Now check in your code!