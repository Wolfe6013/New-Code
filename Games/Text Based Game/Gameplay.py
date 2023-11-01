import random
import time
import pyautogui
import keyboard

time.sleep(1)

x = 0
y = 0

Alive = True

CommandsList = ["North","South","East","West"]
PreviousResult = "\n\n\n\n\nYou search the forest, and find something.\n\n\n\n\n"

def Commands():
    print("The Commands are as follows: ",end="")
    length = len(CommandsList)
    for x in CommandsList:
        if x == CommandsList[length-1]:
            print(f"{x}.",end="")
        else:
            print(f"{x}, ",end="")
    print()

def Info(x,y):
    NoText = True
    print(PreviousResult)
    FillerSpaces = 19
    if x == 0 and y == 0:
        CommandsList.append("East")
        print("As you walk forward you encounter a large stone door. You have finally found it.\nNorth Korea. You have searched for years to find a way to escape from Los Angele\ns. Willian Afton cannot get to you when you are in NK. You will be safe. You jus\nt need to brave this dungeon first. The door is to the East.")
        FillerSpaces -= 4
    if x == 1 and y == 0:
        CommandsList.append
    for x in range(FillerSpaces):
        print()

while Alive:
    CommandsList.clear()
    print(f"\n\n\n\n\n\n\n\nMap! {x},{y}\n\n\n\n\n")
    Info(x,y)
    print()
    Commands()
    print()
    P1Input = input()

    if "North" in CommandsList and P1Input == "North":
        ActDone = True
        y += 1
        PreviousResult = "\n\n\n\n\nYou move North.\n\n\n\n\n"

    if "South" in CommandsList and P1Input == "South":
        ActDone = True
        y -= 1
        PreviousResult = "\n\n\n\n\nYou move South.\n\n\n\n\n"
        
    if "East" in CommandsList and P1Input == "East":
        ActDone = True
        x += 1
        PreviousResult = "\n\n\n\n\nYou move East.\n\n\n\n\n"

    if "West" in CommandsList and P1Input == "West":
        ActDone = True
        x -= 1
        PreviousResult = "\n\n\n\n\nYou move West.\n\n\n\n\n"
    
    if P1Input == "Die":
        ActDone = True
        Alive = False

    if ActDone == False:
        PreviousResult = "\n\n\n\n\nInvalid Command.\n\n\n\n\n"

for x in range(100):
    print("\n\n\n\n\n")
input("Thank you for playing!")