import math
import random
from turtle import *
from graphic_functions import *
from storyline_dictionaries_with_lists import *
from other_dictionaries_and_lists import *
from graphic_introduction import *
from graphic_solo_module import *


bubble_x = -280
bubble_y = 375

formatting()

# # INTRODUCTION
introduction()

# LEVEL 1 CHOICE
write_story(Level_1_Storyline,"Level_1_Introduction", 20, 0, 20,'white')
choice = textinput("User Input", Level_1_Storyline['Level_1_Option']) # PUNCH LIST text input curly brackets
clear()
bgcolor('white')

if choice == "1":
    word_bubble(110,'CadetBlue4')
    write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325,'white')
    solo_adventure()

# elif choice == "2":
#     word_bubble(110,'white')
#     write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325)

# elif choice == "3":
#     word_bubble(110,'white')
#     write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325)

# elif choice == "4":
#     word_bubble(110,'white')
#     write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325)

# else:
#     word_bubble(110,'white')
#     write_story(Level_1_Storyline,"Level_1_Solo_Option_Response",12,-280,325)







done()