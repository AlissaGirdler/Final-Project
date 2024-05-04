import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *



def solo_adventure():
    penup(), goto(0,0), pendown()
    person(25,'female')

    word_bubble(110,'white')
    choice = textinput(Level_2_Solo_Storyline,"Level_2_Domestic/International_Option",12,-280,325)

    if choice == "1":
        domestic_solo()
    
    elif choice == "2": 
        international_solo()
    
    else:
    write_story(Misc_Storyline,"")
    solo_adventure()

# def domestic_solo():
#     print(Level_2_Solo_Storyline["Level_2_Domestic_Response"])
#     print(Level_2_Solo_Storyline["Level_2_Domestic_Travel"])
#     # Generate random weather (good or bad)
#     # What is the best way to incorporate the weather API into this?
#     weather = random.choice(["good", "bad"])

#     if weather == "good":
#         beach_or_dune = input(Level_3_solo_domestic__Activity_storyline["Level_3_Solo_Domestic_Good_Weather_Option"])
        
#         if beach_or_dune == "1":
#             print(Level_3_solo_domestic__Activity_storyline["Level_3_Solo_Domestic_Beach_Day_Response"])
#         elif beach_or_dune == "2":
#             print(Level_3_solo_domestic__Activity_storyline["Level_3_Solo_Domestic_Dune_Surfing_Response"])
#         else:
#             print("Invalid choice. Please enter either 1 or 2.")
#             # Repeat the decision point
#     else:
#         print (Level_3_solo_domestic__Activity_storyline["Level_3_Solo_Domestic_Bad_Weather_Response"])



# def international_solo():
#     print(Level_2_Solo_Storyline["Level_2_International_Response"])
#     print(Level_2_Solo_Storyline["Level_2_International_Travel"])
#     # Generate random weather (good or bad)
#     weather = random.choice(["good", "bad"])

#     if weather == "good":
#         mtfuji_mariokart = input(Level_3_solo_international_storyline['Level_3_Solo_International_Good_Weather_Option'])

#         if mtfuji_mariokart == "1":
#             print(Level_3_solo_international_storyline['Level_3_Solo_International_Mt_Fuji_Response'])
#         elif mtfuji_mariokart == "2":
#             print(Level_3_solo_international_storyline['Level_3_Solo_International_Mario_Kart_Response'])
#         else:
#              print("Invalid choice. Please enter either 1 or 2.")
#             # Repeat the decision point
    
#     else:
#         food_sumo = input(Level_3_solo_international_storyline['Level_3_Solo_International_Bad_Weather_Option'])
        
#         if food_sumo == "1":
#             print(Level_3_solo_international_storyline ['Level_3_Solo_International_Food_Tourism_Response'])
#         elif food_sumo == "2":
#             print(Level_3_solo_international_storyline ['Level_3_Solo_International_Sumo_Wrestling_Response'])