import random

#Below is the module to kick-off / introduce the story. 
#Can each of the "legs" of the adventure be it's own module in order to break up the code? 
#Can we call specific text files?

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


#CODE FOR LEG 1 - SOLO ADVENTURE 
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
        print ("That was cool, but I wish I could have been outside more.")

def international_solo():
    print("You've chosen to go on an international solo adventure to Tokyo, Japan !")
    # Generate random weather (good or bad)
    weather = random.choice(["good", "bad"])

    if weather == "good":
        print("The weather forecast looks great! Enjoy your sunny adventure.")
        # Add the storyline for good weather here
    else:
     print("Unfortunately, the weather forecast predicts rain. Don't forget your umbrella!")
        # Add the storyline for bad weather here

 

   

#CODE FOR LEG 2 - COUPLE'S TRIP
def couples_trip():
    print("You've chosen to go on a couples trip!")
    # Add the storyline for couples trip here

#CODE FOR LEG 3 - GIRL'S TRIP
def girls_getaway():
    print("You've chosen to go on a girls getaway!")
    # Add the storyline for girls getaway here

#CODE FOR LEG 3 - FAMILY TRIP
def bring_the_kids():
    print("You've chosen to bring the kids along!")
    # Add the storyline for bringing the kids here

start_adventure()
