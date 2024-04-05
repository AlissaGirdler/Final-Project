from turtle import *
import math
import random
import time

storyline = {
    "Introduction":
        "\n\
        On Sunday night Taylor's phone pings with an urgent email.\n\
        As Taylor reads, her jaw drops in surprise. \n\
        There is a major network failure at work that will take all week to fix, \n\
        All staff have been given the week off. \n\
        \n\
        Taylor is over the moon, \n\
        she has been wanting to go on vacation for months. \n\
        This week off is her chance,\n\
        Taylor needs your help to plan her last minute trip.\n",
    
    "Level_1_Introduction":
        "\n\
        Taylor loves the idea of going with her family\n\
        but she also LOVES the idea of travelling alone or with her girlfriends\n",
    
    "Level_1_Option": "\
        Should Taylor go on vacation: \n\
            1. alone \n\
            2. with her partner \n\
            3. with her girls \n\
            4. with her kids  \n\
        Enter your choice:",

    "Level_1_Solo": " ",

    "Level_1_Couples": " ",

    "Level_1_Girls": " ",

    "Level_2_Kids": " ",

    "Exit": "Bon voyage Tay Tay! Exiting...",

    "Invalid_Entry": "Invalid entry, please enter a numeric value or type 'Exit' to end the program"

}

print(storyline["Introduction"])

print(storyline["Level_1_Introduction"])
Level_1_Option = input(storyline['Level_1_Option'])

if int(Level_1_Option) == 1:
    print(storyline["Level_1_Solo"])

elif int(Level_1_Option) == 2:
    print(storyline["Level_1_Couples"])

elif int(Level_1_Option) == 3:
    print(storyline["Level_1_Girls"])

elif("exit" in Level_1_Option.lower()):
    print(storyline["Exit"])

else:
    print(storyline["Invalid_Entry"])