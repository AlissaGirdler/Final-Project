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
    write_story(Level_1_Storyline,"Level_1_Couples_Option_Response",12,-280,315,'white')


    choice = textinput("User Input",Level_2_Couples_Storyline["Level_2_Romantic/Adventure_Option"])

    if choice == "1":
        domestic_couple()

    elif choice == "2":
       international_couple()

    elif choice == "Exit":
        word_bubble(110,'IndianRed4')
        write_story(Misc_Storyline,"Exit",12,-280,280,'white')
        sys.exit()
    
    else:
        word_bubble(110,'IndianRed4')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
        couples_trip() # PUNCH LIST add while true loop




def domestic_couple():

    word_bubble(110,'IndianRed4')
    write_story(Level_2_Couples_Storyline,"Level_2_Romantic_Response",12,-280,280,'white')
    time.sleep(3)
    blank_page()

    place("Sanoma",300,-250)
    time.sleep(2)
    place('Madison',-300,-250)


    flight(300,'IndianRed4')
    time.sleep(3)

    word_bubble(110,'IndianRed4')
    write_story(Level_2_Couples_Storyline,"Level_2_Romantic_Travel",12,-280,280, 'white')
    
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
    time.sleep(3)
    blank_page()


def international_couple():
    word_bubble(110,'IndianRed4')
    write_story(Level_2_Couples_Storyline,"Level_2_Adventure_Response",12,-280,280, 'white')

    blank_page()
    place('South Africa',300,-250)
    time.sleep(3)
    place('Madison',-300,-250)
    time.sleep(3)

    flight(300,'IndianRed4')
    time.sleep(3)

    word_bubble(110,'IndianRed4')
    write_story(Level_2_Couples_Storyline,"Level_2_Adventure_Travel",12,-280,280, 'white')


    random_weather = random.choice(weather)

    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)

        sharkcage_safari = textinput("User Input",Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Good_Weather_Option"])

        blank_page()

        if sharkcage_safari == "1":
            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Shark_Diving_Response",12,-280,280, 'white')
            activity('Cage Shark',50,-50)
        
        
        elif sharkcage_safari == "2":
            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Safari_Response",12,-280,280, 'white')
            activity('Safari',50,-50)


        elif sharkcage_safari == "Exit":

            word_bubble(110,'IndianRed4')
            write_story(Misc_Storyline,"Exit",12,-280,280,'white')
            sys.exit()
            
        else:
            word_bubble(110,'IndianRed4')
            write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')
    
    else:

        if random_weather == "cloudy":

            cloudy()
            time.sleep(3)

            word_bubble(110,'white')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Bad_Weather_Response",12,-280,280, 'Azure4')



        elif random_weather == "rainy":

            cloudy()
            time.sleep(3)

            word_bubble(110,'white')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Bad_Weather_Response",12,-280,280, 'Azure4')
        
        sharkcage_safari = textinput("User Input",Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Bad_Weather_Option"])

        blank_page()

        if sharkcage_safari == "1":
            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Shark_Diving_Response",12,-280,280, 'white') # PUNCH LIST HELP
            activity('Cage Shark',50,-50)


        elif sharkcage_safari == "2":
            word_bubble(110,'IndianRed4')
            write_story(Level_3_couples_adventure_storyline,"Level_3_Couples_Adventure_Safari_Response",12,-280,280, 'white')
            activity('Safari',50,-50)


        elif sharkcage_safari == "Exit":

            word_bubble(110,'IndianRed4')
            write_story(Misc_Storyline,"Exit",12,-280,280,'white')
            sys.exit()

        else:
            word_bubble(110,'IndianRed4')
            write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')

