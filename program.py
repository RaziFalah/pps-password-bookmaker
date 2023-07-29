import time as t
import sys as system
from colorama import Fore, Back, Style
import os






#Functions start

def on_login_pass(password, desc):
    print("Processing...")
    f = open("/home/"+usr+"/pps-password-bookmaker/pps_config/data/pass.list", "a")
    f.write("==================================\n|"+desc+"   "+password+"|\n==================================")
    f.close()
    t.sleep(2)
    print("Done")
    exit()


def uninstall(state):
    if(state == "y" or "Y"):
      os.system("python3 /home/"+usr+"/pps-password-bookmaker/uninstall.py")
    else:
      print("Proccess was aborted by user!")
      exit()


#Functions end


usr = os.getlogin()






if(len(system.argv) == 1):
    print(Fore.RED + "Fatal error: pps expects at least 1 argument but was given none! Error code (1)" + Fore.RESET)
    print("Use 'pps -h' or 'pps man' to view options!")
    exit()
elif(len(system.argv) == 2):
    pass
elif(len(system.argv) > 11):
    print(Fore.RED + "Fatal error: to many arguments was given ("+str(len(system.argv) - 2)+") Error code (1)")
    exit()
else:
    pass


with open('/home/'+usr+'/pps-password-bookmaker/pps.pass') as f:
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

if(system.argv[1] == "-h" or system.argv[1] == "-help"):
    print(""" 
    pps -s [description] [password] : use to store on-login password
    pps -v : use to view password list
    pps -uninstall [Yes] : use to remove pps from your system, use the y argu for confirmation
    """)
    exit()
if(system.argv[1] == "man" or system.argv[1] == "-man"):
    os.system("open file:///home/"+usr+"/pps-password-bookmaker/man.html")
elif(system.argv[1] == "-s"):
    if(len(system.argv) == 4):
        on_login_pass(system.argv[2], system.argv[3])
    else:
        print(Fore.RED + "Fatal error: pps -s expects 2 argument but was given "+str(len(system.argv)-2)+" ! Error code (1)" + Fore.RESET)
        print("Use 'pps -h' or 'pps man' to view options!")
        exit()
elif(system.argv[1] == "-uninstall"):
    if(len(system.argv) == 3):
            uninstall(system.argv[2])
    else:
        print(Fore.RED + "Fatal error: pps -uninstall expects 1 argument but was given "+str(len(system.argv)-2)+" ! Error code (1)" + Fore.RESET)
        print("Use 'pps -h' or 'pps man' to view options!")
        exit()
elif(system.argv[1] == "-v" or system.argv[1] == "-view"):
    os.system("cat /home/"+usr+"/pps-password-bookmaker/pps_config/data/pass.list")
    input("\nType anything to exit: ")
    os.system("clear")
    exit()
else:
    print("PPS: " + Fore.YELLOW + " unkown option! ("+system.argv[1]+")" + Fore.RESET)
    print("Use 'pps -h' or 'pps man' to view options!")
    exit()






print("No errors were encounterd but program unexpectedly closed with return code (0)")
