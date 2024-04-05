from turtle import *
import math
import random
import time

Locations = {
    "Madison": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/7.gif",
    "Outer Banks": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/1.gif",
    "Tokyo": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/2.gif",
    "Sanoma": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/3.gif",
    "South Africa": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/4.gif",
    "Lake Geneva": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/5.gif",
    "Las Vegas": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/6.gif"
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

place('Madison', 0,0)

done()