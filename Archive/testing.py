from turtle import *
import math
import random
import time

Locations = {
    "Madison": "Location Photos/7.gif",
    "Outer Banks": "Location Photos/1.gif",
    "Tokyo": "Location Photos/2.gif",
    "Sanoma": "Location Photos/3.gif",
    "South Africa": "Location Photos/4.gif",
    "Lake Geneva": "Location Photos/5.gif",
    "Las Vegas": "Location Photos/6.gif"
}

def place (location,x,y):
    screen = Screen()
    
    # Register called location shape from the dictionary
    screen.addshape(Locations[location])

    # Create a turtle and set its shape to the registered GIF shape
    gif_turtle = Turtle()
    gif_turtle.shape(Locations[location])

    # Move the turtle around to see the GIF
    gif_turtle.penup()
    gif_turtle.goto(x,y)

place('Outer Banks', 0,0)

done()