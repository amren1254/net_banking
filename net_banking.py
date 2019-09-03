'''This is the new version of formerly created first.py in which I am trying to write the same software which will run on python3 '''

#importing necessary libraries
import time
import csv
import psycopg2 # importing psycopg2 driver library to make connection with postgres database.

try:
    conn = psycopg2.connect(user = "amren",
            password = "amren",
            host = "localhost",
            port = "5432",
            database = "tutree")
    cursor = conn.cursor()
    cursor.execute("select version()")
    record = cursor.fetchone()
    print("You are connected to ",record,"\n")
except(Exception,psycopg2.Error) as error:
    print("Error while connecting to database")
finally:
    if(conn):
        cursor.close()
        conn.close()
        print("Postgresql connection closed")

#profile function for a user which will show user details
def profile(userid):
    print("\tWe are happy you are with us\n")
    print("\tWe welcome you to our world\n")



#login function for login a user into its profile
def login():
    print("Welcome to login console user \n\t")
    username = input("\tUSERNAME:  ")
    if (username == 'amren'):
        password = input("\n\tPASSWORD:  ")
        if (password == 'amren'):
            userid = 1
            print("\n\tWelcome user")
            profile(userid)
        else:
            print("\n---------What! Wrong password user------------")
    else:
        print("\nYour account doesn't exist "+username)
#function to validate email 
def validate_email():
    email = input("Enter your email: ")
    #if email == 


#function for checking password strength



#signup function to create a user and give access to use to use our services
def signup():
    print('''Welcome to signup Here you can create an account for yourself and enjoy our services''')
    name = input("\tEnter you Name\t\t")
    email = input("\tEnter your Email\t")
    password = input("\tCreate a password\t")
    query = "insert into user_data values (name,email,password)"
    #query.execute()
    


#about function to let user know about this project
def about():
    print('''\tThis is a practice project before some exam 
            I just want to have hands on experience on python before
            executing python script file in real environment.\n''')




# home function or index function which will be executed at first the program executed.
def home():
    print('Welcome to Net Banking and enjoy the services')
    print('You can choose from below to proceed further\n\t1. Login (if already have account)\n\t2. Signup (for new user) \n\t3. About this project')
    choice = int(input('Enter a chioce You want\t'))
    if choice==1:
        login()
    elif choice==2:
        signup()
    elif choice==3:
        about()
    else:
        print('----Hey wrong input given----\n\tProgram will exit after 2 second')
        time.sleep(2)
home()
