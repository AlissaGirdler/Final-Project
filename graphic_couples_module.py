import sys
import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *


def couples_trip():
    blank_page()
    penup(), goto(0,0), pendown(), setheading(0)
    couple()
    word_bubble(110,'IndianRed4')
    write_story(Level_1_Storyline,"Level_1_Couples_Option_Response",12,-280,325,'white')


    choice = textinput("User Input",Level_2_Couples_Storyline["Level_2_Romantic/Adventure_Option"])

    if choice == "1":
        domestic_couple()

    elif choice == "2":
        international_couple()

    elif choice == "Exit":
        write_story(Misc_Storyline,"Exit",12,-280,280)
        sys.exit()
    
    else:
        write_story(Misc_Storyline,"invalid_entry",12,-280,280)
        couples_trip() # PUNCH LIST add while true loop



def domestic_couple():

    word_bubble(110,'IndianRed4')
    write_story(Level_2_Solo_Storyline,"Level_2_Romantic_Response",12,-280,280,'white')
    time.sleep(3)
    blank_page()

    place("Sanoma",300,-250)
    time.sleep(2)
    place('Madison',-300,-250)


    flight(300,'IndianRed4')
    time.sleep(3)

    word_bubble(110,'IndianRed4')
    write_story(Level_2_Solo_Storyline,"Level_2_Romantic_Travel",12,-280,280, 'white')
    
    blank_page()

    random_weather = random.choice(weather)
    
    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)
        blank_page()

        word_bubble(110,'IndianRed4')
        write_story(Level_3_couples_romantic_storyline,"Level_3_Couples_Romantic_Good_Weather_Response",12,-280,280, 'white')
        activity("Wine Sun",50,-50)

    else:
        if random_weather == "cloudy":

            cloudy()
            time.sleep(3)
            blank_page()

            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_romantic_storyline,"Level_3_Couples_Romantic_Bad_Weather_Response",12,-280,280, 'white')
            activity("Wine Rain",50,-50)

        elif random_weather == 'rainy':

            rain()
            time.sleep(3)
            blank_page()

            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_romantic_storyline,"Level_3_Couples_Romantic_Bad_Weather_Response",12,-280,280, 'white')
            activity("Wine Rain",50,-50)


# def international_couple():
#     print(Level_2_Couples_Storyline["Level_2_Adventure_Response"])
#     print(Level_2_Couples_Storyline["Level_2_Adventure_Travel"])
#     # Generate random weather (good or bad)
#     weather = random.choice(["good", "bad"])

#     if weather == "good":
#         sharkcage_safari = input(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Good_Weather_Option"])

#         if sharkcage_safari == "1":
#             print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Shark_Diving_Response"])
#         elif sharkcage_safari == "2":
#             print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Safari_Response"])
#         else:
#              print("Invalid choice. Please enter either 1 or 2.")
#             # Repeat the decision point
    
#     else:
#         print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Bad_Weather_Response"])

