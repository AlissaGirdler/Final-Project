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
    for location, file_path in Locations.items():
        screen.addshape(file_path)

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

    speed(0)
    pencolor(random.choice(shirt_colors))
    fillcolor(random.choice(shirt_colors))
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


##################   DICTIONARIES AND LISTS   ##################

travel_checklist = [
    "Pack enough snacks to feed a small army.",
    "Double-check that you've packed all favorite stuffed animals.",
    "Download several episodes of their favorite shows onto the tablet.",
    "Charge all electronic devices and pack chargers.",
    "Stock up on motion sickness medication, just in case.",
    "Check the weather forecast for your destination.",
    "Pack extra changes of clothes for spills and accidents.",
    "Make sure you have enough diapers and wipes.",
    "Confirm hotel reservations and check-in times.",
    "Print out copies of important documents like passports and itineraries.",
    "Prepare a travel first aid kit.",
    "Pack sunscreen and hats for sunny destinations.",
    "Make a checklist of essential items and go through it twice.",
    "Load up on car snacks for the journey.",
    "Install and test the car seat if you're driving.",
    "Plan rest stops for long road trips.",
    "Pack a portable potty if your kids are still in training.",
    "Notify credit card companies of your travel plans.",
    "Put together a playlist of kid-friendly songs for the car.",
    "Set up automatic bill payments for while you're away.",
    "Notify neighbors or friends to keep an eye on your home.",
    "Confirm pet care arrangements if you have pets.",
    "Pack favorite bedtime stories for nighttime routines.",
    "Pack plenty of entertainment for the airplane.",
    "Check luggage weight limits and airline regulations.",
    "Prepare for potential delays and layovers.",
    "Pack a travel-sized pillow or blanket for comfort.",
    "Don't forget favorite snacks and drinks for the flight.",
    "Pack a small surprise gift for each child to unwrap during the trip.",
    "Load up on hand sanitizer and disinfecting wipes.",
    "Plan activities for downtime during travel.",
    "Download travel apps for navigation and entertainment.",
    "Pack travel games and toys to keep kids occupied.",
    "Check for any travel advisories or warnings.",
    "Pack an extra set of car keys.",
    "Set up out-of-office replies for work emails.",
    "Confirm arrangements for transportation at your destination.",
    "Make sure you have enough cash in local currency.",
    "Pack a small, collapsible stroller for sightseeing.",
    "Bring a portable phone charger for emergencies.",
    "Pack a nightlight for unfamiliar hotel rooms.",
    "Set up a designated meeting point in case anyone gets separated.",
    "Teach kids your phone number in case they get lost.",
    "Pack a small sewing kit for wardrobe malfunctions.",
    "Pack a small travel umbrella for unexpected rain.",
    "Double-check that all medications are packed.",
    "Pack a small cooler with drinks and snacks for the journey.",
    "Pack plastic bags for wet or dirty clothes.",
    "Pack a small travel laundry detergent in case of spills.",
    "Make sure everyone has comfortable shoes for walking.",
    "Pack hats and sunglasses for everyone.",
    "Bring a reusable water bottle for each person.",
    "Pack a small notebook and pen for jotting down memories.",
    "Pack a deck of cards for family game nights.",
    "Make copies of important documents and store them separately.",
    "Pack travel-sized toiletries for convenience.",
    "Load up on extra patience for the journey.",
    "Check for any travel restrictions or requirements.",
    "Pack a small sewing kit for wardrobe emergencies.",
    "Pack a small flashlight for exploring at night.",
    "Bring a travel-sized baby monitor for hotel rooms.",
    "Pack extra plastic bags for trash and dirty diapers.",
    "Bring a small toolkit for unexpected repairs.",
    "Pack a travel-sized bottle of dish soap for washing bottles.",
    "Bring a small, portable fan for hot destinations.",
    "Pack a travel-sized bottle of hand soap for hygiene.",
    "Bring a small, portable high chair for dining out.",
    "Pack a small, collapsible cooler for picnics.",
    "Bring a small, portable playpen for safe play.",
    "Pack a travel-sized bottle of baby shampoo and wash.",
    "Bring a small, portable baby carrier for outings.",
    "Pack a travel-sized bottle of baby lotion and diaper cream.",
    "Bring a small, portable baby bathtub for bathing.",
    "Pack a travel-sized bottle of baby sunscreen.",
    "Bring a small, portable baby feeding set.",
    "Pack a travel-sized bottle of baby insect repellent.",
    "Bring a small, portable baby blanket for comfort.",
    "Pack a travel-sized bottle of baby laundry detergent.",
    "Bring a small, portable baby toy for entertainment.",
    "Pack a travel-sized bottle of baby oral care products.",
    "Bring a small, portable baby teething toy.",
    "Pack a travel-sized bottle of baby medicine.",
    "Bring a small, portable baby pacifier.",
    "Pack a travel-sized bottle of baby food.",
    "Bring a small, portable baby bib.",
    "Pack a travel-sized bottle of baby wipes.",
    "Bring a small, portable baby bottle and warmer.",
    "Pack a travel-sized bottle of baby hand sanitizer.",
    "Bring a small, portable baby burp cloth.",
    "Pack a travel-sized bottle of baby diaper rash cream.",
    "Bring a small, portable baby nursing cover.",
    "Pack a travel-sized bottle of baby nail clippers.",
    "Bring a small, portable baby thermometer.",
    "Pack a travel-sized bottle of baby gas relief drops.",
    "Bring a small, portable baby nasal aspirator.",
    "Pack a travel-sized bottle of baby hairbrush and comb.",
    "Bring a small, portable baby bath sponge.",
    "Finally, take a deep breath and remind yourself that the chaos is part of the adventure!"
]

introduction_lines = [
    "On Sunday night Taylor's phone pings with an urgent email.",
    "As Taylor reads, their jaw drops in surprise.",
    "There is a major network failure at work that will take all week to fix,",
    "All staff have been given the week off."
    ]

going_away = ["Taylor is over the moon,",
              "she has been wanting to go on vacation for months.",
              "This week off is her chance,",
              "Taylor needs your help to plan her last minute trip."
]

invalid_entry = ["That is an invalid entry,",
                 "please try again."]

Locations = {
    "Madison": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/7.gif",
    "Outer Banks": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/1.gif",
    "Tokyo": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/2.gif",
    "Sanoma": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/3.gif",
    "South Africa": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/4.gif",
    "Lake Geneva": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/5.gif",
    "Las Vegas": "C:/Users/aliss/OneDrive/Desktop/LIS 875/Final-Project/Location Photos/6.gif",
}



##################   PROGRAM START   ##################

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

if '1' or 'alone' in start.lower():
    person(25,'female')

elif '2' or 'partner' in start.lower():
    penup()
    back(25)
    pendown()
    person(25,'female')
    penup()
    forward(75)
    pendown()
    person(25,'male')


elif '3' or 'girls' in start.lower():
    penup()
    back(75*2.5)
    pendown()
    for i in range(5):
        person(25,'female')
        penup()
        forward(75)
        pendown()
 
elif '4' or 'kids' in start.lower():
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