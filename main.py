from spy_details import spy ,Spy ,ChatMessage #importing variables from spydetails.py
from steganography.steganography import Steganography #import stganography module from steganography class of steganography library
import csv
from datetime import datetime  #importingdatetime module from datetime class
time=datetime.now()           #.now() function which will return current date and time
print time                    #printing returned current date and time
print "Hello Buddy!"          #to print string name
print "Let\'s get started"
Status_Message = ['Galti badi galti engineering','Attachments are good for email only','Sleeping']#displaying menu of old status listed
frnd1 = Spy("Tannya","Ms. ",19,2.3)
frnd2 = Spy("Kakul","Ms. ",20,3.3)
friends=[frnd1,frnd2]
def load_frnds():# load friends in friends list from frnd.csv file
    with open("friends.csv", "rb") as friends_data:
        reader = list(csv.reader(friends_data))
        for row in reader[1:]:
            spy=Spy(name=row[0],salutation=row[1],age=row[2],rating=row[3])
            friends.append(spy)
load_frnds()
def load_chats():#loading chat of receiver and sender
    with open("chats.csv", "rb") as friends_data:
        reader = list(csv.reader(chats_data))
        for message,day,date,sent_by_me,receiver_name in reader[1:]:
            print Fore.BLACK+message, Fore.GREEN + day, Fore.RED + day, Fore.BLUE+sent_by_me + Fore.CYAN+receiver_name
            print(style.RESET_ALL)
def selected_chat():
    s_name=raw_input("enter the name of friendwhose name chat you want to see. ")
    with open("chats.csv", "rb") as friends_data:
        reader = list(csv.reader(chats_data))
        for message,day,date,sent_by_me,receiver_name in reader[1:]:
            if s_name==receiver_name:
                print Fore.BLUE+day,Fore.GREEN+date,Fore.RED+sent_by_me,Fore.BLACK+message
                print(style.RESET_ALL)
            else:
                print"No ,chat is available."
def add_status(c_status):     #function to add status
    if c_status != None:      #checking if the status is none
        print "Your current status is " + c_status
    else:
        print "You don't have any status currently "
    existing_status = raw_input("You want to select from old status? Y/N ")#asking them which option you want to select either old status or not
    if existing_status.upper()=="N":
        new_status=raw_input("Enter your status: ")
        if len(new_status)>0:#checking length of status
            with open("sts.csv","a") as friend_status:
                writer=csv.writer(friend_status)
                writer.writerrow([new_status])
                updated_status = new+status
    elif existing_status.upper()=="Y": #checking if user want to add an old status
        serial_no=1
        for old_status in Status_Message:#printing an old status
            print str(serial_no)+ ". " + old_status#concatinating serial no with choosed status
            serial_no=serial_no + 1
        user_choice = input("enter your choice: ")#saking choice of user to choose options
        new_status = Status_Message[user_choice-1]#updating the status
        updated_status = new_status
        return updated_status#will return to the function add_status
def add_friend():#function to add friend
    frnd=Spy(" "," ",0,0.0)
    frnd.name = raw_input("What is your name? ")
    frnd.sal = raw_input("What should we call you? ")
    frnd.age = input("What is your age? ")
    frnd.rating = input("What is your rating? ")
    frnd.is_online = True
    if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating:#conditions for adding new friend
        friends.append(frnd)
        with open("friends.csv", "a" )as friend_data :
            writer=csv.writer(friend_data)
            writer.writerrow([frnd.name, frnd.sal, frnd.rating, frnd.age, frnd.is_online])
    else:
        print 'Friend cannot be added .'
    return len(friends)#will return to add_friend()
