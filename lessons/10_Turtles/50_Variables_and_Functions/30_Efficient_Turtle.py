
"""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2) 
                          # Make the turtle move as fast, but not too fast. 
tina.begin_fill()
tina.fillcolor("blue violet")
tina.pencolor("blue violet")

def draw_shape(dist, side, tina):
        for _ in range(side):
         tina.forward(dist)
         tina.left(360/side)

draw_shape(85, 12, tina)
tina.end_fill()


turtle.exitonclick()                     # Close the window when we click on it