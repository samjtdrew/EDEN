#APPLOADER

import os
import platform
from datetime import datetime
import csv
import sys
from getpass import getpass
import time
import requests

def error(symptom):
    timestamp = datetime.now()
    with open("C:/Users/Sam/OneDrive/Documents/Programming Languages/Python/Project EDEN/DataBases/errortable.csv") as ErrorTable: #consulting symptom table to locate diagnosis
        csv_reader = csv.reader(ErrorTable, delimiter=',')
        for row in csv_reader:
            if row[0] == symptom:
                errorresult = row[1]
                errorcode = row[2]
                break
            else:
                pass
        ErrorTable.close()
    clog = open(mwd + "/ErrorLog/"+ str(timestamp).replace(":", ".") + ".log", "x")
    clog.write("Error Reason: " + symptom)
    clog.write("\nTime Of Error: " + str(timestamp))
    clog.write("\nResult Of Error: " + errorresult) #consult symptom table
    clog.write("\nError Code: " + errorcode) #consult symptom table
    clog.close()
    return errorcode

#collect platform data
print(">> Launching EDEN Version 1.0")
print(">> OS - " + platform.system())
OSNAME = platform.system()
print(">> OS Version - " + platform.version())
OSVERSION = platform.version()
OS = platform.platform()

#check log viablility and scout cwd
cwd = os.getcwd()
cwd = cwd.replace("\\", "/")
os.chdir("../")
mwd = os.getcwd()
mwd = mwd.replace("\\", "/")
os.chdir(cwd)
pid = os.getpid()

if os.path.exists(mwd + "/ErrorLog/errorcount.conf") == True:
    pass
else:
    try:
        os.makedirs(mwd + "/ErrorLog")
        errordir = open(mwd + "/ErrorLog/errorcount.conf", "w+")
        errordir.write("0")
        errordir.close()
        print(">> Error Log Created")
    except:
        errortype = "Error Log Cannot Be Created"
        print(">> ERROR - " + errortype)
        print(">> ABORTING STARTUP >> CRITICAL ERROR >> DETAILS UNAVAILABLE")
        input()
        quit()

#import databases
print(">> Locating DataBases")
if os.path.exists(mwd + "/DataBases") == True:
    print(">> DataBases Found")
else:
    print(">> Missing Required DataBases\n>> Attempting To Import DataBases")
    try:
        os.makedirs(mwd + "/DataBases")
        print(">> DataBases Directory Created")
    except:
        errortype = "DataBase Directory Creation Failed"
        print(">> ERROR - " + errortype)
        print(">> ABORTING STARTUP >> CRITICAL ERROR >> DETAILS UNAVAILABLE")
        input()
        quit()
    try:
        req = requests.get("https://github.com/TikkaDog222/EDENdatabase/raw/main/errortable.csv", allow_redirects=True)
        open(mwd + "/DataBases/errortable.csv", "wb").write(req.content)
        print(">> ErrorTable.csv DataBase Imported From Github")
    except:
        errortype = "ErrorTable.csv Import Failed - Check Internet Connection"
        print(">> ERROR - " + errortype)
        print(">> ABORTING STARTUP >> CRITICAL ERROR >> DETAILS UNAVAILABLE")
        input()
        quit()
    try:
        req = requests.get("https://github.com/TikkaDog222/EDENdatabase/raw/main/commandindex.csv", allow_redirects=True)
        open(mwd + "/DataBases/commandindex.csv", "wb").write(req.content)
        print(">> CommandIndex.csv DataBase Imported From Github")
    except:
        errortype = "CommandIndex.csv Import Failed - Check Internet Connection"
        print(">> ERROR - " + errortype)
        print(">> ABORTING STARTUP >> CRITICAL ERROR >> DETAILS UNAVAILABLE")
        input()
        quit()

#scout user viability
try:
    if os.path.exists(mwd + "/Users") == True:
        print(">> User Directory Found")
    else:
        os.makedirs(mwd + "/Users")
        print(">> User Directory Creation Complete")
except:
    errortype = "Users Directory Cannot Be Created"
    print(">> ERROR - " + errortype)
    errorcode = error(errortype) #parse error to consult error table
    print(">> ABORTING STARTUP >> ERROR CODE " + errorcode + "\nSee Log At '" + mwd + "/ErrorLog' For More Details")
    input()
    quit()

#scout system directory
try:
    if os.path.exists(mwd + "/SYSTEM") == True:
        print(">> System Directory Found")
    else:
        os.makedirs(mwd + "/SYSTEM")
        time.sleep(0.02)
        os.system("attrib +h /s /d " + "../SYSTEM")
        print(">> System Directory Creation Complete")
        #import SpeechRecognition Files
        print(">> Importing SR Data")
        os.makedirs(mwd + "/SYSTEM/SpeechRecognition")
        req = requests.get("https://github.com/x4nth055/pythoncode-tutorials/blob/master/machine-learning/speech-recognition/16-122828-0002.wav?raw=true", allow_redirects=True)
        open(mwd + "/SYSTEM/SpeechRecognition/16-122828-0002.wav", "wb").write(req.content)
except:
    errortype = "System Directory Cannot Be Created"
    print(">> ERROR - " + errortype)
    errorcode = error(errortype) #parse error to consult error table
    print(">> ABORTING STARTUP >> CRITICAL ERROR >> ERROR CODE " + errorcode + "\nSee Log At '" + mwd + "/ErrorLog' For More Details")
    input()
    quit()

#scout root account
if os.path.exists(mwd + "/CredentialStorage/root.conf") == True:
    pass
else:
    print(">> ERROR - Root Account Not Found")
    try:
        os.makedirs(mwd + "/CredentialStorage")
        root = open(mwd + "/CredentialStorage/root.conf", "x")
        root.write("root,passwd")
        root.close()
        print(">> Root Account Created")
    except:
        errortype = "Root Account Creation Failed"
        print(">> ERROR - " + errortype)
        errorcode = error(errortype) #parse error to consult error table
        print(">> ABORTING STARTUP >> ERROR CODE " + errorcode + "\nSee Log At '" + mwd + "/ErrorLog' For More Details")
        input()
        quit()

#Launch EDEN MAIN
print(">> Build Success")
while True:
    runquery = getpass("Would you like to Start EDEN (y/n)?")
    if runquery.lower() == "y":
        break
    elif runquery.lower() == "n":
        quit()
    else:
        print("Not A Valid Option")
        time.sleep(0.5)

#os.system('python EDEN.py')
import EDEN