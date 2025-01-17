import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

from functions import *

print(Fore.CYAN + Style.BRIGHT + "******************************************************************")
with open("password.txt","r") as f:
    password = f.read().strip()
    pssd(password)


print(Fore.MAGENTA + Back.WHITE + Style.BRIGHT + "WELCOME TO THE 'BANK MANAGEMENT SYSTEM'")
print()
print("-----------------------------------------------")

user_input = '''1) Enter 1 to deposite money.
2) Enter 2 to withdraw money.
3) Enter 3 to see your details.
4) Enter 4 to create a new account.
5) Enter 5 to delete your existing account.
6) Enter 6 to exit.
7) Enter 7 to reset password.'''

print(Fore.CYAN + user_input)

while True:
    print("--------------------------------------------")
    print()
    choice = int(input(Fore.CYAN + Style.BRIGHT +  "Enter your choice: "))
    print(Style.RESET_ALL)
    if(choice==4):
        new_account()
        
    elif(choice==3):
        acc_no = input("Enter your account number: ")
        info(acc_no)

    elif(choice==1):
        acc_no = input("Enter your account number: ")
        deposite(acc_no)

    elif(choice==2):
        acc_no = input("Enter your account number: ")
        withdraw(acc_no)

    elif(choice==5):
        acc_no = input("Enter your account nhumber: ")
        print(Fore.RED + Style.BRIGHT + "WARNING: Your account will be permanently deleted.")
        confirmation = int(input("Enter 1 to conitnue or 0 to cancle."))
        if(confirmation==0):
            print(Fore.YELLOW + Style.BRIGHT + "Your account is not deleted.")
        
        elif(confirmation==1):
            delete(acc_no)


    elif(choice==6):
        print("THE PROGRAM IS EXITED.")
        break
    
    elif(choice==7):
        while True:
            confirm = int(input(Fore.CYAN + Style.BRIGHT + "Do you really want to reset password.\nEnter 1 to continue or 0 to quit."))
            print(Style.RESET_ALL)
            if(confirm==1):
                with open("password.txt","r") as f:
                    password = f.read().strip()
                    reset(password)
                    break
            elif(confirm==0):
                print(Fore.YELLOW + Style.BRIGHT + "Password is not changed.") 
                break
            else:
                print("Enter a valid choice.")      
                
                        

    else:
        try:
            raise ValueError()
        except:
            print(Fore.RED + Style.BRIGHT + "Invalid choice.\nPlease enter a valid choice.")

print(Fore.MAGENTA + Back.WHITE + Style.BRIGHT + "THANK YOU FOR USING 'BANK MANAGEMENT SYSTEM'")
print(Style.RESET_ALL)