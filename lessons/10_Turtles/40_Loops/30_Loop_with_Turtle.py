"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)  
side=10
forward=50
left=90
tina.goto(0,-4)
tina.begin_fill()
tina.fillcolor("purple")
for i in range(10):
    tina.pencolor("purple")            # Make the turtle move as fast, but not too fast. 
    tina.forward(forward)                     # Move tina forward by the forward distance
    tina.left(360/side)
tina.end_fill()

tina.goto(-90,-100)  
tina.begin_fill()
tina.fillcolor("cyan")
for i in range(10):
    tina.fillcolor("cyan")
    tina.pencolor("cyan")                 # Make the turtle move as fast, but not too fast. 
    tina.forward(forward)                     # Move tina forward by the forward distance
    tina.left(360/side)
tina.end_fill()

turtle.exitonclick() 