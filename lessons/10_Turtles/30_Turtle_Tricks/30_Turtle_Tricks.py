"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

tina.begin_fill()
tina.fillcolor("cyan")
tina.circle(60)
tina.end_fill()
tina.goto(0,-100)

tina.begin_fill()
tina.fillcolor("purple")
tina.circle(60)
tina.end_fill()
tina.goto(75,-59)

tina.begin_fill()
tina.fillcolor("yellow")
tina.circle(60)
tina.end_fill()


turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!