def select_a_friend():#defining a function
    serial_no=1
    for frnd in friends:
        print str(serial_no) + ".  " + frnd.name
        serial_no=serial_no + 1
    user_selected_frnd=input("Enter your choice: ")#asking user choice to which friend  to select
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index #returning data to select_a friend()
def send_a_message():#defining function
    selected_frnd=select_a_friend()
    original_image=raw_input("What is the name of your image?")#asking user about the name of image
    secret_text=raw_input("What is your secret text ? ")#asking about what secret text you need to save in image
    list=["HELP ME","SOS","SAVE ME","EMERGENCY"]#listng the special message
    if secret_text.upper() in list:
        print Fore.RED + "Inappropriate message. "
        print (Style.RESET_ALL)
    else:
        output_path="output.jpg"#giving the output_path or we can say name where tyhe merged image and secret text will be stored an donly the image will be displayed.
        Steganography.encode(original_image,output_path,secret_text)#encoding the image with secret text.
        with open("chat.csv", "a") as chats_data:
            writer = csv.writer(chats_data)
            writer.writerrow([secret_text,time,spy.name,friends[selected_frnd].name])
        print "Your secret text has been succesfully encoded "
        new_chat= ChatMessage(secret_text,True)
    friends[selected_frnd].chats.append(new_chat)#appending in friends list the new_chat dictionary
    print "Your secret message is ready. "
def read_a_message():
    selected_frnd=select_a_friend()
    output_path=raw_input("Which image you want to decode? ")#asking about which image user need to decode
    secret_text=Steganography.decode(output_path)#decoding the text from image
    print "Secret text is "+ secret_text
    new_chat=ChatMessage(secret_text,False)
    friends[selected_frnd].chats.append(new_chat)#appending
    print "Your secret message has been saved. "
def save_chat():
    selected_frnd=select_a_friend()
#if selected_friend==1
def spy_chat(spy_name,spy_age,spy_rating):#defing function
    print "Here are your options " + spy.name
    current_status = None
    show_menu=True
    while show_menu:
        spy_choice=input("What do you want to do? \n 1.Add a status \n 2.Add a friend \n 3.Send a message \n 4.Read a message \n 5. Read chat history \n 0.exit")
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
spy_username=raw_input(" Enter your username/email. ")
spy_password=raw_input("Enter your password")
if spy_username=="Priya" and spy_password=="loginadmin":
    print " You are logged in. "
    spy_exist=raw_input("Are you a new user(Y/N)? ")
    if spy_exist.upper()=="N":#when spy isn old one
        print "Welcome back "+ spy.name + " age : "+str(spy.age) +"having rating of " +str(spy.rating)
        spy_chat(spy.name,spy.age,spy.rating) #calling functions
    elif spy_exist.upper() == "Y": #if spy is new then the resgistration starts
        spy =Spy(" "," ",0,0.0)
        spy.name = raw_input("what is your spy name") #take name as input from user
        print spy.name
        if len("name")>2:#checking for length of the string name
            print "Welcome " + spy.name + ". Glad to have you back with us"
            spy_salutaion = raw_input("What should we call you (Mr. or Ms.)? ")
            if spy_salutaion=="Mr." or spy_salutaion== 'Ms.' or spy_salutaion=="ms." or spy_salutaion=="mr.":#using if to check condition to take input of salutation
                spy.name = spy_salutaion + " " + spy.name
                print "welcome" + spy.name + "Glad to see you back"
                print "Alright " + spy.name+ ". I'd like to know a little bit more about you"
                spy.age = input("What is your age?")
                if 60>spy.age>14:#nested if statement to check range of age
                    print "Welcome to the team. "
                    spy.rating = input("What is your ratings?")
                    if spy.rating>5.0:#fixing the rating greater than 5
                        print "Welldone. "
                    elif 3<spy.rating<=5.0:#elif statement for more than one condition
                        print "Average spy"
                    elif 2.0<spy.rating<=5.5:
                        print "Need to work"
                    else: #worst working
                        print "Worst"
                    spy_is_online = True#checking if spy is online
                    print "Authentication is completed. Welcome " + spy.name + "age:" + str(spy.age) + " and ratings: " + str(spy.rating)
                    spy_chat(spy.name,spy.age,spy.rating)
                else:
                    print "Your age is not eligible to be a spy"
            else:#when salutation is incorrect
                print "Invalid salutation"
        else:
            print "Ooopss Please enter a valid name"
    else:
        print"Invalid input"
else:
    print"You can't log in. "