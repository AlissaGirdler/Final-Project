import sys
import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *

def solo_adventure():
    bgcolor('white')
    penup(), goto(0,0), pendown(), setheading(0)
    person(25,'female')
    word_bubble(110,'CadetBlue4')
    write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325,'white')

    choice = textinput("User Input",Level_2_Solo_Storyline["Level_2_Domestic/International_Option"])

    if choice == "1":
        domestic_solo()
    
    elif choice == "2": 
        international_solo()
    
    elif choice == "Exit":
        write_story(Misc_Storyline,"Exit",12,-280,280)
        sys.exit()
    
    else:
        write_story(Misc_Storyline,"invalid_entry",12,-280,280)
        solo_adventure() # PUNCH LIST add while true loop

def domestic_solo():

    bgcolor('white')
    word_bubble(110,'LightGoldenRodYellow')
    write_story(Level_2_Solo_Storyline,"Level_2_Domestic_Response",12,-280,280,'Azure4')
    time.sleep(3)
    blank_page()

   
    place("Outer Banks",300,-250)
    time.sleep(2)
    place('Madison',-300,-250)


    flight(300,'yellow')
    time.sleep(3)

    word_bubble(110,'LightGoldenRodYellow')
    write_story(Level_2_Solo_Storyline,"Level_2_Domestic_Travel",12,-280,280, 'Azure4')
    
    blank_page()

    random_weather = random.choice(weather)

    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)

        beach_or_dune = textinput("User Input",Level_3_solo_domestic__Activity_storyline["Level_3_Solo_Domestic_Good_Weather_Option"])
        
        blank_page()

        if beach_or_dune == "1":
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_domestic__Activity_storyline,"Level_3_Solo_Domestic_Beach_Day_Response",12,-280,280, 'Azure4')
            activity('Beach Day',50,-50)

        elif beach_or_dune == "2":
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_domestic__Activity_storyline,"Level_3_Solo_Domestic_Dune_Surfing_Response",12,-280,280, 'Azure4')
            activity('Dune Surfing',50,-50)
   
        elif beach_or_dune == "Exit":   
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Misc_Storyline,"Exit",12,-280,280)
            sys.exit()
    
        else:
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Misc_Storyline,"invalid_entry",12,-280,280)
        
    
    else:
        if random_weather == "cloudy":

            cloudy()
            time.sleep(3)
            blank_page()

            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_domestic__Activity_storyline,"Level_3_Solo_Domestic_Bad_Weather_Response",12,-280,280, 'Azure4')
            activity('Wright Museum',50,-50)

        elif random_weather == 'rainy':

            rain()
            time.sleep(3)
            blank_page()

            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_domestic__Activity_storyline,"Level_3_Solo_Domestic_Bad_Weather_Response",12,-280,280, 'Azure4')
            activity('Wright Museum',50,-50)


def international_solo():
    word_bubble(110,'LightGoldenRodYellow')
    write_story(Level_2_Solo_Storyline,"Level_2_International_Response",12,-280,280, 'Azure4')

    
    blank_page()
    place('Tokyo',300,-250)
    time.sleep(3)
    place('Madison',-300,-250)
    time.sleep(3)

    flight(300,'orange')
    time.sleep(3)

    word_bubble(110,'LightGoldenRodYellow')
    write_story(Level_2_Solo_Storyline,"Level_2_International_Travel",12,-280,280, 'Azure4')

    random_weather = random.choice(weather)

    if random_weather == "sunny":
        
        sunny()
        time.sleep(3)

        mtfuji_mariokart = textinput("User Input", Level_3_solo_international_storyline['Level_3_Solo_International_Good_Weather_Option'])

        blank_page()

        if mtfuji_mariokart == "1":
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Mt_Fuji_Response",12,-280,280, 'Azure4')
            activity('Mt Fuji',50,-50)

        elif mtfuji_mariokart == "2":
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Mario_Kart_Response",12,-280,280, 'Azure4')
            activity('Mario Kart',50,-50)

        elif mtfuji_mariokart == "Exit":

            word_bubble(110,'LightGoldenRodYellow')
            write_story(Misc_Storyline,"Exit",12,-280,280,'Azure4')
            sys.exit()
    
        else:
            word_bubble(110,'LightGoldenRodYellow')
            write_story(Misc_Storyline,"invalid_entry",12,-280,280,'Azure4')
    
    else:
        if random_weather == "cloudy":

            cloudy()
            time.sleep(3)

            food_sumo = textinput("User Input",Level_3_solo_international_storyline['Level_3_Solo_International_Bad_Weather_Option'])
            
            blank_page()

            if food_sumo == "1":
                word_bubble(110,'LightGoldenRodYellow')
                write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Food_Tourism_Response",12,-280,280, 'Azure4')
                activity('Food Tourism',50,-50)

            elif food_sumo == "2":
                word_bubble(110,'LightGoldenRodYellow')
                write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Sumo_Wrestling_Response",12,-280,280, 'Azure4')
                activity('Sumo',50,-50)
        
        elif random_weather == "rainy":

            cloudy()
            time.sleep(3)

            food_sumo = textinput("User Input",Level_3_solo_international_storyline['Level_3_Solo_International_Bad_Weather_Option'])
            
            blank_page()

            if food_sumo == "1":
                word_bubble(110,'LightGoldenRodYellow')
                write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Food_Tourism_Response",12,-280,280, 'Azure4')
                activity('Food Tourism',50,-50)

            elif food_sumo == "2":
                word_bubble(110,'LightGoldenRodYellow')
                write_story(Level_3_solo_international_storyline,"Level_3_Solo_International_Sumo_Wrestling_Response",12,-280,280, 'Azure4')
                activity('Sumo',50,-50)
    
    time.sleep(3)
    blank_page()
