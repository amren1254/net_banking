# Program for managing record of user in bank



# Importing module time
import time

# Importing module CSV for performing operation on csv files such as updation, deletion, Insertion....
import csv

# Login module for logging in the user....

def login():
    data=[]
    read=csv.reader(open('n1.csv'))   # CSV file is opened in the read mode....
    for row in read:
        data.append(row)
    uname=input('Enter your username:')
    for i in range(0,len(data)):
        if uname==data[i][4]:
            b=i
            
            print ('Correct Username')
            passw=input('Enter your password')
            if passw==data[b][5]:
                print ('Correct Password\n'),profile(b)     # Profile function is called with an argument....
            else:
                print ('Wrong password')

#  Signup module to register a new user....

def signup():
    print ("\n------ Welcome to the Signup -------"),time.sleep(2)    # Time attribute sleep is called to delay for 2 seconds....
    name=input('Enter your name')
    age=input('\nEnter your age')
    address=input('\n Enter your address')
    email=input('\n Enter your email')
    username=input('Enter your username')
    password=input('\n Enter your password')
    first=input('How much do you want to credit as your initial balance(min. 3000)')
    print ('\n _____New user created----')
    f1=open('n1.csv','a')           # CSV file is opened in append mode to write all the data of new user....
##  Write operation is performed in csv file....
    f1.write(name)
    f1.write(',')
    f1.write(age)
    f1.write(',')
    f1.write(address)
    f1.write(',')
    f1.write(email)
    f1.write(',')
    f1.write(username)
    f1.write(',')
    f1.write(password)
    f1.write(',')
    f1.write(first)
    f1.write('\n')
    f1.close()       # csv file is closed after write operation....
##    print '\n\n\tWelcome for login'
    time.sleep(2)               # Time attribute sleep is called to delay for 2 seconds....
    home()                      # Home function is called without any argument....

#  Home module as initial interface for user....

def home():
    print ('\n\t\t::::::Welcome :::::')
    ch=int(input('\t\t\nEnter your choice \n 1.Login\n\n 2.Signup\n\n 3.Exit'))
    if(ch==1):
     login()                 # Login function is called without any argument....
    elif(ch==2):
     signup()                # Signup function is called without any argument....
    else:
     print ('\t\tProgram Terminated')
        #login()
        
 
# Credit module for credit operation ....

def credit(r):
    print ('\n\t\t---Welcome to credit panel----'),time.sleep(2)
    cred= int(input('\n\t\t Enter the amount you want to credit'))
    data=[]
    read=csv.reader(open('n1.csv'))         # CSV file is opened in the read mode....
    for row in read:
        data.append(row)
    
    data[r][6]=(eval(data[r][6])+cred)
    f1=open('n1.csv','w')                   # CSV file is opened for write operation....
    writer=csv.writer(f1)
    writer.writerows(data)
    f1.close()                              # CSV file is closed after write operation
        
    print ('\n\t\t Now your a/c balance is '),data[r][6]
    profile(r)

# Debit module for debit operation....

def debit(r):
    print ('\n\t\t Welcome to the Debit panel'),time.sleep(2)
    deb=input('\n\t\t Enter the amount you want to debit')
    data=[]
    read=csv.reader(open('n1.csv'))         # CSV file is opened in the read mode....
    for row in read:
        data.append(row)
    
    data[r][6]=(eval(data[r][6])-deb)
    f1=open('n1.csv','w')                   # CSV file is opened for write operation....
    writer=csv.writer(f1)
    writer.writerows(data)
    f1.close()                      # CSV file is closed after write operation....
    
    print ('\nNow your a/c balance is '),time.sleep(2),data[r][6]
    profile(r)                      # Profile function is called with an argument....


#  Transfer module for transfer operation....

def transfer(crr):
    print ('Welcome to the transfer panel')
    acc=input('Enter the username of whom you want to transfer')
    data=[]
    read=csv.reader(open('n1.csv'))
    for row in read:
        data.append(row)
    for i in range(0,len(data)):
        if acc==data[i][4]:
            a=i
            print ('User Found \t\t'),data[a][0],('\n\nYou can proceed')
##        else:
##            print 'Specified user not found'
    amt=int(input('Enter amount to be transferred'))
    data[a][6]=eval(data[a][6])+amt
    data[crr][6]=eval(data[crr][6])-amt
    f1=open('n1.csv','w')
    writer=csv.writer(f1)   # CSV file is opened for write operation....
    writer.writerows(data)
    f1.close()              # CSV file is closed after read and write operation....
    profile(crr)            # Profile function is called with an argument....


# Logout module for logout the user....

def logout():
    ch= input('\nDo you want to logout(y/n)')
    if ch=='y' or ch=='Y':
        f1=open('n1.csv','r')
        f1.close()
        print ('You are logged out')
    home()              # Home module is called without any argument....

# Profile module for user....
def profile(row):
    data=[]
    read=csv.reader(open('n1.csv'))
    for row1 in read:
        data.append(row1)
    print ('\n Welcome\t'),data[row][0]
    print ('\n Your  a/c balance is \t '),data[row][6]
    ch=input('\n What you want to do\n1.Credit\n2.Debit\n3.Transfer\n4.Logout')
    if ch==1:
        credit(row)         # Cedit function is called with an argument....
    if ch==2:
        debit(row)          # Debit function is called with an argument....
    if ch==3:
        transfer(row)       # Transfer function is called with an argument....
    if ch==4:
        logout()            # Logout function is called without any argument....



# Home module is called without any argument....

home()
