import random
import time
import pyautogui
import keyboard

#Make sure every line is exactly 80 char
#37 lines top to bottom.

CommandsList = ["North","South","East","West","Inventory","Search"]
def Commands():
    length = len(CommandsList)
    for x in CommandsList:
        if x == CommandsList[length-1]:
            print(f"{x}.")
        else:
            print(f"{x}, ",end="")

def Input():
    P1Input = input()

def Premap():
    print("--------------------------------------------------------------------------------",end="")
    print("          ",end="")

def Map():
    MapPieces = [
        "           _______     _    | |",
        "    N     |       \   / \   | |",
        "  W-+-E   |  __    \_/   \__/ |",
        "    S     | |  \              /",
        "          | |   \______/\____/"]
    for x in MapPieces:
        Premap()
        print(x)

def Info():
    print(PreviousResult)
    for x in range(20):
        print()

def Setup():
    print()
    print()
    Map()
    print()

def PageEnd():
    print()
    Commands()
    print()
    Input()

Setup()
Info()
PageEnd()