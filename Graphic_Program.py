import random
from turtle import *
#from graphic_functions import *
#from storyline_dictionaries_with_lists import *
#from other_dictionaries_and_lists import *
#from solo_module import *
#from couples_module import *
#from girls_module import *

bubble_x = -280
bubble_y = 375

#################################### SETUP FUNCTIONS ####################################

# Configure turtle
def formatting():
    title("Taylor's Vacation")
    setup(height=800, width=1000)
    hideturtle()
    speed(0)

#################################### WRITE STORY ####################################

# Draws word bubble
def word_bubble(radius, color):

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


def write_story(list_name, size):

    y = 0 # INCOMPLETE - need to find correct coordinates
    line_height = size*2

    pencolor('')
    for item in list_name:
        penup()
        goto(bubble_x,y),
        pendown()
        write(item, align="center", font=("Arial", size, "italic"))
        y -= line_height


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


Misc_Storyline = {
    
    "title" : ["Welcome to Taylor's Surprise","VACATION!"],

    "directions" : ["When prompted, enter numerical values only,",
        "type 'exit' to leave."],

    "introduction" : ["On Sunday night Taylor's phone pings with an urgent email.",
        "As Taylor reads, her jaw drops in surprise.",
        "There is a major network failure at work that will take all week to fix,",
        "All staff have been given the week off.",
        "Taylor is over the moon,",
        "she has been wanting to go on vacation for months.",
        "This week off is her chance,",
        "Taylor needs your help to plan her last minute trip."],

    "Invalid_Entry": [
        "Invalid entry, please enter a numeric",
        "value or type 'Exit' to end the program"],

    "Exit": [
        "Bon voyage Tay Tay!",
        "Exiting..."],

    "Ending": [
        "Either way,",
        "it's time to get back to work!"]
}

Level_1_Storyline = {
    "Level_1_Introduction": [
        "Taylor loves the idea of going with her family",
        "but she also LOVES the idea of travelling alone or with her girlfriends"
    ],
    
    "Level_1_Option": [
        "Should Taylor go on vacation:",
        "1. alone",
        "2. with her partner",
        "3. with her girls",
        "4. with her kids",
        "Enter your choice:"
    ],

    "Level_1_Solo_Option_Response": [
        "Excellent!",
        "Taylor is in need of some self care time",
        "she thinks to herself...",
        "'Should I commit to a BIG trip and go international",
        "or will staying domestic feel like a getaway?'"
    ],

    "Level_1_Couples_Option_Response": [
        "My husband and I never even went on a honeymoon,",
        "it's definitely time for some time together.",
        "Taylor wonders thinks 'I could book the tickets",
        "and surprise him tonight but...",
        "would he prefer romance or adventure?'"
    ],

    "Level_1_Girls_Option_Response": [
        "Yesssssssss!",
        "I am calling my girls right now!"
    ],

    "Level_1_Kids_Option_Response": [
        "Hmmmm, okay...Taylor can pull this off,",
        "travelling with two toddlers last minute - NO BIG DEAL!"
    ]
}

Level_2_Solo_Storyline = {
    "Level_2_Domestic/International_Option": [
        "Should Taylor go:",
        "1. domestic",
        "2. international",
        "Enter your choice:"
    ],

    "Level_2_Domestic_Response": [
        "This is going to take some though",
        "Taylor is thinking something simple, sunny and calm.",
        "Outer Banks, North Carolina!"
    ],

    "Level_2_International_Response": [
        "Without a moments hesitation, Taylor yells",
        "'I'm going to Japan!'"
    ],

    "Level_2_Domestic_Travel": [
        "Taylor's flight arrived in North Carolina on time",
        "and she headed to the small beach house to relax.",
        "Several days flew past while Taylor read books,",
        "cooked and walked on the beach."
    ],

    "Level_2_International_Travel": [
        "Taylor's flight was long and economy was crowded",
        "but she was immediately energized upon arrival.",
        "Tokyo was buzzing with life and the smell of the",
        "best food in the world!"
    ]
}

Level_2_Couples_Storyline = {
    "Level_2_Romantic/Adventure_Option": [
        "Should Taylor plan a trip that is:",
        "1. Romantic",
        "2. Adventurous",
        "Enter your choice:"
    ],

    "Level_2_Romantic_Response": [
        "A wine country getaway would be perfect.",
        "Taylor and her partner book a trip to Sanoma."
    ],

    "Level_2_Adventure_Response": [
        "Capetown has always been on their bucketlist,",
        "it is nerve racking and exciting.",
        "They book their flight for 6am the next day"
    ],

    "Level_2_Romantic_Travel": [
        "They splurge on first class and cheers as",
        "with a glass of champagne as they lift off."
    ],
    
    "Level_2_Adventure_Travel": [
        "The flight goes well arrives on time,",
        "let the adventure begin!"
    ]
}

