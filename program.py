import time as t
import sys as system
from colorama import Fore, Back, Style
import os






#Functions start

def on_login_pass():
    pass




#Functions end


usr = os.getlogin()






if(len(system.argv) == 1):
    print(Fore.RED + "Fatal error: pps expects at least 1 argument but was given none!" + Fore.RESET)
    print("Use 'pps -h' or 'pps man' to view options!")
    exit()
elif(len(system.argv) == 2):
    pass
elif(len(system.argv) > 11):
    print(Fore.RED + "Fatal error: to many arguments was given ("+str(len(system.argv) - 2)+")")
    exit()
else:
    print(Fore.YELLOW + "Ignoring non fatal errors! ("+str(len(system.argv)-1)+")" + Fore.RESET)


with open('/home/'+usr+'/pps.pass') as f:
    master_password = f.readline()

import maskpass
print("[PPS] master password login")
check_master_password = maskpass.askpass(mask="")

tries = 3
while(master_password != check_master_password and tries >= 0):
    print("Authentication failed, please try again")
    tries = tries - 1
    check_master_password = maskpass.askpass(mask="")

if tries == -1:
    print("Too many tries, please try again later")
    exit()

if(system.argv[1] == "-h" or system.argv[1] == "man"):
    print(""" 
    pps -s [description] [password] : use to store on-login password
    """)
    exit()
elif(system.argv[1] == "-s"):
    if(len(system.argv) == 4):
        on_login_pass()
    else:
        print(Fore.RED + "Fatal error: pps -s expects at least 2 argument but was given "+str(len(system.argv)-2)+" !" + Fore.RESET)
        print("Use 'pps -h' or 'pps man' to view options!")
        exit()
else:
    print("PPS: " + Fore.YELLOW + " unkown option! ("+system.argv[1]+")" + Fore.RESET)
    print("Use 'pps -h' or 'pps man' to view options!")
    exit()






print("No errors were encounterd!")
