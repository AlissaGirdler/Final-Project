import random
from Archive.storyline_dictionaries import *


def couples_trip():

    choice = input(Level_2_Couples_Storyline["Level_2_Romantic/Adventure_Option"])

    if choice == "1":
        domestic_couple()
    elif choice == "2":
        international_couple()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        couples_trip()

def domestic_couple():
    print(Level_2_Couples_Storyline["Level_2_Romantic_Response"])
    print(Level_2_Couples_Storyline["Level_2_Romantic_Travel"])
    # Generate random weather (good or bad)
    # What is the best way to incorporate the weather API into this?
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print(Level_3_couples_romantic_storyline["Level_3_Couples_Romantic_Good_Weather_Response"])
       
    else:
       print(Level_3_couples_romantic_storyline["Level_3_Couples_Romantic_Bad_Weather_Response"])


def international_couple():
    print(Level_2_Couples_Storyline["Level_2_Adventure_Response"])
    print(Level_2_Couples_Storyline["Level_2_Adventure_Travel"])
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        sharkcage_safari = input(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Good_Weather_Option"])

        if sharkcage_safari == "1":
            print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Shark_Diving_Response"])
        elif sharkcage_safari == "2":
            print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Safari_Response"])
        else:
             print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    
    else:
        print(Level_3_couples_adventure_storyline["Level_3_Couples_Adventure_Bad_Weather_Response"])


