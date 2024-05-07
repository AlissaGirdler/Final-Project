import sys
import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *

def girls_getaway():
    blank_page()
    penup(), goto(0,0), pendown(), setheading(0)
    girls()
    word_bubble(110,'LightPink3')
    write_story(Level_1_Storyline,"Level_1_Girls_Option_Response",12,-280,315,'white')


    choice = textinput("User Input", Level_2_Girls_storyline["Level_2_serene/wild_option"])

    if choice == "1":
        serene_girls()

    elif choice == "2":
        wild_girls()

    elif choice == "Exit":
        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"Exit",12,-280,280,'white')
        sys.exit()
    
    else:
        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
        girls_getaway() # PUNCH LIST add while true loop

def serene_girls():

    word_bubble(110,'LightPink3')
    write_story(Level_2_Girls_storyline,"Level_2_serene_response",12,-280,280,'white')
    time.sleep(3)
    blank_page()

    place("Lake Geneva",300,-250)
    time.sleep(2)
    place('Madison',-300,-250)

    road_trip(600)
    time.sleep(3)

    word_bubble(110,'LightPink3')
    write_story(Level_2_Girls_storyline,"Level_2_serene_travel",12,-280,280,'white')

    blank_page()

    random_weather = random.choice(weather)

    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)
        blank_page()

        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')
    
    elif random_weather == "cloudy":
        
        cloudy()
        time.sleep(3)
        blank_page()

        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')

    elif random_weather == "rainy":
        
        rain()
        time.sleep(3)
        blank_page()

        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')
    
    experience = textinput("User Input",Level_3_girls_serene_storyline["Level_3_girls_serene_activity_option"])

    if experience == "1":
        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_cheap_response",12,-280,280, 'white')
        activity('Cheap Spa',50,-50)
       
    elif experience == "2":
        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_expensive_response",12,-280,280, 'white')
        activity('Expensive Spa',50,-50)

    elif experience == "Exit":
        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"Exit",12,-280,280,'white')
        sys.exit()
    
    else:
        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
        serene_girls() # PUNCH LIST add while true loop
    
    time.sleep(3)
    blank_page()

def wild_girls():

    word_bubble(110,'LightPink3')
    write_story(Level_2_Girls_storyline,"Level_2_wild_response",12,-280,280,'white')

    blank_page()
    place('Las Vegas',300,-250)
    time.sleep(3)
    place('Madison',-300,-250)
    time.sleep(3)

    flight(300,'LightPink3')
    time.sleep(3)

    word_bubble(110,'LightPink3')
    write_story(Level_2_Girls_storyline,"Level_2_wild_travel",12,-280,280,'white')

    random_weather = random.choice(weather)

    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)
        vegas_strip = textinput("User Input", Level_3_girls_wild_storyline["Level_3_girls_wild_good_weather_option"])

        blank_page()

        if vegas_strip == "1":
            word_bubble(110,'LightPink3')
            write_story(Level_3_girls_wild_storyline,"Level_3_girls_wild_old_vegas_response",12,-280,280,'white')
            activity('Old Strip',50,-50)

        elif vegas_strip == "2":
            word_bubble(110,'LightPink3')
            write_story(Level_3_girls_wild_storyline,"Level_3_girls_wild_new_vegas_response",12,-280,280,'white')
            activity('New Strip',50,-50)

        elif vegas_strip == "Exit":

            word_bubble(110,'LightPink3')
            write_story(Misc_Storyline,"Exit",12,-280,280,'white')
            sys.exit()

        else:
            word_bubble(110,'LightPink3')
            write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')


    else:
        if random_weather == "cloudy":

            cloudy()
            time.sleep(3)

        elif random_weather == "rainy":

            cloudy()
            time.sleep(3)
        
    casino_show = textinput("User Input", Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_option"])

    blank_page()

    if casino_show == "1":
        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_wild_storyline,"Level_3_girls_wild_bad_weather_casino_response",12,-280,280,'white')
        activity('Casino',50,-50)

    elif casino_show == "2":
        word_bubble(110,'LightPink3')
        write_story(Level_3_girls_wild_storyline,"Level_3_girls_wild_bad_weather_show_response",12,-280,280,'white')
        activity('Show',50,-50)

    elif casino_show == "Exit":

        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"Exit",12,-280,280,'white')
        sys.exit()

    else:
        word_bubble(110,'LightPink3')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
