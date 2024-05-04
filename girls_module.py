import random
from storyline_dictionaries import *


def girls_getaway():


    choice = input(Level_2_Girls_storyline["Level_2_serene/wild_option"])

    if choice == "1":
        serene_girls()
    elif choice == "2":
        wild_girls()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        girls_getaway()

def serene_girls():
    print(Level_2_Girls_storyline["Level_2_serene_response"])
    print(Level_2_Girls_storyline["Level_2_serene_travel"])
    print(Level_3_girls_serene_storyline["Level_3_girls_serene_weather_response"])

    experience = input(Level_3_girls_serene_storyline["Level_3_girls_serene_activity_option"])

    if experience == "1":
        print(Level_3_girls_serene_storyline["Level_3_girls_serene_cheap_response"])
       
    elif experience == "2":
        print(Level_3_girls_serene_storyline["Level_3_girls_serene_expensive_response"])
    
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        # Repeat the decision point




def wild_girls():
    print(Level_2_Girls_storyline["Level_2_wild_response"])
    print(Level_2_Girls_storyline["Level_2_wild_travel"])
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        vegas_strip = input(Level_3_girls_wild_storyline["Level_3_girls_wild_good_weather_option"])

        if vegas_strip == "1":
            print(Level_3_girls_wild_storyline["Level_3_girls_wild_old_vegas_response"])
        elif vegas_strip == "2":
            print(Level_3_girls_wild_storyline["Level_3_girls_wild_new_vegas_response"])
        else:
             print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    
    else:
        casino_show = input(Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_option"])
      
        if casino_show == "1":
            print (Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_casino_response"])
        elif casino_show == "2":
          print (Level_3_girls_wild_storyline["Level_3_girls_wild_bad_weather_show_response"])