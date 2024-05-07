import time
import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *
from graphic_introduction import *
from graphic_solo_module import *
from graphic_couples_module import *
from graphic_girls_module import *

bubble_x = -280
bubble_y = 375

formatting()

# INTRODUCTION
introduction()

# LEVEL 1 
write_story(Level_1_Storyline,"Level_1_Introduction", 20, 0, 20,'white')
while True:
    choice = textinput("User Input", Level_1_Storyline['Level_1_Option'])
    blank_page()
    
    # LEVELS 2 & 3
    if choice == "1":
        solo_adventure()
        break 

    elif choice == "2":
        couples_trip()
        break 

    elif choice == "3":
        girls_getaway()
        break

    elif choice == "4":
        word_bubble(110,'DarkSeaGreen')
        family()
        blank_page()
        write_story(Level_1_Storyline,"Level_1_Kids_Option_Response",12,-280,325,'white')
        time.sleep(3)
        notebook()
        write_story(Level_1_Storyline,"Level_1_Kids_Option_Response",12,-280,325,'white')

    elif choice == "Exit":
        word_bubble(110,'CadetBlue4')
        write_story(Misc_Storyline,"Exiting",12,-280,325,'white')
        sys.exit()
        
    else: 
        word_bubble(110,'CadetBlue4')
        write_story(Misc_Storyline,"invalid_entry",12,-280,280,'white')

    

# RETURN TRAVEL QUALITY
if choice == "3":
    
    random_drive = random.choice(list(Driving_Quality_Randomizer.keys()))

    # Use the randomly chosen key in the write_story function
    word_bubble(110,'CadetBlue4')
    write_story(story_dict=Driving_Quality_Randomizer, key=random_drive, size=12, x=-280, y=325, pen_color='white')

    blank_page()
    return_road_trip(600)
    place('Madison',-250,-200)

else: 
    random_flight = random.choice(list(Flight_Quality_Randomizer.keys()))

    # Use the randomly chosen key in the write_story function
    word_bubble(110,'CadetBlue4')
    write_story(story_dict=Flight_Quality_Randomizer, key=random_flight, size=12, x=-280, y=325, pen_color='white')

    blank_page()
    return_flight(400,'black')
    place('Madison',-300,-200)

# LEVEL 4
trip_outcome = textinput("User Input",Level_4_storyline,"Outcome_Option", 12, -280, 280, 'white')

red_page()
if trip_outcome == "1":
    write_story(Level_4_storyline,"Relaxed_and_Reenergized_Response", 20, 0, 50,"White")
    time.sleep(3)
    red_page()
elif trip_outcome == "2":
    write_story(Level_4_storyline,"Exhausted_and_Stressed_Response", 20, 0, 50,"White")
    time.sleep(3)
    red_page()   

# ENDING
write_story(Misc_Storyline,"Ending", 20, 0, 20,"White")
time.sleep(3)
blank_page()
place('UW',0,0)
penup(), goto(0,-300), pendown()
write("Thanks for playing, goodbye!", align="center", font=("Arial", 15, "italic"))
time.sleep(5)
sys.exit()

done()