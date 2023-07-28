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
            if line.strip("\n") != "alias pps='python3 /home/"+usr+"/pps-password-bookmaker/program.py'":
                f.write(line)
    print("PPS: pps was successfuly uninstalled from system")
    t.sleep(3)
    print("Reinitializing session configuration ...")
    t.sleep(3)
    t.sleep(2)
    print("Cleaning...")
    os.system("rm /home/"+usr+"/pps-password-bookmaker/pps.pass")
    os.system("rm pps_config/data/pass.list")
    os.system("rmdir pps_config/data")
    os.system("rmdir pps_config")
    t.sleep(2)
    print("Done")
    os.system("exec bash --login")


elif (state == "n" or state == "N"):
    print("Aborted by user!")
else:
    print("unkown option!")
    print("Aborted by session!")
