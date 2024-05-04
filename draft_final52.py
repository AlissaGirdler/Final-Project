import random
from storyline_dictionaries import *
from solo_module import *
from couples_module import *
from girls_module import *
from other_dictionaries_and_lists import *

#do we have to put exit function here and also in each module?


#INTRODUCTION
print(Misc_Storyline["Introduction"])

#LEVEL 1 CHOICE
print(Level_1_Storyline["Level_1_Introduction"])
choice = input(Level_1_Storyline['Level_1_Option'])

if choice == "1":
    print(Level_1_Storyline["Level_1_Solo_Option_Response"])
    solo_adventure()
elif choice == "2":
    print(Level_1_Storyline["Level_1_Couples_Option_Response"])
    couples_trip()
elif choice == "3":
    print (Level_1_Storyline["Level_1_Girls_Option_Response"])
elif choice == "4":
   print (Level_1_Storyline["Level_1_Kids_Option_Response"])
   print (Level_2_Kids_Storyline['sure'])
   print (travel_checklist) #INSERT BREAK HERE AT SPECIFIC TIME
   print (Level_2_Kids_Storyline['time'])
   #INSERT FUNCTION TO KICK BACK TO THE START?
else:
    print("Invalid choice. Please enter a number from 1 to 4.")


#add a print statement here to segway into return flight?
# Randomly generate outcome of return flight 
return_flight_outcome = random.choice(["Perfect_Upgrade", "Nightmare", "Just_Fine", "Pretty_Good"])
if return_flight_outcome == "Perfect_Upgrade":
     print(Flight_Quality_Randomizer['Perfect_Upgrade'])
elif return_flight_outcome == "Nightmare":
     print(Flight_Quality_Randomizer['Nightmare'])
elif return_flight_outcome == "Just_Fine":
     print(Flight_Quality_Randomizer['Just_Fine'])
else:
     print(Flight_Quality_Randomizer['Pretty_Good'])


#LEVEL 4 CHOICE 
choice = input(Level_4_storyline['Outcome_Option'])

if choice == "1":
    print(Level_4_storyline['Relaxed_and_Reenergized_Response'])
elif choice == "2":
    print(Level_4_storyline['Exhausted_and_Stressed_Response'])


#ENDING
print(Misc_Storyline["Ending"])