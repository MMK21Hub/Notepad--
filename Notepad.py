
import time

print("Loading Notepad-- by MMK21...")
status = "loading"
 
from os import system, name  

run = True

def clear(): 
    # This bit's taken from https://www.geeksforgeeks.org/clear-screen-python/
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def shutdown():
    clear()
    print("Saving world...")
    f.close
    time.sleep(1)
    raise SystemExit

def readLineNo(lineNo):
    currentLineNo = 0
    while currentLineNo < lineNo:
        currentLine = f.readline()
        currentLineNo = currentLineNo + 1
    return currentLine

def mainLoop():
    clear()

    print("== Commands: help, goto <line>, quit ==")
    usrCmdAll = input("> ")
    usrCmd = usrCmdAll.split(' ', 1)[0]
    try:
        param1 = usrCmdAll.split(' ', 1)[1]
    except:
        param1 = ""

    if usrCmd == "help":
        clear()
        print("=== HELP MENU ===")
        print("")
        print("GOTO: View a line of the Work File. Fails if no file is open. Usage: goto <line>")
        print("HELP: Display all commands. Usage: help")
        print("QUIT: Exit Notepad--. Usage: quit")
        print("")
        print("< Join r/CactusClub >")
    elif usrCmd == "quit" or usrCmd == "exit" or usrCmd == "stop" or usrCmd == "close":
        shutdown()
    elif usrCmd == "goto":
        if status == "fileopen":
            if param1.isnumeric():
                param1 = int(param1)
                output = readLineNo(param1)
                if output == "":
                    print("Could not find that line!")
                else:
                    print(output)
            else:
                print("Invalid parameter!")
        else:
            print("You cannot use this command at the moment.")
    else:
        print("Unknown or incomplete command, see below for error")
        print(usrCmd+"<--[HERE]")
    
    input("Press enter to continue...")

time.sleep(1)
status = "homescreen"
print("Done!")

f = open("WorkFile.txt","r+")
status = "fileopen"

while run:
    # Reset variables:
    global currentLine
    currentLine = 0
    global currentLineNo
    currentLineNo = 0
    f.seek(0)

    mainLoop()
    print("t")