
import time
import datetime
#from os import system, name, path
import os

currenttimefull = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
logf = open(currenttimefull+".txt","a+")
global currentLine
currentLine = ""
global loopedno
loopedno = 0
run = True
Debug = True
crashMsg = ""
f = ""

info  = "INFO"
note  = "INFO"
debug = "INFO"
warn  = "WARN"
err   = "ERROR"
error = "ERROR"
fatal = "FATAL"
crash = "FATAL"
kernel= "Kernel"
top   = "Kernel"
root  = "Kernel"
main  = "Main"
load  = "Loader"
menu  = "Menu"
svr   = "Server"
server= "Server"

logf.write("==== NOTEPAD-- BY MMK21 ====")
print("Loading Notepad-- by MMK21...")
status = "loading"  

def log(msgtype,msg,thread = "Main"):
    currenttime = datetime.datetime.now().strftime("%H:%M:%S")
    logf.write("\n"+"["+currenttime+"] ["+thread+"/"+msgtype+"]: "+msg)

def clear(watermark = True): 
    # This bit's adapted from https://www.geeksforgeeks.org/clear-screen-python/
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 
    if watermark:
        print(">>>>>> Notepad--")

def shutdown(exitcode = -1):
    clear()
    print(">>>>")
    print(">>>")
    print(">>")
    log(info,"Freezing session",svr)
    log(info, "Stopping server",svr)
    print("Saving world...")
    log(info, "Saving file...",svr)
    log(info, "Saving chunks",svr)
    if f != "": f.close()
    global workfile
    workfile = workfile
    log(info, "ThreadedAnvilChunkStorage ("+workfile+"): All chunks are saved",svr)
    workfile = ""
    exitcode = str(exitcode)
    log(info, "Stopping! [Code "+exitcode+"]",top)
    exitcode = int(exitcode)
    logf.close()
    time.sleep(1)
    raise SystemExit
    #> == EXIT CODES ==
    #  -1: Unknown
    #   0: Window closed
    #   1: User entered 'quit'
    #  99: Crash

def readLineNo(lineNo):
    currentLineNo = 0
    while currentLineNo < lineNo:
        currentLine = f.readline()
        currentLineNo = currentLineNo + 1
    return currentLine

def mainLoop():

    clear()
    global loopedno
    loopedno = loopedno + 1
    loopedno = str(loopedno)
    log(note, "Starting Main Loop #" + loopedno)
    loopedno = int(loopedno)

    print(">>>> Work File: "+workfile+"")
    global currentLine
    if currentLine != "":
        print(">>> "+currentLine)
    else:
        print(">>> "            )
    print(">> Commands: help, goto <line>, quit")
    usrCmdAll = input("> ")
    usrCmd = usrCmdAll.split(' ', 1)[0]
    try:
        param1 = usrCmdAll.split(' ', 1)[1]
    except:
        param1 = ""

    log(info, 'User entered command "'+usrCmdAll+'". Starting command parser.')
    if usrCmd == "help":
        clear()
        log(note,"Rendering help menu")
        print(">>>>")
        print(">>>")
        print(">> Commands: help, goto <line>, quit")
        print("=== HELP MENU ===")
        print("")
        print("GOTO: View a line of the Work File. Fails if no file is open. Usage: goto <line>")
        print("HELP: Display all commands. Usage: help")
        print("QUIT: Exit Notepad--. Usage: quit")
        print("")
        print("< Join r/CactusClub >")
    elif usrCmd == "quit" or usrCmd == "exit" or usrCmd == "stop" or usrCmd == "close":
        run = False
        shutdown(1)
    elif usrCmd == "goto":
        if status == "fileopen":
            if param1.isnumeric():
                param1 = int(param1)
                output = readLineNo(param1)
                if output == "":
                    print("Could not find that line!")
                    log(err,"Command failed! IllegalArgumentError on line 1: "+usrCmd+"<--[HERE] Value specified is larger than maximum possiable value.")
                else:
                    print(output)
                    currentLine = output.rstrip()
            else:
                log(err, "Could not parse command. Error on line 1: "+usrCmd+"<--[HERE] Invalid parameter(s).")
                print("Invalid parameter(s)!")
        else:
            print("You cannot use this command at the moment.")
    else:
        log(err, "Could not parse command. Error on line 1: "+usrCmd+"<--[HERE] Unknown command.")
        print("Unknown or incomplete command, see below for error")
        print(usrCmd+"<--[HERE]")
    
    input("Press enter to continue...")

log(info,"Loaded all functions",load)
log(info, "Setting user: Default",load)
log(info, "Join r/CactusClub",root)
time.sleep(1)
status = "homescreen"
print("Done!")

try:

    global workfile
    workfile = "WorkFile.txt"
    f = open("WorkFile.txt","r+")
    log(info,"Opened "+workfile,menu)
    status = "fileopen"

    while run:
        # Reset variables:
        global currentLineNo
        currentLineNo = 0
        f.seek(0)

        mainLoop()
except Exception as crashMsg:
    crashMsg = str(crashMsg)
    if run:
        log(crash,"An exception has occoured and the process has crashed.",top)
        log(crash,crashMsg,top)
        print("Notepad-- has crashed! Press enter to close the window.")
        print("The crash message is:")
        print("\t",crashMsg)
        input()
        shutdown(99)