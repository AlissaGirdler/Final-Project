
#Begin storyline: 

with open ("1_introduction.txt", "r", encoding = 'utf-8') as f:
    for i, line in enumerate(f,1):
        print(f"[i]: {line.rstrip()}")

# come back and clean up the [i] in front of each line


def main(): 
    trip_dictionary = {} #can we use a dictionary to house the txt files for each scenario? key value pair?
    while True: 
        tripchoice == textinput("Should Taylor go on vaction: \n", "1. alone. \n 2. with her partner. \n 3. with her girls. \n 4. with her kids. \n Enter your choice or type quit to exit:")

        if tripchoice =='1': 
            print ("Enter file reference for next prompt")

        elif tripchoice == '2':
            print ("Enter file reference for next prompt")

        elif tripchoice == '3':
            print ("Enter file reference for next prompt")
        
        elif tripchioce == '4':
            print ("Enter file reference for next prompt")






    def main():
    guestbook = {}
    while True:
        signin = textinput("Signin","Would you like to sign in? \n1.Yes, continue.\n2. View the guestbook.\n3. Exit:")

        if signin == '1':
            name = textinput("Signin", "Enter your name (Last Name, First Name): ")
            message = textinput("signin", "Leave a message for Cole: ")
            add_entry(guestbook, name, message)

        elif signin == '2':
            display_guestbook(guestbook)
        
        else:
            speed(10)
            penup()
            goto(-190,200)
            pendown()
            write("Exiting...goodbye!")
            exit(0)