Level_2_Girls_storyline = {
    "Level_2_serene/wild_option": [
        "Should the girls go:",
        "1. serene",
        "2. wild",
        "Enter your choice:"
    ],

    "Level_2_serene_response": [],
    "Level_2_wild_response": [],
    "Level_2_serene_travel": [],
    "Level_2_wild_travel": []
}

Level_2_Kids_Storyline = {
    "sure": [
        "Are you sure?",
        "There will be a lot to do..."
    ],
    "time": [
        "Taylor doesn't have time for that.",
        "Pick again:"
    ]
}

Weather_API_storyline = {
    "day five": [
        "Five days into the trip,",
        "Taylor faces the fact that her trip is coming to an end.",
        "It's time to plan one last vacation hoorah."
    ],
    
    "good": [
        "The weather forecast looks great for tomorrow!"
    ],

    "bad": [
        "A storm is forming...",
        "it will be bad weather for the rest of the trip.",
        "'Noooo!'"
    ],

    "failed": [
        "'oh, that's weird' Taylors says,",
        "The local weather channel is offline",
        "'I'll have to take my chances and hope for the best!'"
    ]
}

Level_3_solo_domestic__Activity_storyline = {

    "Level_3_Solo_Domestic_Good_Weather_Option": [
        "Taylor wakes up to a perfect sunny day.",
        "Should she go:",
        "1. to the beach",
        "2. dune surfing",
        "Enter your choice:"
    ],

    "Level_3_Solo_Domestic_Beach_Day_Response": [
        "Taylor spends the day soaking up the sun,",
        "building sandcastles, and playing beach volleyball."
    ],

    "Level_3_Solo_Domestic_Dune_Surfing_Response": [
        "Feeling adventurous, Taylor decides to try dune surfing.",
        "It's thrilling and leaves her feeling exhilarated!"
    ],
    
    "Level_3_Solo_Domestic_Bad_Weather_Response": [
        "It's raining outside,",
        "but Taylor won't let that dampen her spirits.",
        "She spends the day exploring the Wright museum."
    ]
}

Level_3_solo_international_storyline ={

    "Level_3_Solo_International_Good_Weather_Option": [
        "The weather in Japan is perfect,",
        "should Taylor:",
        "1. climb Mt, Fuji",
        "2. go on a Mario Kart race around Tokyo",
        "Enter your choice:"
    ],

    "Level_3_Solo_International_Mt_Fuji_Response": [
        "The view from the top of Mt. Fuji is breathtaking.",
        "Taylor feels like she's on top of the world!"
    ],

    "Level_3_Solo_International_Mario_Kart_Response": [
        "Taylor channels her inner Mario Kart racer",
        "dresses up as donkey kong",
        "and explores Tokyo on a go-kart tour."
    ],

    
    "Level_3_Solo_International_Bad_Weather_Option": [
        "It's raining cats and dogs in Tokyo,",
        "but Taylor won't let that ruin her day.",
        "Should she:",
        "1. eat all day",
        "2. go to a sumo match"
    ],

    "Level_3_Solo_International_Food_Tourism_Response": [
        "Taylor indulges in sushi, ramen, and tempura,",
        "discovering new flavors at every stop."
    ],

    "Level_3_Solo_International_Sumo_Wrestling_Response": [
        "Taylor attends a traditional sumo wrestling match",
        "and cheers on the competitors with the locals."
    ]
}

Level_3_couples_romantic_storyline = {
    
    "Level_3_Couples_Romantic_Good_Weather_Response": [
        "The weather in Sonoma is perfect for wine tasting.",
        "Taylor and her partner spend the day exploring vineyards",
        "and enjoying each other's company in the picturesque countryside."
    ],

    "Level_3_Couples_Romantic_Bad_Weather_Response": [
        "It's raining in Sonoma, but Taylor and her partner",
        "still go to the winery anyways!"
    ]
}

