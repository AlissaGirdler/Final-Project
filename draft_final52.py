from storyline_dictionaries import *
from solo_module import *


#INTRODUCTION
print(Misc_Storyline["Introduction"])

#LEVEL 1 CHOICE
print(Level_1_Storyline["Level_1_Introduction"])
choice = input(Level_1_Storyline['Level_1_Option'])

if choice == "1":
    print(Level_1_Storyline["Level_1_Solo_Option_Response"])
    solo_adventure()



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