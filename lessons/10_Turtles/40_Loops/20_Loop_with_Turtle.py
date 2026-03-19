"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)  
tina.goto(-200,-200)  
tina.begin_fill()
tina.fillcolor("red")
for i in range(5):
    tina.pencolor('red')                  # Make the turtle move as fast, but not too fast. 
    tina.forward(150)                     # Move tina forward by the forward distance
    tina.left(72)
tina.end_fill()

tina.goto(150,-200) 
tina.begin_fill()
tina.fillcolor("blue")                      # Turn tina left by the left turn
for i in range(5):
    tina.pencolor('blue')                  # Make the turtle move as fast, but not too fast. 
    tina.forward(150)                     # Move tina forward by the forward distance
    tina.left(72)
tina.end_fill()

tina.goto(-250,200)
tina.begin_fill()
tina.fillcolor("green")
for i in range(5):
    tina.pencolor('green')                  # Make the turtle move as fast, but not too fast. 
    tina.forward(150)                     # Move tina forward by the forward distance
    tina.left(72)
tina.end_fill()

tina.goto(150,200)
tina.begin_fill()
tina.fillcolor("yellow")
for i in range(5):
    tina.pencolor('yellow')                  # Make the turtle move as fast, but not too fast. 
    tina.forward(150)                     # Move tina forward by the forward distance
    tina.left(72)
tina.end_fill()
tina.goto(0,0)
turtle.exitonclick()                    # Close the window when we click on it