Level_3_couples_adventure_storyline = {
    
    "Level_3_Couples_Adventure_Good_Weather_Option": [
        "The weather in Cape Town is perfect for outdoor adventures.",
        "Taylor and her partner have a choice to make.",
        "Should they go:",
        "1. go shark diving",
        "2. on a safari",
        "Enter your choice:"
    ],

    "Level_3_Couples_Adventure_Shark_Diving_Response:" : [
        "Face to face with sharks, Taylor and her partner",
        "feel an adrenaline rush like never before!",
        "but...they would be happy to",
        "NEVER DO THAT AGAIN!"
    ],

    "Level_3_Couples_Adventure_Safari_Response": [
        "Spotting lions, elephants, and giraffes in the wild",
        "it was the most magical day!"
    ],

    
    "Level_3_Couples_Adventure_Bad_Weather_Response": [
        "It's stormy in Cape Town, but Taylor and her partner",
        "embrace the adventure and decide to either:",
        "1. go shark diving",
        "2. go on a safari",
        "Enter your choice:"
    ]
}

Level_3_girls_serene_storyline = {
    
    "Level_3_girls_serene_weather_response" : [
        "The weather doesn't matter -",
        "we are going to the spa!"
    ],

    "Level_3_girls_serene_activity_option" : [
        "Should the girls go cheap or opt for abouji spa?",
        "1. Cheap",
        "2. Expensive",
        "Enter your choice:"
    ],

    "Level_3_girls_serene_cheap_response" : [
        "Opting for a cheap spa,",
        "the girls find themselves feeling not so relaxed.",
        "There was mold in the showers and",
        "the masseuse was creepy."
    ],

    "Level_3_girls_serene_expensive_response" : [
        "Choosing an expensive spa, the girls",
        "indulge in a luxury complete with massages,",
        "facials, and champagne."
    ]
}

Level_3_girls_wild_storyline = {

    "Level_3_girls_wild_good_weather_option" : [
        "The weather is perfect for a stroll outside.",
        "Should the girls visit old or new Vegas?",
        "1. Old Vegas",
        "2. New Vegas",
        "Enter your choice:"
    ],

    "Level_3_girls_wild_old_vegas_response" : [
        "'ewwwwwwwwwwww!",
        "I've seen so many things...!'",
        "Taylor thinks 'It was still kinda fun to",
        "see the old casinos on Freemont street"
    ],

    "Level_3_girls_wild_new_vegas_response" : [
        "Choosing new Vegas, the girls experience",
        "the glitz and glamour while partying",
        "their way down the strip"
    ],

    "Level_3_girls_wild_bad_weather_option" : [
        "The weather is not ideal for outdoor adventures.",
        "Should the girls hit the casinos or catch a show?",
        "1. Casinos",
        "2. Show",
        "Enter your choice:"
    ],

    "Level_3_girls_wild_bad_weather_casino_response" : [
        "Opting for the casinos, the girls enjoy",
        "cocktails at the bars.",
        "before spending way too much",
        "money at the tables."
    ],

    "Level_3_girls_wild_bad_weather_show_response" : [
        "Choosing a show, Taylor and her friends",
        "decide to see Absinthe at Ceasars Palace.",
        "It was sooo funny!"
    ]
}

Flight_Quality_Randomizer = {

    "Perfect_Upgrade": [
        "Taylor lucks out with a perfect upgrade to first class.",
        "The extra legroom and gourmet meals make the flight",
        "a luxurious experience!"
    ],

    "Nightmare": [
        "Taylor's flight turns into a nightmare,",
        "with delays, turbulence, and lost luggage.",
        "It's a journey she'd rather forget!"
    ],

    "Just_Fine": [
        "The flight goes smoothly,",
        "with no major issues or surprises.",
        "It's just fine, nothing more, nothing less."
    ],

    "Pretty_Good": [
        "Taylor's flight is pretty good,",
        "with friendly staff, decent meals, and on-time arrival.",
        "It's a comfortable journey overall."
    ]
}

Level_4_storyline = {

    "Outcome_Option": [
        "Home at last.",
        "How did Taylor's vacation leave her feeling?",
        "1. Relaxed and reenergized",
        "2. Exhausted and stressed",
        "Enter your choice:"
    ],

    "Relaxed_and_Reenergized_Response": [
        "Taylor returns home feeling relaxed,",
        "reenergized, and ready to take on whatever",
        "challenges come her way.",
        "It was the perfect getaway!"
    ],

    "Exhausted_and_Stressed_Response": [
        "Taylor's vacation left her feeling exhausted",
        "and stressed out. It's going to take some time",
        "to recover from this trip gone wrong..."
    ]
}

write_story(Misc_Storyline["title"],10)

done()