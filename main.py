from spydetails import spy #importing variables from spydetails.py
from steganography.steganography import Steganography #import stganography module from steganography class of steganography library
from datetime import datetime #importingdatetime module from datetime class
time=datetime.now() #.now() function which will return current date and time
print time #printing returned current date and time
print "Hello Buddy!" #to print string name
print "Let\'s get started"
Status_Message = ['Galti badi galti engineering','Attachments are good for email only','Sleeping']#displaying menu of old status listed
friends_name = [{"name":"shyam","age":24,"rating":3.5,"is_online":True,"chats":[]},{"name":"aman","age":29,"rating":4,"is_online":True,"chats":[]}]#making list of friends which consists of dictionaries
def add_status(c_status):#function to add status
    if c_status != None:#checking if the status is none
        print "Your current status is " + c_status
    else:
        print "You don't have any status currently "
    existing_status = raw_input("You want to select from old status? Y/N ")#asking them which option you want to select either old status or not
    if existing_status.upper()=="N":
        new_status=raw_input("Enter your status: ")
        if len(new_status)>0:#checking length of status
            Status_Message.append(new_status)#adding the status in the status list
    elif existing_status.upper()=="Y": #checking if user want to add an old status
        serial_no=1
        for old_status in Status_Message:#printing an old status
            print str(serial_no)+ ". " + old_status#concatinating serial no with choosed status
            serial_no=serial_no + 1
        user_choice = input("enter your choice: ")#saking choice of user to choose options
        new_status = Status_Message[user_choice-1]#updating the status
        updated_status = new_status
        return updated_status
def add_friend():#function to add friend
    frnd={
        "name":" ",
        "age":0,
        "rating":0.0,
        "is_online":True,
        "chats":[]
    }
    frnd["name"] = raw_input("What is your name? ")
    frnd["age"] = input("What is your age? ")
    frnd["rating"] = input("What is your rating? ")
    if len(frnd["name"]>2 and 12<frnd["age"]<50 and frnd["rating"]>spy["ratings"]:#conditions for adding new friend
     friends.append(frnd)
    else:
        print "Friend cannot be added ."
    return len(friends)#will return to add_friend()
def select_a_friend():#defining a function
    serial_no=1
    for frnd in friends:
        print str(serial_no) + ".  " + frnd ["name"]
        serial_no=serial_no + 1
    user_selected_frnd=input("Enter your choice: ")#asking user choice to which friend  to select
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index #returning data to select_a friend()
def send_a_message():#defining function
    selected_frnd=select_a_friend()
    originsl_image=raw_input("What is the name of your image?")#asking user about the name of image
    secret_text=raw_input("What is your secret text ? ")#asking about what secret text you need to save in image
    output_path="output.png"#giving the output_path or we can say name where tyhe merged image and secret text will be stored an donly the image will be displayed.
    Steganography.encode(original_image,out_path,secret_text)#encoding the image with secret text.
    print "Your secret text has been succesfully encoded "
    new_chat={ #dictionary
        "message":secret_text,
        "time":datetime.now(),
        "sent_by_me":True
    }
    friends[selected_frnd]["chats"].append(new_chat)#appending in friends list the new_chat dictionary
    print "Your secret message is ready. "
def read_a_message():
    selected_frnd=select_a_friend()
    output_path=raw_input("Which image you want to decode? ")#asking about which image user need to decode
    secret_text=Steganography.decode(output_path)#decoding the text from image
    print "Secret text is "+ secret_text
    new_chat={
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    friends[selected_frnd]["chats"].append(new_chat)#appending
    print "Your secret message has been saved. "
def spy_chat(spy_name,spy_age,spy_rating):#defing function
    print "Here are your options " + spy["name"]
    current_status = None
    show_menu=True
    while show_menu:
        spy_choice=input("What do you want to do? \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read a message \n 0.exit")
        if spy_choice==1:#will display the status
            current_status = add_status(current_status)
            print "Updated status is " + current_status
        elif spy_choice==2:#cwill display number of friend user have.
            no_of_frnds = add_friend()#calling function add friend to add friend
            print "You have " + str(no_of_frnds) + " friends "# printing number of friends
        elif spy_choice==3:#will send encoded message
            send_a_message()
        elif spy_choice==4:
            read_a_message()
        elif spy_choice==5:
            print "Read chats from user. "
        elif spy_choice==6: #will come out of show_menu option
            show_menu=False
        else:
            print "Invalid options"
spy_exist=raw_input("Are you a new user(Y/N)? ")
if spy_exist.upper()=="N":#when spy isn old one
        print "Welcome back "+ spy["name"] + " age : "+str(spy["age"]) +"having rating of " +str(spy["rating"])
        start_chat(spy["name"],spy["age"],spy["ratings"])
elif spy_exist.upper()=="Y": #if spy is new then the resgistration starts
    spy ={ #dictionary
        "name": " ",
        "age": 0,
        "rating":0.0
    }
    spy["name"] = raw_input("what is your spy name") #take name as input from user
    print spy["name"]
    if len(["spy name"])>2:#checking for length of the string name
        print "Welcome " + spy["name"] + ". Glad to have you back with us"
        spy_salutaion = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutaion=="Mr." or spy_salutaion== 'Ms.' or spy_salutaion=="ms." or spy_salutaion=="mr.":#using if to check condition to take input of salutation
            spy["name"] = spy_salutaion + " " + spy["name"]
            print "Alright " + spy["name" ]+ ". I'd like to know a little bit more about you"
            spy["age"] = input("What is your age?")
            if 60>spy["age"]>14:#nested if statement to check range of age
                print "Welcome to the team."
                spy["ratings"] = input("What is your ratings?")
                if spy["ratings"]>5.0:#fixing the rating greater than 5
                    print "Welldone. "
                elif 3<spy["ratings"]<=5.0:#elif statement for more than one condition
                    print "Average spy"
                elif 2.0<spy["ratings"]<=5.5:
                    print "Need to work"
                else: #worst working
                    print "Worst"
                spy_is_online = True#checking if spy is online
                print "Authentication is completed. Welcome " + spy_name + "age:" + str(spy_age) + " and ratings: " + str(spy_ratings)
                start_chat(spy["name"],spy_age,spy_ratings)
            else:
                print "Your age is not eligible to be a spy"
        else:#when salutation is incorrect
            print "Invalid salutation"
    else:
        print "Ooopss Please enter a valid name"
else:
    print"Invalid input"