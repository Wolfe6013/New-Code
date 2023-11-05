import os, random, time, sys

run = True
menu = True
play = False
floor = 1
x = 4
y = 1
name = "skibibid"

key = False
alive = True

HP = 80
MaxHP = HP
Strength = 10
Mana = 10
Wit = 10
Dexterity = 10

map = [["--------------------"],
       ["--------------------"],
       ["--------------------"],
       ["--------------------"]]

#┣┫┳┻┿┏┓┗┛┃━


if floor == 0:
    map = ["┏━━━━━━━━━━━┓     ",
           "┃           ┃     ",
           "┃+━━━━━━━━┓ ┃     ",
           "┃         ┃ ┃     ",
           "┣━━━━━━━━━┛ ┣━━━━┓",
           "┃▲          +    ┃",
           "┗━━━━━━━━━━━┻━━━━┛"]

if floor == 1:
    map = ["┏━━━━━━━━━━━━┳━━━━┓",
           "┃            *    ┃",
           "┃ ┏┳━━━━━━━┓ ┃    ┃",
           "┃ ┗┫       ┃ ┣━━━━┫",
           "┃ ▼┃       + +    ┃",
           "┗━━┿━━━━━━━┫ ┃    ┃",
           "   ┃       ┃ ┃    ┃",
           "   ┃       ┃ ┃    ┃",
           "   ┣━━━*━━━┛ ┣━━━━┫",
           "   +         +    ┃",
           "   ┣━━━+━━━┓ ┃    ┃",
           "   ┃       ┃ ┃    ┃",
           "   ┃       ┃ ┃    ┃",
           "   ┗┳━━━━━━┻$┿━━━━┛",
           "    ┃▲       ┃     ",
           "    ┗━━━━━━━━┛     "]

if floor == 2:
    map = ["┏━━━━━━━━━━━━━━┓",
           "┃              ┃",
           "┃              ┃",
           "┃              ┃",
           "┃              ┃",
           "┃ ┏━━━━━━━━━━━━┫",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┃            ┃",
           "┃ ┗━━━┳━━━━━━━+┫",
           "┃    ▼┃        ┃",
           "┃     $        ┃",
           "┗━━━━━┻━━━━━━━━┛"]

def drawMap():
    for row in map:
        newRow = list(row)

    row_y = 0
    for newRow in map:
        row_x = 0
        for column in newRow:
            if row_y == y and row_x == x and map[y][x] == " ": print("X",end="")
            else: print(column,end="")
            row_x += 1
        print()
        row_y += 1

def clear():
    os.system("cls")

def draw():
    print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")

def save():
    if (floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity) % 2 == 0:
        print(f"hi, {floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity}")
        even = True
    else:
        print(f"Hello! {floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity}")
        even = False
    key = (floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity) % 8
    statsList = [
        name,
        str(x),
        str(y),
        str(floor),
        str(HP),
        str(MaxHP),
        str(Strength),
        str(Mana),
        str(Wit),
        str(Dexterity),
        str(even),
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
        print(f"│1. NEW GAME\n│2. LOAD GAME\n│3. CONTROLS\n│4. QUIT GAME")
        draw()
        choice = input("│>")
        validChoice = False
        if choice == "1":
            validChoice = True
            clear()
            print("│WHAT IS YOUR NAME? ")
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
                    x = int(load_list[1][:-1])
                    y = int(load_list[2][:-1])
                    floor = int(load_list[3][:-1])
                    HP = int(load_list[4][:-1])
                    MaxHP = int(load_list[5][:-1])
                    Strength = int(load_list[6][:-1])
                    Mana = int(load_list[7][:-1])
                    Wit = int(load_list[8][:-1])
                    Dexterity = int(load_list[9][:-1])
                    even = bool(load_list[10][:-1])
                    key = int(load_list[1][:-1])
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