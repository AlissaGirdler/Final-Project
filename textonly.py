import math
import random

Level_1_Storyline = {
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

    "Level_1_Solo_Option_Response": "\n\
        Excellent! \n\
        Taylor is in need of some self care time\n\
        she thinks to herself...\n\
        'Should I commit to a BIG trip and go international\n\
        or will staying domestic feel like a getaway?'",

    "Level_1_Couples_Option_Response": "\n\
        My husband and I never even went on a honeymoon,\n\
        it's definitely time for some time together.\n\
        Taylor wonders thinks 'I could book the tickets\n\
        and surprise him tonight but...\n\
        would he prefer romance or adventure?'",

    "Level_1_Girls_Option_Response" : "\n\
        Yesssssssss!\n\
        I am calling my girls right now!",

    "Level_1_Kids_Option_Response": "\n\
        Hmmmm, okay...Taylor can pull this off,\n\
        travelling with two toddlers last minute - NO BIG DEAL!"
}

Level_2_Storyline = {
    "Level_2_Solo_Domestic/International_Option": "\n\
        Should Taylor go: \n\
            1. domestic \n\
            2. international \n\
        Enter your choice:",

    "Level_2_Solo_Domestic_Response": "\n\
        This is going to take some though\n\
        Taylor is thinking something simple, sunny and calm.\n\
        Outer Banks, North Carolina!",

    "Level_2_Solo_International_Response": "\n\
        Without a moments hesitation, Taylor yells\n\
        'I'm going to Japan!'",

    "Level_2_Solo_Domestic_Travel" : " ",

    "Level_2_Solo_International_Travel" : " "
}

Misc_Storyline = {
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

    "Invalid_Entry": "\n\
        Invalid entry, please enter a numeric \n\
        value or type 'Exit' to end the program",

    "Exit": "\n\
        Bon voyage Tay Tay! \n\
        Exiting...",
}


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
        print(Level_1_Storyline["Exit"])

    else:
        print(Level_1_Storyline["Invalid_Entry"])

    return Level_1_Option

print(Misc_Storyline["Introduction"])
Level_1()