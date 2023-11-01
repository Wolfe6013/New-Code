import os
import random
import time
import pyautogui
import keyboard

run = True
menu = True
play = False
key = False

HP = 50
MaxHP = HP
ATK = 3
gold = 0
x = 0
y = 0

map = [["tile1","tile2","tile3"],
       ["tile4","tile5","tile6"],
       ["tile7","tile8","tile9"]]

y_len = len(map)-1
x_len = len(map[0])-1

current_tile = map[y][x]

biome = {
    "tile1": {
        "t": "TILE1",
        "e": True},
    "tile2": {
        "t": "TILE1",
        "e": False},
    "tile3": {
        "t": "TILE1",
        "e": True},
    "tile4": {
        "t": "TILE1",
        "e": False},
    "tile5": {
        "t": "TILE1",
        "e": True},
    "tile6": {
        "t": "TILE1",
        "e": True},
    "tile7": {
        "t": "TILE1",
        "e": True},
    "tile8": {
        "t": "TILE1",
        "e": True},
    "tile9": {
        "t": "TILE1",
        "e": False}
    }

e_list = ["Rat","2 Rats","3 Rats","18 Rats","Goblins","Kim-Jong-Un Cultist","Free Speech"]

mobs = {}

def clear():
    os.system("cls")

def draw():
    print("###--------------------###")

def save():
    statsList = [
        name,
        str(HP),
        str(MaxHP),
        str(ATK),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt","w")
    for item in statsList:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        draw()
        print("1. NEW GAME\n2. LOAD GAME\n3. CONTROLS\n4. QUIT GAME")
        draw()
        choice = input("#")
        validChoice = False
        if choice == "1":
            validChoice = True
            clear()
            name = input("What is your name? ")
            if name == "Dejan":
                for x in range(50):
                    print("Dejan is a bad person.")
                time.sleep(1)
                clear()
                quit()
            menu = False
            play = True
            print(f"Hello {name}.")

        if choice == "2":
            validChoice = True
            try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 8:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    MaxHP = int(load_list[2][:-1])
                    ATK = int(load_list[3][:-1])
                    gold = int(load_list[4][:-1])
                    x = int(load_list[5][:-1])
                    y = int(load_list[6][:-1])
                    key = bool(load_list[7][:-1])
                    clear()
                    print(f"Welcome back {name}!")
                    menu = False
                    play = True
                else:
                    print("Corrupted save file!")
                    input(">")
            except OSError:
                print("No loadable save file!")
                input(">")

        if choice == "3":
            validChoice = True
            clear()
            print("___---Controls---___\n\nHey chat, there is no controls yet. Lucky you!\n")
            input(">")

        if choice == "4":
            validChoice = True
            clear()
            quit()

        if validChoice == False:
            print("That is not a valid choice. Only type the number of the option you wish to pick.")
            time.sleep(1)

    while play:
        clear()
        save()
        draw()
        print("LOCATION:",biome[map[y][x]]["t"])
        draw()
        print(f"NAME: {name}")
        print(f"HP: {HP}/{MaxHP}")
        print(f"ATK: {ATK}")
        print(f"GOLD: {gold}")
        print(f"COORDS: ({x},{y})")
        draw()
        print("0 - Save and Quit")
        n_option = False
        s_option = False
        e_option = False
        w_option = False

        if y > 0:
            print("1 - NORTH")
            n_option = True
        if x < x_len:
            print("2 - EAST")
            e_option = True
        if y < y_len:
            print("3 - SOUTH")
            s_option = True
        if x > 0:
            print("4 - WEST")
            w_option = True
        draw()
        dest = input(">")
        keyBind = False

        if dest == "0":
            keyBind = True
            save()
            play = False
            menu = True
        if dest == "1" and n_option == True:
            keyBind = True
            if y > 0:
                y -= 1
        if dest == "2" and e_option == True:
            keyBind = True
            if x < x_len:
                x += 1
        if dest == "3" and s_option == True:
            keyBind = True
            if y < y_len:
                y += 1
        if dest == "4" and w_option == True:
            keyBind = True
            if x > 0:
                x -= 1
        
        if keyBind == False:
            print("Invalid command.")
            time.sleep(1)   