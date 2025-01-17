# FUNCTIONS

import time 
import getpass
import hashlib
import random as rd
import csv
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

#------------------------------------------------------------------------------------------------------------------------

# deposite function
def deposite(acc_no):
    file = open("data.csv","r")
    reader = csv.reader(file)
    l = []
    while True:
        try:
            amount = int(input("Enter the amount you want to deposite: "))
            if(amount<0):
                raise ValueError()
            else:
                for row in reader:
                    if(row[4]==acc_no):
                        row[3]=str(int(row[3])+amount)
                        print(Back.WHITE +  Fore.MAGENTA + Style.BRIGHT + f"THANK YOU FOR DEPOSITING {amount} RUPEES.")

                    l = l + [row] 
                break     
        except:
            print(Fore.RED + Style.BRIGHT + "Please enter a valid amount.")

    for list in l:
        if(list[4]==acc_no):
            break

    else:
        print(Fore.RED + Style.BRIGHT + f"No aacount with account number {acc_no} exist!")

    file.close()

    file = open("data.csv","w",newline="")
    writer = csv.writer(file)
    for row in l:
        writer.writerow(row)
    file.close()

    
#-------------------------------------------------------------------------------------------------------------------------------

# withdraw function
def withdraw(acc_no):
    file = open("data.csv","r")
    reader = csv.reader(file)
    l = []

    while True:
        try:
            amount = int(input("Enter the amount you want to withdraw."))
            if(amount<0):
                raise ValueError()
            else:
                for row in reader:
                    if(row[4]==acc_no):
                        if(int(row[3])>=amount):
                            row[3]=str(int(row[3])-amount)
                            print(Back.WHITE + Fore.MAGENTA + Style.BRIGHT + f"THANK YOU FOR WITHDRAWING {amount} RUPEES.")
                        else:
                            print(Fore.RED + Style.BRIGHT + "WITHDRAWAL FAILED DUE TO INSUFFICIENT BALANCE.")
                    l = l + [row]  
                
                break

        except:
            print(Fore.RED + Style.BRIGHT + "Please enter a valid amount.")

               
    for list in l:
        if(list[4]==acc_no):
            break

    else:
        print(Fore.RED + Style.BRIGHT + f"No aacount with account number {acc_no} exist!")

    file.close()

    file = open("data.csv","w",newline="")
    writer = csv.writer(file)
    for row in l:
        writer.writerow(row)
    file.close()

    
#--------------------------------------------------------------------------------------------------------------------------

# making new account
def new_account():

    while True:
        
        name = input("Enter your full name: ")
        name2 = name.title()
        if(name2.find(" ")!=-1):
            l = name2.split()
            if(l[0].isalpha()==False or l[1].isalpha()==False):
                print(Fore.RED + Style.BRIGHT + "Please enter valid name.")
                continue
                
        else:
            print(Fore.RED + Style.BRIGHT + "Please enter a valid name.")
            continue
        
        while True:
            try:
                phn = int(input("Enter your phone number: "))
                if(phn<1000000000 or phn>9999999999):
                    raise ValueError()
                else:
                    break
            except:
                print(Fore.RED + Style.BRIGHT + "Enter a valid phone number.")
        
        while True:
            email = input("Enter your email: ")
            email2 = email.lower()
            if(email2.find("@")!=-1 and email2.find(".")!=-1):
                break

            else:
                print(Fore.RED + Style.BRIGHT + "Please enter a valid email address.")

        
        Bank_Balance = int(0)

                      
        acc_no = rd.randint(100000000000,1000000000000)

        date = time.strftime('%d/%m/%Y')
        Time = time.strftime('%H:%M:%S')
        while True:
            file = open("data.csv","r")
            reader = csv.reader(file)

            for i in reader:
                if(i[4]==acc_no):
                    acc_no = rd.randint(100000000000,1000000000000)
                    break
            else:
                file.close()
                break

        
        l = [name2,phn,email2,Bank_Balance,acc_no,date,Time]
        file = open("data.csv","a",newline="")
        w=csv.writer(file)
        w.writerow(l)
        file.close()

        
        print(Fore.GREEN + Style.BRIGHT + f"Dear {name}, Your data is submitted successfully!")
        print(Fore.YELLOW + f"Your account number is {acc_no}. Please note it for future use.")   
        print("_______________________________________________________")
        print()

        choice1 = int(input("Enter 1 to create another account or 0 to quit: "))
        if(choice1==0):
            break
        if(choice1==1):
            continue
