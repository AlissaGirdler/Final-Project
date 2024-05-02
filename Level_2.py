import math
import random
from storyline_dictionaries import *
from other_dictionaries_and_lists import *
from Level_1 import *


def Level_2():
    while True:
        Level_1_Option = Level_1()

        if int(Level_1_Option) == 1:
            Level_2_Solo_Option = input(Level_2_Solo_Storyline["Level_2_Solo_Domestic/International_Option"])

            if Level_2_Solo_Option == '1':
                print(Level_2_Solo_Storyline["Level_2_Domestic_Response"])
                print(Level_2_Solo_Storyline["Level_2_Domestic_Travel"])
                break

            elif Level_2_Solo_Option == '2':
                print(Level_2_Solo_Storyline["Level_2_International_Response"])
                print(Level_2_Solo_Storyline["Level_2_International_Travel"])
                break

            elif Level_2_Solo_Option.lower() == "exit":
                print(Misc_Storyline["Exit"])
                return

            else:
                print(Misc_Storyline["Invalid_Entry"])

        elif int(Level_1_Option) == 2:
            Level_2_Couples_Option = input(Level_2_Couples_Storyline["Level_2_Romantic/Adventure_Option"])

            if Level_2_Couples_Option == '1':
                print(Level_2_Couples_Storyline["Level_2_Romantic_Response"])
                print(Level_2_Couples_Storyline["Level_2_Romantic_Travel"])
                break

            elif Level_2_Couples_Option == '2':
                print(Level_2_Couples_Storyline["Level_2_Adventure_Response"])
                print(Level_2_Couples_Storyline["Level_2_Adventure_Travel"])
                break

            elif Level_2_Couples_Option.lower() == "exit":
                print(Misc_Storyline["Exit"])
                return

            else:
                print(Misc_Storyline["Invalid_Entry"])

        elif int(Level_1_Option) == 3:
            Level_2_Girls_Option = input(Level_2_Girls_storyline["Level_2_serene/wild_option"])

            if Level_2_Girls_Option == '1':
                print(Level_2_Girls_storyline["Level_2_serene_response"])
                print(Level_2_Girls_storyline["Level_2_serene_travel"])
                break

            elif Level_2_Girls_Option == '2':
                print(Level_2_Girls_storyline["Level_2_wild_response"])
                print(Level_2_Girls_storyline["Level_2_wild_travel"])
                break

            elif Level_2_Girls_Option.lower() == "exit":
                print(Misc_Storyline["Exit"])
                return

            else:
                print(Misc_Storyline["Invalid_Entry"])

        elif int(Level_1_Option) == 4:
            print(Level_2_Kids_Storyline["sure"])

            for i in range():
                print(travel_checklist[i])

            print(Level_2_Kids_Storyline["time"])
            
