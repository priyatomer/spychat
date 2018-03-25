from spy_details import spy_name,spy_salutation,spy_age,spy_ratings #importing variables from spydetails.py
print "Hello Buddy!" #to print string name
print "Let\'s get started"
def start_chat(spy_name,spy_age,spy_rating): # funtion to show menu
    print "Here are your options " + spy_name
    show_menu=True
    while show_menu:
        choice=input("What do you want to do? \n 1.Add a status \n 2.Add a friend \n 0.exit")
        if choice==1:
            print "Will add a status."
        elif choice==2:
            print "Will add a friend"
        elif choice==0:
            show_menu=False
        else:
            print "Invalid entry"
spy_exist=raw_input("Are you a new user(Y/N)? ")
if spy_exist.upper()=="N":
    print "Welcome back "+ spy_salutation + spy_name
    start_chat(spy_name,spy_age,spy_ratings)
elif spy_exist.upper()=="Y": #if spy is new then the resgistration starts
    spy_name = raw_input("What is your spy name? ") #take name as input from user
    if spy_name.isspace(): #to check for space input
        print "Enter a valid name"
    if len(spy_name)>2:#checking for length of the string name
        print "Welcome " + spy_name + ". Glad to have you back with us." #concatenating strings
        spy_salutaion = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutaion=="Mr." or spy_salutaion=="Ms.":#using if to check condition to take input of salutation
            spy_name = spy_salutaion + " " + spy_name
            print "Alright " + spy_name + ". I'd like to know a little bit more about you"
            spy_age = input("What is your age?")
            if 60>spy_age>14:#nested if statement to check range of age
                print "Your age is correct."
                spy_ratings = input("What is your ratings?")
                if spy_ratings>8.0:
                    print "Great spy"
                elif 5.5<spy_ratings<=8.0:#elif statement for more than one condition
                    print "Average spy"
                elif 3.0<spy_ratings<=5.5:
                    print "Bad spy"
                else:
                    print "Are you really a spy?"
                spy_is_online = True
                print "Authentication is completed. Welcome " + spy_name + "age:" + str(spy_age) + " and ratings: " + str(spy_ratings)
                start_chat(spy_name,spy_age,spy_ratings)
            else:
                print "Your age is not eligible to be a spy"
        else:
             print "Invalid salutation"
    else:
        print "Ooopss Please enter a valid name"
else:
    print"Invalid entry"
