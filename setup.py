import os
import time as t
from colorama import Fore, Back, Style
usr = os.getlogin()

state = input("Would you like to install pps?\n"+Fore.YELLOW +"Please beware overinstallation can courrpt the program"+Fore.RESET+"\n[Y/n]: ")
if (state == "Y" or state == "y"):
    pass
elif (state == "n" or state == "N"):
    print("Aborted by user!")
    exit()

print("installing requirements...")
t.sleep(3)
os.system("pip install maskpass --break-system-packages")





print("Setting up command line interface...")
f = open("/home/"+usr+"/.bashrc", "a")
f.write("alias pps='python3 /home/"+usr+"/Desktop/programming/password-saver/program.py'")
f.close()
t.sleep(3)
print("Reinitializing session configuration ...")
t.sleep(3)



os.system("clear")
import maskpass
print("[PPS] please set up master password")
password = maskpass.askpass(mask="")

f = open("/home/"+usr+"/pps.pass", "a")
f.write(password)
f.close()

print("PPS: command line interface was successfuly added")
t.sleep(2)
print("Terminal session was successfuly reinitialized...")
t.sleep(2)
print("Program was successfuly installed!")
print("use pps -h for manual")



print(Fore.YELLOW + "PPS: User was logged into a new session, if exited to previous session program will not work!")
os.system("exec bash --login")