#---------------------------------------------------------------------------------------------------------------------------        
        
# displaying info
def info(acc_no):
    
    file = open("data.csv","r")
    reader = csv.reader(file)
    l = []

    for i in reader:
        if(i[4]==acc_no):
            print(Fore.MAGENTA + Back.WHITE + Style.BRIGHT + "Your details:")
            print()
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Name",i[0]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Phone Number",i[1]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Email",i[2]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Bank Balance",i[3]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Account Number",i[4]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Account created on ",i[5]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")
            print(Fore.MAGENTA + Back.WHITE +"|%20s | %20s|"%("Time",i[6]))
            print(Fore.MAGENTA + Back.WHITE +"---------------------------------------------")

            print()
        l = l + [i]   
    for list in l:
        if(list[4]==acc_no):
            break

    else:
        print(Fore.RED + Style.BRIGHT + f"No aacount with account number {acc_no} exist!")
    
    file.close()
    print()


#------------------------------------------------------------------------------------------------------------------------------------

# deleting an account
def delete(acc_no):
    file = open("data.csv","r")
    reader = csv.reader(file)

    l = []
    for row in reader:
        if(row[4]==acc_no):
            print(f"Account with account number {acc_no} is permanently deleted.") 
            continue

        l = l + [row]  

    for list in l:
        if(list[4]==acc_no):
            break

    else:
        print(Fore.RED + Style.BRIGHT + f"No aacount with account number {acc_no} exist!")     

    file.close()

    file = open("data.csv","w",newline="")
    writer = csv.writer(file)
    for row in l:
        writer.writerow(row)
    file.close()


#-----------------------------------------------------------------------------------------------------------------------------------------------

# password
def pssd(password):

    while True:
        try:
            user_input = getpass.getpass("Enter your password: ")
            if not isinstance(user_input,str):
                raise ValueError()
            
            message = user_input.encode('utf-8')
            hsh = hashlib.sha256(message).hexdigest()

            if(hsh==password):
                print(Fore.GREEN + Style.BRIGHT + "Correct password!")
                break
            
            else:
                print(Fore.RED + Style.BRIGHT + "Incorrect password!")

        except:
            print(Fore.RED + Style.BRIGHT + "Password must be a string.")

    
#---------------------------------------------------------------------------------------------------------------------------------------------

# reset password
def reset(password):
    while True:
        try:
            old = getpass.getpass("Enter old password: ")
            if not isinstance(old,str):
                raise ValueError()
            else:
                message = old.encode('utf-8')
                old2 = hashlib.sha256(message).hexdigest()
                if(old2==password):
                        print(Fore.GREEN + Style.BRIGHT + "Correct password!")
                        break
                
                else:
                    print(Fore.RED + Style.BRIGHT + "Incorrect password!")
                
        except:
            print(Fore.RED + Style.BRIGHT + "Password must be a string.")

    while True:
            try:
                new = getpass.getpass("Enter new password: ")
                if not isinstance(new,str):
                    raise ValueError()
                    
                else:
                    break
            except:
                print(Fore.RED + Style.BRIGHT + "Password must be a string.")

    message = new.encode('utf-8')
    new2 = hashlib.sha256(message).hexdigest()
        
    with open("password.txt","w") as f:
        f.write(new2)

    print(Fore.YELLOW + Style.BRIGHT + "Password updated successfuly!")