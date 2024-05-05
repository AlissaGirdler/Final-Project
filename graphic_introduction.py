from turtle import *
import math
import random
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *
from graphic_functions import *
import time

def introduction():
    bgcolor('CadetBlue4')
    write_story(Misc_Storyline,"title", 20, 0, 20,"White")
    time.sleep(2)
    write_story(Misc_Storyline,"directions",12,0,-20,"White")
    time.sleep(4)
    clear()
    write_story(Misc_Storyline,"introduction",15,0,110,"White")
    time.sleep(10) # PUNCH LIST ITEM 
    clear()

