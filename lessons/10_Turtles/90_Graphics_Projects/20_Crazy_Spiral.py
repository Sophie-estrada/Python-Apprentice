"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""
import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["purple", "blue", "cyan", "yellow", "blue violet"]

def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 130  # the length of the flaming arms

t = turtle.Turtle() 
t.pensize(5)
t.shape("turtle") 

t.width(2) 

t.speed(0) 

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""    
    t.pencolor(getRandomColor())
    t.left(300)
    t.forward(500)
    t.right(600)
    t.forward(100)
    t.goto(100,0)

num_shapes = 100

for i in range(num_shapes):
    make_a_shape(t)
    t.right(360/num_shapes)

for i in range(25):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(640) 

    t.left(40) 

    t.forward(flameSize) 

    t.right(170) 

    t.forward(flameSize) 

    t.right(62) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 


# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.
