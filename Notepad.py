if True:
    # version.json
    ver = "0.2.5"
    isStable = False
    isDev = False
    phase = "Alpha"

import time
import datetime
#from os import system, name, path
import os
import sys
import shutil
import atexit


currenttimefull = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
logf = open(currenttimefull+".txt","a+")
global workfile
workfile = ""
global currentLine
currentLine = ""
global loopedno
loopedno = 0

columns, rows = shutil.get_terminal_size(fallback=(80, 24)) #https://bit.ly/31SGiOo
run = True
debugMode = False
crashMsg = ""
f = ""

info  = "INFO"
note  = "INFO"
debug = "DEBUG"
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

logf.write("==== NOTEPAD-- v"+ver+" BY MMK21 ====")
print("Loading Notepad-- by MMK21...")
global status
status = ["loading"]

def log(msgtype,msg,thread = "Main"):
    if msgtype == debug:
    #if False:
        if debugMode:
            currenttime = datetime.datetime.now().strftime("%H:%M:%S")
            logf.write("\n"+"["+currenttime+"] ["+thread+"/"+msgtype+"]: "+msg)
        else:
            pass
    else:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        logf.write("\n"+"["+currenttime+"] ["+thread+"/"+msgtype+"]: "+msg)

class DebugCrash(Exception):
    pass

log(debug,"Loading function 'clear()'.",load)
def clear(watermark = True): 
    # This bit's adapted from https://www.geeksforgeeks.org/clear-screen-python/
    if os.name == 'nt': 
        _ = os.system('cls') 
    else: 
        _ = os.system('clear') 
    if watermark:
        print(">>>>>> Notepad-- v"+ver)

log(debug,"Loading function 'shutdown()'.",load)
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
    log(debug,"Loading function 'readLineNo()'.",load)
    currentLineNo = 0
    global currentLine
    while currentLineNo < lineNo:
        currentLine = f.readline()
        currentLineNo = currentLineNo + 1
    return currentLine

log(debug,"Loading function 'mainLoop()'.",load)
# log( debug , "Loading function 'mainLoop()' - " +     "loading topbar."     , load )
# log( debug , "Loading function 'mainLoop()' - " + "loading command parser." , load )
def mainLoop():

    global status
    if status != "fileopen" and os.path.isfile("WorkFile.txt"):
        global workfile
        workfile = "WorkFile.txt"
        global f
        f = open("WorkFile.txt","r+")
        log(info,"Opened "+workfile,menu)
        status = ["fileopen"]
    elif os.path.isfile("WorkFile.txt"):
        f.seek(0)
    else:
        log(err,"Could not find a Work File!")

    clear()
    global loopedno
    loopedno = loopedno + 1
    loopedno = str(loopedno)
    log(note, "Starting Main Loop #" + loopedno)
    loopedno = int(loopedno)
    refresh = False

    if status == "fileopen":
        print(">>>> Work File: "+workfile)
    else:
        print(">>>>            "         )
    global currentLine
    readLineNo(currentLineNo)
    if currentLine != "":
        status.append("lineopen")
        print(">>> "+currentLine)
    else:
        print(">>> "            )
    ## Topbar/CmdTips
    print(">> Commands:",end=" ")
    print("help",end=" ")
    if status == "fileopen": print("goto",end=" ")
    print("quit")
    #print(">> Commands: help, goto <line>, quit")

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
        print(">>>> ")
        print(">>>  ")
        print(">>   ")

        print("=== HELP MENU ===")
        print("")
        print("CRASH:   Crashes Notepad--; used for debugging. Usage: crash")
        print("GOTO:    View a line of the Work File. Fails if no file is open. Usage: goto <line>")
        print("HELP:    Display all commands. Usage: help")
        print("QUIT:    Exit Notepad--. Usage: quit")
        print("UP/DOWN: Navigate through the lines in your workfile. Usage: up [count]")
        print("                                                             down [count]")
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
                    currentLine = output.rstrip()
                    print(">>> "+currentLine)
            else:
                log(err, "Could not parse command. Error on line 1: "+usrCmd+"<--[HERE] Invalid parameter(s).")
                print("Invalid parameter(s)!")
        else:
            print("You cannot use this command at the moment.")
    elif usrCmdAll == "":
        refresh = True
    elif usrCmd == "crash":
        log(debug,"Hold down F3 + C like it's 1999")
        raise DebugCrash("Manually triggered debug crash")
    else:
        log(err, "Could not parse command. Error on line 1: "+usrCmd+"<--[HERE] Unknown command.")
        print("Unknown or incomplete command, see below for error")
        print(usrCmd+"<--[HERE]")
    
    if refresh:
        log(debug,"Refreshing Command Bar.")
        refresh = False
    else:
        input("Press enter to continue...")

log(debug, "Debug mode is enabled.",kernel)
log(info,"Loaded all functions",load)
atexit.register(shutdown, 0)
log(info, "Setting user: Default",load)
log(info, "Join r/CactusClub",root)
time.sleep(1)
status = ["homescreen"]
print("Done!")

try:
    while run:
        # Reset variables:
        global currentLineNo
        currentLineNo = 0

        mainLoop()
except Exception as crashMsg:
    crashMsg = str(crashMsg)
    if run:
        log(crash,"An exception has occoured and the process has crashed.",top)
        log(crash,crashMsg,top)
        clear()
        print(">>>>")
        print(">>>")
        print(">>")
        print("Notepad-- has crashed! Please press enter to close the window.")
        print("The crash message is:")
        print("\t",crashMsg)
        input()
        shutdown(99)