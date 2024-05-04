from turtle import *
import math
import random
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *
import time

bubble_x = -280
bubble_y = 375

#################################### SETUP FUNCTIONS ####################################

# Configure turtle
def formatting():
    title("Taylor's Vacation")
    setup(height=800, width=1000)
    hideturtle()
    speed(0)

##################################### WRITE STORY ####################################

# Draws word bubble
def word_bubble(radius, color):

    bubble_x = -280
    bubble_y = 375

    speed(0); pencolor(color); fillcolor(color); penup(); goto(bubble_x,bubble_y); pendown()
    setheading(0); begin_fill(); circle(-radius); end_fill()
    right(90); forward(radius); right(90); forward(radius/4)
    setheading(90); begin_fill(); circle((radius*.8)); end_fill()
    setheading(0); forward(radius/2)
    setheading(-90); begin_fill(); circle(radius*.8); end_fill()
    
    penup(); setheading(0); forward(radius/3); right(90); forward(radius);pendown()
    begin_fill(); circle(radius/8); end_fill()
    penup(); forward(radius/4); setheading(0); forward(radius/4); right(90);pendown()
    begin_fill(); circle(radius/16); end_fill()
    penup(); forward(radius/8); setheading(0); forward(radius/8); right(90);pendown()
    begin_fill(); circle(radius/32); end_fill()


def write_story(story_dict, key, size, x, y):
    line_height = size * 2

    for item in story_dict[key]:
        penup()
        goto(x, y)
        pendown()
        write(item, align="center", font=("Arial", size, "italic"))
        y -= line_height
        time.sleep(1)

write_story(Misc_Storyline,"title",20,0,0)
time.sleep(2)
write_story(Misc_Storyline,"directions",12,0,-30)
time.sleep(2)
clear()
write_story(Misc_Storyline,"introduction",15,0,100)

#################################### TRAVEL FUNCTIONS ####################################

# Draws airplane traveling a flight path with parameters for size and plane color
def flight(radius, color):

    #defines variables used in flight function
    size = radius/5
    distance = 2*math.pi*radius/360

    #sets color and formatting
    speed(3)
    pencolor(color)
    fillcolor(color)
    
    #angels flight path
    left(30)
    speed(3)
    width(3)
    pencolor('gray')

    for i in range(5):
        pendown()
        forward(distance*2)
        penup()
        right(1)
        forward(distance*2)
        right(1)

    current_position = pos()
    set_heading = heading()
    speed(0)

    #draws airplane body
    begin_fill()
    setheading(set_heading)
    right(90)
    forward(size/20)
    left(88)
    forward(size)
    circle((size/2.5),40)
    goto(current_position)
    setheading(set_heading)
    left(90)
    forward(size/20)
    right(88)
    forward(size)
    circle(-(size/2.5),40)
    end_fill()

    #draw right tail
    begin_fill()
    goto(current_position)
    setheading(set_heading)
    right(110)
    forward(size/5)
    left(95)
    forward(size/20)
    left(75)
    forward(size/4)
    end_fill()

    #draw left tail
    begin_fill()
    goto(current_position)
    setheading(set_heading)
    left(110)
    forward(size/5)
    right(95)
    forward(size/20)
    right(75)
    forward(size/4)
    end_fill()

    #draw right wing
    begin_fill()
    goto(current_position)
    setheading(set_heading)
    forward(size/1.6)
    left(110)
    forward(size/1.66)
    right(95)
    forward(size/20)
    right(75)
    forward(size/1.33)
    end_fill()

   #draw right wing 
    begin_fill()
    goto(current_position)
    setheading(set_heading)
    forward(size/1.6)
    right(110)
    forward(size/1.66)
    left(95)
    forward(size/20)
    left(75)
    forward(size/1.33)
    end_fill()

    #draws remaining flight path
    goto(current_position)
    setheading(set_heading)
    forward(size+(size/2.5))
    right(10)
    speed(3)
    width(3)
    pencolor('gray')

    for i in range(22):
        pendown()
        forward(distance*2)
        penup()
        right(1)
        forward(distance*2)
        right(1)

    setheading(0)

