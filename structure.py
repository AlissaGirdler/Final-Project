from turtle import *
import math
import random
import time

##################   VARIABLE LIST   ##################


bubble_x = -280
bubble_y = 375


##################   FUNCTION LIST   ##################


# Function to clear Python canvas of previous actions based on entered paramater or number of actions that need to be erased
def clear_actions(num_actions):
    for _ in range(num_actions):
        undo()

# INCOMPLETE Sets up turtle formatting
def formatting():
    title("Taylor's Vacation")
    setup(height=800, width=1000)
    hideturtle()

#Draws word bubble for text to appear in 
def word_bubble(radius, color):

    speed(0), pencolor(color), fillcolor(color), penup(), goto(bubble_x,bubble_y), pendown()
    setheading(0), begin_fill(), circle(-radius), end_fill()
    right(90), forward(radius), right(90), forward(radius/4)
    setheading(90), begin_fill(), circle((radius*.8)), end_fill()
    setheading(0), forward(radius/2)
    setheading(-90), begin_fill(), circle(radius*.8), end_fill()
    
    penup(), setheading(0), forward(radius/3), right(90), forward(radius),pendown()
    begin_fill(), circle(radius/8), end_fill()
    penup(), forward(radius/4), setheading(0), forward(radius/4), right(90),pendown()
    begin_fill(), circle(radius/16), end_fill()
    penup(), forward(radius/8), setheading(0), forward(radius/8), right(90),pendown()
    begin_fill(), circle(radius/32), end_fill()

# writes story text from specified dictionary(?) text box
def write_story(list_name, color):
    
    word_bubble(110,color)
    
    speed(1)
    y = 285 # INCOMPLETE - need to find correct coordinates
    line_height = 20

    pencolor('black')
    for item in list_name:
        penup()
        goto(bubble_x,y),
        pendown()
        write(item, align="center", font=("Arial", 10, "italic"))
        y -= line_height

# shows gif image for trip location and places it on turtle canvas
def place (location,x,y):
    screen = Screen()
    
    # Register shapes from the dictionary
    screen.addshape(Locations[location])

    # Create a turtle and set its shape to the registered GIF shape
    gif_turtle = Turtle()
    gif_turtle.shape(Locations[location])

    # Move the turtle around to see the GIF
    gif_turtle.penup()
    gif_turtle.goto(x,y)
    
def person (radius,gender):
    
    skin_colors = ['AntiqueWhite', 'chocolate4', 'LightSalmon', 'tan']
    hair_colors = ['SaddleBrown', 'black', 'red4', 'snow3', 'lemonchiffon', 'burlywood']
    shirt_colors = ['coral1', 'maroon4', 'CadetBlue', 'DarkSeaGreen', 'Lightgoldenrod1', 'LightPink']
    chosen_skin_color = random.choice(skin_colors)

    speed(0)
    pencolor(random.choice(shirt_colors))
    fillcolor(chosen_skin_color)
    begin_fill()
    forward(radius)
    left(90)
    forward(radius*1.5)
    circle(radius*1,180)
    forward(radius*1.5)
    left(90)
    forward(radius)
    end_fill()

    penup()
    left(90)
    forward(radius*2.75)
    right(90)
    pendown()

    pencolor(random.choice(skin_colors))
    fillcolor(random.choice(skin_colors))
    begin_fill()
    circle(radius*.75)
    end_fill()

    penup()
    setheading(180)
    forward(radius*.75)
    right(90)
    forward(radius*.6)
    pendown()
    fillcolor(random.choice(hair_colors))

    if gender == 'male':
        pencolor(random.choice(hair_colors))
        begin_fill()
        forward(radius*.9)
        circle(-(radius*.25),90)
        forward(radius)
        circle(-(radius*.25),90)
        forward(radius*.9)
        right(190)
        circle((radius*.75),180)
        end_fill()

    elif gender == 'female':
        pencolor(random.choice(hair_colors))
        begin_fill()
        forward(radius*.2)
        circle(-(radius*.75),90)

        circle((radius*.25),45)    
        circle((radius*.25)/2,90)
        circle((radius*.25),90)
        circle((radius*.25)/2,90)
        circle((radius*.25),45) 

        
        setheading(0)
        circle(-(radius*.75),90)
        forward(radius*.2)
        right(180)
        circle((radius*.75),180)
        end_fill()
    
    else:
        pencolor(random.choice(hair_colors))
        begin_fill()
        forward(radius*.15)
        circle(-(radius*.75),180)
        forward(radius*.75)
        right(90)
        forward(radius*.75)
        right(180)
        circle(radius*.75,135)
        setheading(180)

        forward(radius*1.01)
        left(45)
        circle(radius*.75,135)
        setheading(180)
        forward(radius*.75)
        right(90)
        forward(radius*.75)
        end_fill()

    pendown()


# Introduction
formatting()
write_story(introduction_lines, 'gray')
time.sleep(5)
write_story(going_away, 'gray')

# User selection - Solo, couples, girls or family trip
start = textinput("Help Taylor plan their vacation!","Should Taylor go on vacation: \n1. alone. \n2. with her partner. \n3. with her girls. \n4. with her kids.  \nEnter your choice:")

penup()
goto(0,0)
setheading(0)
pendown()

if int(start) == 1: 
    person(25,'female')

elif int(start) == 2: #'2' or 'partner' in start.lower():
    penup()
    back(25)
    pendown()
    person(25,'female')
    penup()
    forward(75)
    pendown()
    person(25,'male')


elif int(start) == 3: #'3' or 'girls' in start.lower():
    penup()
    back(75*2.5)
    pendown()
    for i in range(5):
        person(25,'female')
        penup()
        forward(75)
        pendown()
 
elif int(start) == 4: #'4' or 'kids' in start.lower():
    penup()
    back(25)
    pendown()
    person(25,'female')
    penup()
    forward(75)
    pendown()
    person(25,'male')
    penup()
    goto(-60,-25)
    pendown()
    person(20, 'male')
    penup()
    forward(60)
    pendown()
    person(20, 'other')
    penup()
    forward(60)
    pendown()
    person(20, 'female')

else:
    write_story(invalid_entry, 'gray')

        



done()