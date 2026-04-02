""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""
import turtle
from PIL import Image
from pathlib import Path

def resize_gif(image_path, scale=0.5):
    """Resize a GIF and save it as a new file."""
    img = Image.open(image_path)
    new_size = (int(img.width * scale), int(img.height * scale))
    img = img.resize(new_size, Image.LANCZOS)
    resized_path = str(image_path).replace(".gif", "_resized.gif")
    img.save(resized_path)
    return resized_path

def set_turtle_image(t, image_name, scale=0.5):
    """Set the turtle's shape to a resized custom image."""
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)
    resized_path = resize_gif(image_path, scale=scale)

    screen = t.getscreen()
    screen.addshape(resized_path)
    t.shape(resized_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()
set_turtle_image(t, "leaguebot_bolt.gif", scale=0.5)  # change scale here
t.penup()
t.speed(3)

for i in range(6):
    t.pencolor("blue")
    t.pendown()
    t.forward(100)
    t.right(60)

turtle.exitonclick()