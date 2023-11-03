import os
import random
import time

run = True
menu = True
play = False
floor = 2
x = 4
y = 0

key = False
alive = True

HP = 80
MaxHP = HP
Str = 10
Mana = 10
Wit = 10
Speed = 10

map = [["--------------------"],
       ["--------------------"],
       ["--------------------"],
       ["--------------------"]]

#┣┫┳┻┿┏┓┗┛┃━


if floor == 0:
    map = [["┏━━━━━━━━━━━┓     "],
           ["┃           ┃     "],
           ["┃+━━━━━━━━┓ ┃     "],
           ["┃         ┃ ┃     "],
           ["┣━━━━━━━━━┛ ┣━━━━┓"],
           ["┃>          +    ┃"],
           ["┗━━━━━━━━━━━┻━━━━┛"]]

if floor == 1:
    map = [["┏━━━━━━━━━━━━┳━━━━┓"],
           ["┃            *    ┃"],
           ["┃ ┏┳━━━━━━━┓ ┃    ┃"],
           ["┃ ┗┫       ┃ ┣━━━━┫"],
           ["┃ >┃       + +    ┃"],
           ["┗━━┿━━━━━━━┫ ┃    ┃"],
           ["   ┃       ┃ ┃    ┃"],
           ["   ┃       ┃ ┃    ┃"],
           ["   ┣━━━*━━━┛ ┣━━━━┫"],
           ["   +         +    ┃"],
           ["   ┣━━━+━━━┓ ┃    ┃"],
           ["   ┃       ┃ ┃    ┃"],
           ["   ┃       ┃ ┃    ┃"],
           ["   ┗┳━━━━━━┻$┿━━━━┛"],
           ["    ┃>       ┃     "],
           ["    ┗━━━━━━━━┛     "]]

if floor == 2:
    map = [["┏━━━━━━━━━━━━━━┓"],
           ["┃              ┃"],
           ["┃              ┃"],
           ["┃              ┃"],
           ["┃              ┃"],
           ["┃ ┏━━━━━━━━━━━━┫"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┃            ┃"],
           ["┃ ┗━━━┳━━━━━━━+┫"],
           ["┃    >┃        ┃"],
           ["┃     $        ┃"],
           ["┗━━━━━┻━━━━━━━━┛"]]

y_len = len(map)-1
x_len = len(map[0])-1

listMap = [[],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           [],
           []]

for list in map:
    for row in list:
        for column in row:
            listMap.append(column)

print()
current_tile = map[y][x]

for row in map:
    for column in row:
        if column == current_tile: print("@",end="")
        else: print(column,end="")
    print()
input()

def clear():
    os.system("cls")

def draw():
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")

def save():
    statsList = [
        name,
        str(HP),
        str(MaxHP),
        str(key)
    ]

    f = open("load.txtw")
    for item in statsList:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        draw()
        print(f"│1. NEW GAME\n│2. LOAD GAME\n│3. CONTROLS\n│4. QUIT GAME")
        draw()
        choice = input("│>")
        validChoice = False
        if choice == "1":
            validChoice = True
            clear()
            ("│WHAT IS YOUR NAME? ")
            name = input("│>")
            menu = False
            play = True
            draw()
            print(f"│WELCOME {name}!")
            draw()
            input("│<")

        if choice == "2":
            validChoice = True
            try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 4:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    MaxHP = int(load_list[2][:-1])
                    key = bool(load_list[3][:-1])
                    clear()
                    draw()
                    print(f"│WELCOME BACK {name}!")
                    draw()
                    input("│<")
                    menu = False
                    play = True
                else:
                    print(f"│CORRUPT SAVE FILE!")
                    input("│<")
            except OSError:
                print(f"│NO LOADABLE SAVE FILE!")
                input("│<")

        if choice == "3":
            validChoice = True
            clear()
            print(f"┣━━━━━━━━━━━━━━━━━━CONTROL━━━━━━━━━━━━━━━━━━━━┫\n│\n│TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK\n│HP IS THE AMOUNT OF HEALTH YOU HAVE. DON'T DROP BELOW 0 OR YOU LOSE!\n│ATK IS THE DAMAGE YOU DEAL.\n│AC IS WHAT THE OPPONENT NEEDS TO ROLL TO HIT YOU.\n│MODIFIER IS WHAT YOU ADD TO YOUR ROLL TO HIT.\n│'>' MEANS YOU ARE EXPECTED TO INPUT A COMMAND.\n│'<━┛' MEANS PRESS 'ENTER' TO CONTINUE.\n│")
            input("│<")

        if choice == "4":
            validChoice = True
            clear()
            quit()

        if validChoice == False:
            print(f"│THAT IS NOT A VALID CHOICE. ONLY TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK.")
            input("│<")

    while play:
        clear()
        save()
        draw()
        print(f"│LOCATION: FLOOR {floor}")
        draw()
        for b in range(5):
            print(f"│",end="")
            for a in range(4):
                if a == x and b == y:
                    print(f"━    X     ",end="")
                else:
                    print(f"━ {map[b][a]} ",end="")
            print(f"━┫")

        draw()
        print(f"│NAME: {name}")
        if HP < MaxHP:
            if HP <= MaxHP-5:
                print(f"│HP: {HP}+5/{MaxHP}")
                HP += 5
            else: 
                dif = MaxHP-HP
                print(f"│HP: {HP}+{dif}/{MaxHP}")
                HP += dif
        else:
            print(f"│HP: {HP}/{MaxHP}")
        print(f"│COORDS: ({x},{y})")
        draw()
        print(f"│0 ━ SAVE AND QUIT")
        n_option = False
        s_option = False
        e_option = False
        w_option = False

        if y > 0:
            print(f"│1 ━ NORTH")
            n_option = True
        if y < y_len:
            print(f"│2 ━ SOUTH")
            s_option = True
        if x > 0:
            print(f"│3 ━ WEST")
            w_option = True
        if x < x_len:
            print(f"│4 ━ EAST")
            e_option = True
        draw()
        dest = input("│>")
        validCommand = False

        if dest == "0":
            validCommand = True
            save()
            play = False
            menu = True
        if dest == "1" and n_option == True:
            validCommand = True
            if y > 0:
                y -= 1
                standing = False
        if dest == "2" and s_option == True:
            validCommand = True
            if y < y_len:
                y += 1
                standing = False
        if dest == "3" and w_option == True:
            validCommand = True
            if x > 0:
                x -= 1
                standing = False
        if dest == "4" and e_option == True:
            validCommand = True
            if x < x_len:
                x += 1
                standing = False
        
        if validCommand == False:
            print(f"│INVALID COMMAND")
            standing = True
            input("│<")