# IN PROGRESS Car drive
def road_trip(length):
    
    for i in range((length // 6) // 2):
        forward(4)
        penup()
        forward(2)
        pendown()
    
    # tires only
    penup()
    forward((length/10)/10)
    pendown()
    pencolor('black')
    width((length/10)/11)
    circle((length/10)/10)
    penup()
    forward(((length/10)/10)*8)
    pendown()
    circle((length/10)/10)
    
    width(1)
    pencolor('red')
    penup()
    forward((length/10)/10)
    left(90)
    forward((length/10)/10)
    right(90)
    pendown()
    fillcolor('red')
    begin_fill()
    forward((length/10)/10)
    left(90)
    forward(((length/10)/10)*2)
    left(90)
    forward(((length/10)/10)*2)
    right(90)
    circle(((length/10)/10)*6)
    right(90)
    forward(((length/10)/10)*2)
    left(90)
    forward(((length/10)/10)*2)
    left(90)
    forward((length/10))
    end_fill()

    width(1)
    for i in range((length // 6) // 2):
        forward(4)
        penup()
        forward(2)
        pendown()


#################################### WEATHER FUNCTIONS ####################################

# Draw cloud
def cloud (size, cloud_color):
    speed(0)
    pencolor(cloud_color)
    fillcolor(cloud_color) 
    begin_fill()   
    for i in range(2):
        forward(size)
        left(90)
        forward(int(size/6))
        left(90)
    end_fill()

    begin_fill(), circle(random.randint(int(size/6), int(size/4))), end_fill()
    forward(int(size))
    begin_fill(), circle(random.randint(int(size/6), int(size/4))), end_fill()
    back(random.randint(int(size/2), int(size/1.2)))
    begin_fill(), circle(random.randint(int(size/4), int(size/3))), end_fill()
    forward(random.randint(int(size/4), int(size/2)))
    begin_fill(), circle (random.randint(int(size/4), int(size/3))), end_fill()
    end_fill()

# Draws an entire cloudy sky
def cloudy_sky():
    bgcolor('gray')
    for i in range(random.randint(10,20)):
        penup()
        goto(random.randint(-300,250),random.randint(-200,300))
        pendown()
        cloud(random.randint(25,100),'white')

# Draw raindrop
def raindrop ():    
    
    blues = ['lightblue','lightblue2','lightblue3','lightblue4']

    right(90)
    pencolor('gray')
    color(random.choice(blues))
    begin_fill()
    circle(25, 180)
    left(25)
    forward(60)
    left(130)
    forward(60)       
    end_fill()

# Draws an entire rainy sky
def rain():
    bgcolor('gray')
    for i in range(random.randint(50,75)):
        penup()
        goto(random.randint(-500,400),random.randint(-400,500))
        setheading(0)
        pendown()
        raindrop()

# Draw sun
def sun (size):
    center = position()
    set_heading = (0)

    penup()
    right(90)
    forward(size)
    left(90)
    pendown()
    fillcolor('lightgoldenrod2')
    width(5)
    pencolor('lightgoldenrod2')
    begin_fill()
    circle(size)
    end_fill()
    for i in range(36):
        penup()
        goto(center)
        setheading(set_heading)
        pendown()
        forward(size * 1.2)
        set_heading += 10

# Draw sunny sky
def sunny ():
    bgcolor('lightblue2')
    penup(), goto(200,200), pendown()
    sun(50)


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
    chosen_hair_color = random.choice(hair_colors)
    chosen_shirt_color = random.choice(shirt_colors)

    speed(0)
    pencolor(chosen_shirt_color)
    fillcolor(chosen_shirt_color)
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

    pencolor(chosen_skin_color)
    fillcolor(chosen_skin_color)
    begin_fill()
    circle(radius*.75)
    end_fill()

    penup()
    setheading(180)
    forward(radius*.75)
    right(90)
    forward(radius*.6)
    pendown()
    fillcolor(chosen_hair_color)

    if gender == 'male':
        pencolor(chosen_hair_color)
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
        pencolor(chosen_hair_color)
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
        pencolor(chosen_hair_color)
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

def to_do_list ():
    for _ in range(4):
        forward(10) 
        left(90)

    

done()