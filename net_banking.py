'''This is the new version of formerly created first.py in which I am trying to write the same software which will run on python3 '''

#importing necessary libraries
import time
import csv

#login function for login a user into its profile
def login():
    print("Welcome to logn console user \n\t")



#signup function to create a user and give access to use to use our services



#about function to let user know about this project





# home function or index function which will be executed at first the program executed.
def home():
    print('Welcome to Net Banking and enjoy the services')
    print('You can choose from below to proceed further\n\t1. Login (if already have account)\n\t2. Signup (for new user) \n\t3. About this project')
    choice = int(input('Enter a chioce You want'))
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
