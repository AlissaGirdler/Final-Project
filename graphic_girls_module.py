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


    choice = input(Level_2_Girls_storyline["Level_2_serene/wild_option"])

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

    word_bubble(110,'IndianRed4')
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

        word_bubble(110,'IndianRed4')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')
    
    elif random_weather == "cloudy":
        
        cloudy()
        time.sleep(3)
        blank_page()

        word_bubble(110,'IndianRed4')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')

    elif random_weather == "rainy":
        
        rain()
        time.sleep(3)
        blank_page()

        word_bubble(110,'IndianRed4')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_weather_response",12,-280,280, 'white')
    
    experience = textinput("User Input",Level_3_couples_romantic_storyline["Level_3_girls_serene_activity_option"])

    if experience == "1":
        word_bubble(110,'IndianRed4')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_cheap_response",12,-280,280, 'white')

       
    elif experience == "2":
        word_bubble(110,'IndianRed4')
        write_story(Level_3_girls_serene_storyline,"Level_3_girls_serene_expensive_response",12,-280,280, 'white')


    elif experience == "Exit":
        word_bubble(110,'IndianRed4')
        write_story(Misc_Storyline,"Exit",12,-280,280,'white')
        sys.exit()
    
    else:
        word_bubble(110,'IndianRed4')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
        serene_girls() # PUNCH LIST add while true loop

serene_girls()

# def wild_girls():
#     print(Level_2_Girls_storyline["Level_2_wild_response"])
#     print(Level_2_Girls_storyline["Level_2_wild_travel"])
#     # Generate random weather (good or bad)
#     weather = random.choice(["good", "bad"])

#     if weather == "good":
#         vegas_strip = input(Level_3_girls_wild_storyline["Level_3_girls_wild_good_weather_option"])

#         if vegas_strip == "1":
#             print(Level_3_girls_wild_storyline["Level_3_girls_wild_old_vegas_response"])
#         elif vegas_strip == "2":
#             print(Level_3_girls_wild_storyline["Level_3_girls_wild_new_vegas_response"])
#         else:
#              print("Invalid choice. Please enter either 1 or 2.")
#             # Repeat the decision point
    
#     else:
#         casino_show = input(Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_option"])
      
#         if casino_show == "1":
#             print (Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_casino_response"])
#         elif casino_show == "2":
#           print (Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_show_response"])