#!/usr/bin/env python3
'''This is the new version of formerly created first.py in which 
I am trying to write the same software which will run on python3 '''

'''importing necessary libraries'''
import time     #importing time library to make delays and store user creation time in database.
import csv      # importing csv library as used in older version of code to store user data 
#but I am using postgresql database in this one to store user data.
import psycopg2 # importing psycopg2 driver library to make connection with postgres database.
from termcolor import colored
import webbrowser
import re

import os

try:
    conn = psycopg2.connect(user = "amren",
            password = "amren",
            host = "localhost",
            port = "5432",
            database = "tutree")
    cursor = conn.cursor()      #creating cursor for the database to perform operation on database 
    #cursor.execute("select version()")  #executing the first query
    #record = cursor.fetchone()
    #print("You are connected to ",record,"\n")  #printed the first query result
except(Exception,psycopg2.Error) as error:
        print(colored("Error while connecting to database","red"))


'''profile function for a user which will show user details'''
def profile(userid):
    print(colored("\tWe are happy you are with us\n","yellow"))
    print(colored("\tWe welcome you to our world\n","yellow"))



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
            print("\n---------What! Wrong password "+ username +"------------")
    else:
        print("\nYour account doesn't exist "+username)
#function to validate email 
def validate_email():
    email = input("\tEnter your Email\t")
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex,email)):
        return email
    else:
        print(colored("\tInvalid Email","red"))
        validate_email()


#function for checking password strength
def validate_password():
    password = input("\tEnter password\t")
    flag = 0
    while True:   
        if (len(password)<8): 
            flag = -1
            break
        elif not re.search("[a-z]", password): 
            flag = -1
            break
        elif not re.search("[A-Z]", password): 
            flag = -1
            break
        elif not re.search("[0-9]", password): 
            flag = -1
            break
        elif not re.search("[_@$]", password): 
            flag = -1
            break
        elif re.search("\s", password): 
            flag = -1
            break
        else: 
            flag = 0
            return password
            break
  
    if flag ==-1: 
        print(colored("\tNot a Valid Password","red"))
        validate_password()

#signup function to create a user and give access to use to use our services
def signup():
    print('''Welcome to signup Here you can create an account for yourself and enjoy our services''')
    name = input("\tEnter you Name\t\t")
    email = validate_email()
    password = validate_password()
    #query = "insert into netbanking values (1,name,email,password)"
    #handling connection to the postgres database
    sql = "insert into netbanking values(%s,%s,%s)"
    record_to_insert = (name,email,password)
    cursor.execute(sql,record_to_insert)
    conn.commit()


#about function to let user know about this project
def about():
    print(colored("You will be redirected to your default browser in 6 sec",'yellow',attrs = ['blink']))
    print('''\tThis is a practice project before some exam 
            I just want to have hands on experience on python before
            executing python script file in real environment.\n''')
    time.sleep(6)
    webbrowser.open_new("about_netbanking.html")



# home function or index function which will be executed at first the program executed.
def home():
    while True:
        print(colored('Welcome to Net Banking and enjoy the services','green'))
        print('''You can choose from below to proceed further
                1. Login (if already have account)
                2. Signup (for new user) 
                3. About this project
                ** Press e/E to exit''')
        choice = input('Enter a chioce You want \t')
        try:
            choice = int(choice)
            if choice==1:
                login()
            if choice==2:
                signup()
            if choice==3:
                about()
        except:
            print(colored("Program terminating","red",attrs = ['reverse','blink']))
            time.sleep(2)
            break
home()  #called home function to execute first and run the program eventually
