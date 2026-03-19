"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle
tina = turtle.Turtle()

def set_turtle_image(turtle, image_name):
   
    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)


set_turtle_image(tina, 'pikachu.gif')

tina.penup()
tina.speed(3)

for i in range(4):
    tina.goto(200, 200)
    tina.goto(-200, -200)

turtle.exitonclick()