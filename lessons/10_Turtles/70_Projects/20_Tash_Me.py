""" 
Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustache
3) Move the moustache to the right spot on the emoji
"""
import turtle

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
set_turtle_image(t, "pikachu.gif")
set_background_image(screen, "emoji.png") # Set the background image of the screen
t.penup() # Lift the pen to avoid drawing lines
t.forward(100) # Move the turtle forward to position it correctly on the emoji
t.right(90) # Rotate the turtle to the right
turtle.exitonclick()