import random

#Can each of the options of the adventure be it's own module in order to break up the code? 
#Can we call specific text files?
#Don't forget to add an exit option!!



#INTRODUCTION MODULE - INCORPORATE THIS INTO TURLES

def start_adventure():
    print("Welcome to the Choose Your Own Adventure story!")
    print("You have four options for your trip:")
    print("1. Solo")
    print("2. Couples trip")
    print("3. Girls getaway")
    print("4. Bring the kids")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        solo_adventure()
    elif choice == "2":
        couples_trip()
    elif choice == "3":
        girls_getaway()
    elif choice == "4":
        bring_the_kids()
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
        start_adventure()











#SOLO ADVENTURE MODULE - INCORPORATE INTO TURTLES
def solo_adventure():
    print("You've chosen to go on a solo adventure!")
    print("Now, you have two options:")
    print("1. Domestic")
    print("2. International")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        domestic_solo()
    elif choice == "2":
        international_solo()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        solo_adventure()

def domestic_solo():
    print("You've chosen to go on a domestic solo adventure to Outer Banks, North Carolina!")
    # Generate random weather (good or bad)
    # What is the best way to incorporate the weather API into this?
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather forecast looks great! Enjoy your sunny adventure.")
        beach_or_dune = input("You have two options: Beach day or Dune surfing. Enter 1 for Beach day or 2 for Dune surfing: ")
        
        if beach_or_dune == "1":
            print("You've chosen to spend a relaxing day at the beach!")
            print ("That was great!")
        elif beach_or_dune == "2":
            print("You've chosen to try out dune surfing!")
            print("Then got a little wild and injured yourself.")
        else:
            print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    else:
        print("Unfortunately, the weather forecast predicts rain. Head over to the Wright Museum of Flight to get your National Park stamp. Don't forget your umbrella!")
        print ("That was cool, but you wished you could have been outside more.")



def international_solo():
    print("You've chosen to go on an international solo adventure to Tokyo, Japan !")
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather forecast looks great! Enjoy your sunny adventure.")
        mtfuji_mariokart = input("You have two options: Climb Mt Fuji or Mario Kart. Enter 1 for Mt Fuji or 2 for Mario Kart: ")

        if mtfuji_mariokart == "1":
            print("You've chosen to spend the day climbing Mt. Fuji!")
            print("And it was absoultely amazing!")
        elif mtfuji_mariokart == "2":
            print("You've chosen to race in a real life Mario Kart event!")
            print("Rainbow road treated you well, you won the race!")
        else:
             print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    
    else:
        print("The weather forecast predicts rain. Head downtown for a food tour and a Sumo Wrestling match. Don't forget your umbrella!")
        print ("You were able to fit in both activities and met a few fun individuals along the way.")
        

 










   

#CODE FOR LEG 2 - COUPLE'S TRIP
def couples_trip():
    print("You've chosen to go on a couples trip!")
    print("Now, you have two options:")
    print("1. Sanoma")
    print("2. South Africa")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        domestic_couple()
    elif choice == "2":
        international_couple()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        couples_trip()

def domestic_couple():
    print("You've chosen to go on a domestic couple's adventure to Sanoma, CA!")
    print ("A wine tour has been scheduled, rain or shine!")
    # Generate random weather (good or bad)
    # What is the best way to incorporate the weather API into this?
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather was sunny and comfortable, it was a wonderful time!")
       
    else:
        print("Unfortunately, the weather was a little cold and rainy. Which ultimately ruined the experience.")
  



def international_couple():
    print("You've chosen to go on an international couple's adventure to South Africa!")
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather forecast looks great! Enjoy your sunny adventure.")
        sharkcage_safari = input("You have two options: Go on Safari or Cage Shark swimming. Enter 1 for Safari or 2 for Cage Shark: ")

        if sharkcage_safari == "1":
            print("You've chosen to spend the day roaming the African desert")
            print("And it was exhilerating!")
        elif sharkcage_safari == "2":
            print("You've chosen to risk a limb with Cage Shark swimming!")
            print("The sharks treated you well, you had an exhilerating experience!")
        else:
             print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    
    else:
        print("The weather forecast predicts rain. Go on the adventure anyway. Don't forget your umbrella!")
        print ("Despite the rain you have a new inspired perspective on life.")








#CODE FOR LEG 3 - GIRL'S TRIP
def girls_getaway():
    print("You've chosen to go on a girls getaway!")
    print("Now, you have two options:")
    print("1. Serene")
    print("2. Wild")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        serene_girls()
    elif choice == "2":
        wild_girls()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
        girls_getaway()

def serene_girls():
    print("You've chosen to go on a serence girls trip to Lake Geneva, Wisconsin.")
    print ("A spa day has been scheduled, rain or shine!")
    # Generate random weather (good or bad)
    experience = random.choice(["good", "bad"])

    if experience == "good":
        print("It was expensive, but so relaxing!")
       
    else:
        print("Unfortunately, the spa was kind of cheap and didn't really meet our expectations.")




def wild_girls():
    print("Vegas ladies!")
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather forecast looks great! Let's walk the strip.")
        vegas_strip = input("You have two options: Old Strip or New Strip. Enter 1 for Old or 2 for New: ")

        if vegas_strip == "1":
            print("You've chosen to spend the day exploring the older side of Vegas")
            print("And it was a litte sketchy...and gross!")
        elif vegas_strip == "2":
            print("You've chosen to spend the evening purusing the new strip!")
            print("And had the most fun watching Kygo at XS Nightclub")
        else:
             print("Invalid choice. Please enter either 1 or 2.")
            # Repeat the decision point
    
    else:
        print("The weather forecast predicts rain.")
        casino_show = input ("You have two options: Gamble at the Casino or take in a Show. Enter 1 for Casino or 2 for Show: ")
      
        if casino_show == "1":
            print ("You went to the Casino and won $500!")
        elif casino_show == "2":
            print ("You went to a show and were mezmerized by Cirque de Soleil")
        








#CODE FOR LEG 3 - FAMILY TRIP
def bring_the_kids():
    print("You've chosen to bring the kids along!")
    print("Invalid choice. Please enter a number from 1 to 4.")
    start_adventure()

start_adventure()




# Randomly generate outcome of return flight
return_flight_outcome = random.choice(["went well", "went badly"])
if return_flight_outcome == "went well":
     print("Your return flight went smoothly. You had a great trip overall!")
else:
     print("Your return flight was delayed, but you made the best of it. It was still a memorable adventure!")