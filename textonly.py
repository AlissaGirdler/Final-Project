import math
import random
from storyline_dictionaries import *
import graphic_dictionaries_and_lists


def Level_1():

    print(Level_1_Storyline["Level_1_Introduction"])
    Level_1_Option = input(Level_1_Storyline['Level_1_Option'])

    if int(Level_1_Option) == 1:
        print(Level_1_Storyline["Level_1_Solo_Option_Response"])

    elif int(Level_1_Option) == 2:
        print(Level_1_Storyline["Level_1_Couples_Option_Response"])

    elif int(Level_1_Option) == 3:
        print(Level_1_Storyline["Level_1_Girls_Option_Response"])

    elif("exit" in Level_1_Option.lower()):
        print(Misc_Storyline["Exit"])

    else:
        print(Misc_Storyline["Invalid_Entry"])

    return Level_1_Option

def Level_2():
    Level_1_Option = Level_1()
     
    if int(Level_1_Option) == 1:
        Level_2_Option = input(Level_2_Storyline["Level_2_Solo_Domestic/International_Option"])

        if Level_2_Option == 1:
            print(Level_2_Storyline["Level_2_Solo_Domestic_Response"])

        elif Level_2_Option == 2:
            print(Level_2_Storyline["Level_2_Solo_International_Response"])
        
        elif("exit" in Level_2_Option.lower()):
            print(Misc_Storyline["Exit"])

        else:
            print(Misc_Storyline["Invalid_Entry"])

        return Level_2_Option

    elif int(Level_1_Option) == 2:
        print(" ")

    elif int(Level_1_Option) == 3:
        print(Level_1_Storyline["Level_1_Girls_Option_Response"])

    elif int(Level_1_Option) == 4:
        print(" ")

    


Level_1()