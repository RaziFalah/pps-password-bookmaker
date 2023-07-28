import os
import time as t
usr = os.getlogin()
state = input("Would you like to uninstall pps for "+usr+"? [y/N]: ")
if (state == "Y" or state == "y"):
    t.sleep(3)
    print("sorry to see you go!")
    t.sleep(2)
    print("Uninstalling pps...")
    with open("/home/"+usr+"/.bashrc", "r") as f:
        lines = f.readlines()
    with open("/home/"+usr+"/.bashrc", "w") as f:
        for line in lines:
            if line.strip("\n") != "alias pps='python3 /home/"+usr+"/Desktop/programming/password-saver/program.py'":
                f.write(line)
    print("PPS: pps was successfuly uninstalled from system")
    t.sleep(3)
    print("Reinitializing session configuration ...")
    t.sleep(3)
    t.sleep(2)
    print("Cleaning...")
    os.system("rm /home/"+usr+"/pps.pass")
    t.sleep(2)
    print("Done")
    os.system("exec bash --login")


elif (state == "n" or state == "N"):
    print("Aborted by user!")
else:
    print("unkown option!")
    print("Aborted by session!")
