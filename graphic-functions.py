from turtle import *
import math
import random

setup(height=800, width=1000)
bgcolor('lightblue2')

#draws airplane traveling a flight path with parameters for size and plane color
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

#draws cloud with size and color parameters
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

#draws an entire cloudy sky to be used in weather generator
def cloudy_sky():
    bgcolor('gray')
    for i in range(random.randint(10,20)):
        penup()
        goto(random.randint(-300,250),random.randint(-200,300))
        pendown()
        cloud(random.randint(25,100),'white')

#car icon for local trips
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

#draw sun to be used in weather generator
def sun (size):
    
    speed(0)
    center = position()
    set_heading = (0)

    penup()
    right(90)
    forward(size)
    left(90)
    pendown()
    fillcolor('yellow')
    pencolor('yellow')
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

def person (radius):

    shirt_colors = ['blue']
    skin_colors = []
    hair_colors = []

    
    pencolor()
    fillcolor('red')
    begin_fill()
    forward(radius*1.1)
    left(90)
    forward(radius*1.5)
    circle(radius*1.1,180)
    forward(radius*1.5)
    left(90)
    forward(radius*1.1)
    end_fill()

    penup()
    left(90)
    forward(radius*2.75)
    right(90)
    pendown()

    pencolor('tan')
    fillcolor('tan')
    begin_fill()
    circle(radius*.75)
    end_fill()

    setposition(180)
    forward(radius)
    right(90)
    fillcolor('brown')
    begin_fill()
    forward(radius*1.1)
    right(90)
    forward(radius*2)
    right(90)
    forward(radius*1.1)
    right(190)
    circle(radius,180)
    end_fill()

def talloval(r):
    circle(r,45)    
    circle(r/2,90)
    circle(r,90)
    circle(r/2,90)
    circle(r,45) 


def person (radius,gender):
    speed(1)
    pencolor('red')
    fillcolor('red')
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

    pencolor('tan')
    fillcolor('tan')
    begin_fill()
    circle(radius*.75)
    end_fill()

    penup()
    setheading(180)
    forward(radius*.75)
    right(90)
    forward(radius*.6)
    pendown()
    fillcolor('brown')

    if gender == 'male':
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
        pencolor('black')
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



person(50, 'other')

done()