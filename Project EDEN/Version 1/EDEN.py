#EDEN MAIN
import os
import sys
from getpass import getpass
import platform
import csv
import time
import AudioListener as al

def TitleScreen():
    print("\n _______ ______  _______ __   _")
    print(" |______ |     \ |______ | \  |")
    print(" |______ |_____/ |______ |  \_|")
    print("                               ")
    print("Version: 1.0")
    print("Platform: Python3.10")

def commandIndex(execute):
    with open(mwd + "/DataBases/commandindex.csv") as CommandIndex:
        csv_reader = csv.reader(CommandIndex, delimiter=',')
        for row in csv_reader:
            if row[0] == execute:
                action = row[1]
                command = row[2]
                #execute the commands in the format listed under the command index
                if row[1] == "execute":
                    exec(row[2])
                    exec(row[3])
                    exec(row[4])
                else:
                    pass
                break
            else:
                pass
        CommandIndex.close()

TitleScreen()
cwd = os.getcwd()
cwd = cwd.replace("\\", "/")
os.chdir("../")
mwd = os.getcwd()
mwd = mwd.replace("\\", "/")
os.chdir(cwd)
pid = os.getpid()
#check credentials
loopconst = True
while loopconst == True:
    user = input("\nUsername: ")
    passwd = getpass(user + "@EDEN Password: ")
    try:
        with open(mwd + "/CredentialStorage/" + user + ".conf", "r") as CredFile:
            takepass = CredFile.read().split(",")
            if passwd == takepass[1]:
                print("Welcome", user)
                if user == "root" and takepass[1] == "passwd":
                    #change password prompt
                    time.sleep(0.02)
                    newpass = getpass("\nPlease Enter New Passord For Root: ")
                    changeroot = open(mwd + "/CredentialStorage/root.conf", "w")
                    changeroot.write("root," + newpass)
                    changeroot.close()
                else:
                    pass
                loopconst = False
            else:
                print("Incorrect Password\nPlease Try Again")
                time.sleep(0.2)
    except:
        print("Incorrect Username\nPlease Try Again")
        time.sleep(0.2)

#check that a root user profile has been created
if os.path.exists(mwd + "/Users/" + user) == True:
    pass
else:
    os.makedirs(mwd + "/Users/" + user + "/Documents")
    os.makedirs(mwd + "/Users/" + user + "/Media")
    os.makedirs(mwd + "/Users/" + user + "/Utilities")
    os.makedirs(mwd + "/Users/" + user + "/Sys")
    #hide 'Sys' directory
    os.system("attrib +h /s /d " + "../Users/" + user + "/Sys")
#setting the user directory to the current user
uwd = mwd + "/Users/" + user
#set the system working directory
swd = mwd + "/Users/" + user + "/Sys"

#Call listener file to setup
while True:
    al.speak("How can i help?")
    statement = al.takeCommand().lower()
    if statement == 0:
        continue
    elif "eden" in statement.lower():
        statement = statement.lower().replace("eden ", "")
        print(statement.upper())
        commandIndex(statement.upper())
    else:
        print("-")