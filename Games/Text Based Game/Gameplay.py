import os, random, time, sys, keyboard, pyautogui

pyautogui.press('f11')

run = True
menu = True
play = False
fight = False
bossFight = False

key1 = False
key2 = False
secret1 = False
secret2 = False
blood_glasses = False

searching = False

moveList = " ","+","k","B","*"

#Red:# \033[1;31;40m \033[0m
#Green:# \033[1;32;40m \033[0m
#Yellow:# \033[1;33;40m \033[0m
#Blue:# \033[1;34;40m \033[0m
#Purple:# \033[1;35;40m \033[0m

def statCustom():
    global Strength, Dexterity, Mana, Wit
    changingStats = True
    points = 0
    while changingStats:
        clear()
        print("│CHANGE STATS SO THEY ARE CUSTOMISED HOW YOU LIKE.")
        draw(False)
        print(f"│YOU HAVE {points} POINTS.")
        draw(False)
        if Strength > 5: print(f"│\033[1;34;40m1\033[0m - STRENGTH = {Strength}-1")
        elif Strength >= 5: print(f"│\033[1;34;40m1\033[0m - STRENGTH = {Strength}")
        if Mana > 5: print(f"│\033[1;34;40m2\033[0m - MANA = {Mana}-1")
        elif Mana >= 5: print(f"│\033[1;34;40m2\033[0m - MANA = {Mana}")
        if Wit > 5: print(f"│\033[1;34;40m3\033[0m - WIT = {Wit}-1")
        elif Wit >= 5: print(f"│\033[1;34;40m3\033[0m - WIT = {Wit}")
        if Dexterity > 5: print(f"│\033[1;34;40m4\033[0m - DEXTERITY = {Dexterity}-1")
        elif Dexterity >= 5: print(f"│\033[1;34;40m4\033[0m - DEXTERITY = {Dexterity}")
        draw(False)
        if points > 0:
            if Strength < 15: print(f"│\033[1;34;40m5\033[0m - STRENGTH = {Strength}+1")
            else: print(f"│\033[1;34;40m5\033[0m - STRENGTH = {Strength}")
            if Mana < 15: print(f"│\033[1;34;40m6\033[0m - MANA = {Mana}+1")
            else: print(f"│\033[1;34;40m6\033[0m - MANA = {Mana}")
            if Wit < 15: print(f"│\033[1;34;40m7\033[0m - WIT = {Wit}+1")
            else: print(f"│\033[1;34;40m7\033[0m - WIT = {Wit}")
            if Dexterity < 15: print(f"│\033[1;34;40m8\033[0m - DEXTERITY = {Dexterity}+1")
            else: print(f"│\033[1;34;40m8\033[0m - DEXTERITY = {Dexterity}")
            draw(False)
        print(f"│TYPE NUMBER OF ACTION YOU WISH TO PERFORM (YOU CANNOT DROP A STAT BELOW 5, OR ABOVE 15)")
        print("│\033[1;34;40m0\033[0m TO CONTINUE (MAKE SURE TO USE ALL YOUR POINTS)")
        draw(False)
        pointChange = input("│>\033[1;34;40m")
        print("\033[0m")
        validInput = False
        if pointChange == "0":
            validInput = True
            changingStats = False
        if pointChange == "1" and Strength > 5:
            validInput = True
            points += 1
            Strength -= 1
        if pointChange == "2" and Mana > 5:
            validInput = True
            points += 1
            Mana -= 1
        if pointChange == "3" and Wit > 5:
            validInput = True
            points += 1
            Wit -= 1
        if pointChange == "4" and Dexterity > 5:
            validInput = True
            points += 1
            Dexterity -= 1
        if pointChange == "5" and Strength < 15 and points > 0:
            validInput = True
            points -= 1
            Strength += 1
        if pointChange == "6" and Mana < 15 and points > 0:
            validInput = True
            points -= 1
            Mana += 1
        if pointChange == "7" and Wit < 15 and points > 0:
            validInput = True
            points -= 1
            Wit += 1
        if pointChange == "8" and Dexterity < 15 and points > 0:
            validInput = True
            points -= 1
            Dexterity += 1
        if not validInput:
            print(f"│THAT IS NOT A VALID OPTION.")
            input("│\033[1;34;40m<")
            print("\033[0m")

#┣┫┳┻┿┏┓┗┛┃━

y_max = 18
x_max = 21

def drawMap():
    global map, x, y, moveList, secret1, secret2, blood_glasses
    if secret1 == True and secret2 == True:
        blood_glasses = True
        secret1 = False
        secret2 = False
    if floor == 0 and not blood_glasses:
        map = ["  ┏━━━━━━━━━━━━┓     ",
               "  ┃            ┃     ",
               "  ┣━+━━━━━━━━┓ ┃     ",
               "  ┃         B┃ ┃     ",
               "  ┣━━━━━━━━━━┛ ┣━━━┓ ",
               "  ┃▲           +   ┃ ",
               "  ┗━━━━━━━━━━━━┻━━━┛ "]
    
    if floor == 0 and blood_glasses:
        map = ["  ┏━━━━━━━━━━━━┓     ",
               "  ┃            ┃     ",
               "  ┣━+━━━━━━━━┓ ┃     ",
               "  ┃          ┃ ┃     ",
               "  ┣━━━━━━━━━━┛ ┣━━━┓ ",
               "  ┃▲           +   ┃ ",
               "  ┗━━━━━━━━━━━━┻━━━┛ "]

    if floor == 1 and not blood_glasses and not key1 and not secret1 and not secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┓     ",
               " ┃             ┃     ",
               " ┃ ┏┳━━━━━━━━┓ ┃     ",
               " ┃ ┗┫        ┃ ┣━━━━┓",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━━━━━━┫ ┃    ┃",
               "     ┃    k  ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻$┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 1 and not blood_glasses and key1 and not secret1 and not secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┓     ",
               " ┃             ┃     ",
               " ┃ ┏┳━━━━━━━━┓ ┃     ",
               " ┃ ┗┫        ┃ ┣━━━━┓",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━━━━━━┫ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻+┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 1 and blood_glasses and not key1 and not secret1 and not secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┳━━━━┓",
               " ┃             *    ┃",
               " ┃ ┏┳━━━━━━━━┓ ┃    ┃",
               " ┃ ┗┫        ┃ ┣━━━━┫",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━*━━━━┫ ┃    ┃",
               "     ┃    k  ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻$┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 1 and blood_glasses and key1 and not secret1 and not secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┳━━━━┓",
               " ┃             *    ┃",
               " ┃ ┏┳━━━━━━━━┓ ┃    ┃",
               " ┃ ┗┫        ┃ ┣━━━━┫",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━*━━━━┫ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻+┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]
    
    if floor == 1 and not blood_glasses and not key1 and secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┓     ",
               " ┃             ┃     ",
               " ┃ ┏┳━━━━━━━━┓ ┃     ",
               " ┃ ┗┫        ┃ ┣━━━━┓",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━*━━━━┫ ┃    ┃",
               "     ┃    k  ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻$┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 1 and not blood_glasses and key1 and secret2:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┓     ",
               " ┃             ┃     ",
               " ┃ ┏┳━━━━━━━━┓ ┃     ",
               " ┃ ┗┫        ┃ ┣━━━━┓",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━*━━━━┫ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻+┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]
    
    if floor == 1 and not blood_glasses and not key1 and secret1:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┳━━━━┓",
               " ┃             *    ┃",
               " ┃ ┏┳━━━━━━━━┓ ┃    ┃",
               " ┃ ┗┫        ┃ ┣━━━━┫",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━━━━━━┫ ┃    ┃",
               "     ┃    k  ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻$┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 1 and not blood_glasses and key1 and secret1:
        map = ["                     ",
               " ┏━━━━━━━━━━━━━┳━━━━┓",
               " ┃             *    ┃",
               " ┃ ┏┳━━━━━━━━┓ ┃    ┃",
               " ┃ ┗┫        ┃ ┣━━━━┫",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━━━━━━┫ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻+┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]

    if floor == 2 and key2:
        map = ["                   ",
               "   ┏━━━━━━━━━━━━━┓ ",
               "   ┃             ┃ ",
               "   ┃             ┃ ",
               "   ┃             ┃ ",
               "   ┃             ┃ ",
               "   ┃ ┏━━━━━━━━━━━┫ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┗━━┳━━━━━━━+┫ ",
               "   ┃   ▼┗┓       ┃ ",
               "   ┃     +       ┃ ",
               "   ┗━━━━━┻━━━━━━━┛ "]
    
    if floor == 2 and not key2:
        map = ["                   ",
               "   ┏━━━━━━━━━━━━━┓ ",
               "   ┃            k┃ ",
               "   ┃             ┃ ",
               "   ┃             ┃ ",
               "   ┃             ┃ ",
               "   ┃ ┏━━━━━━━━━━━┫ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┗━━┳━━━━━━━+┫ ",
               "   ┃   ▼┗┓       ┃ ",
               "   ┃     $       ┃ ",
               "   ┗━━━━━┻━━━━━━━┛ "]

    if floor == 1:
        fullMap = ["                     ",
               " ┏━━━━━━━━━━━━━┳━━━━┓",
               " ┃             *    ┃",
               " ┃ ┏┳━━━━━━━━┓ ┃    ┃",
               " ┃ ┗┫        ┃ ┣━━━━┫",
               " ┃ ▼┃        + +    ┃",
               " ┗━━┻┳━━*━━━━┫ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "-----┣━━━━━━━┛ ┣━━━━┫",
               "     +         +    ┃",
               "-----┣━━━━+━━┓ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┃       ┃ ┃    ┃",
               "     ┗┳━━━━━━┻+┿━━━━┛",
               "      ┃▲       ┃     ",
               "      ┗━━━━━━━━┛     "]
    else:
        fullMap = ["                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         ",
                   "                         "]

    y_max = len(map)-1
    x_max = len(map[0])-1

    for row in map:
        newRow = list(row)

    row_y = 0
    for newRow in map:
        row_x = 0
        for column in newRow:
            if row_y == y and row_x == x and map[y][x] in moveList and searching: print("\033[0;37;45mX\033[0m",end="")
            elif row_y == y and row_x == x and map[y][x] in moveList and not searching: print("X",end="")
            elif row_y == y+1 and row_x == x and searching:
                if fullMap[y+1][x] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            elif row_y == y-1 and row_x == x and searching:
                if fullMap[y-1][x] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            elif row_y == y and row_x == x+1 and searching:
                if fullMap[y][x+1] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            elif row_y == y and row_x == x-1 and searching:
                if fullMap[y][x-1] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            elif row_y == y and row_x == x+2 and searching:
                if fullMap[y][x+2] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            elif row_y == y and row_x == x-2 and searching:
                if fullMap[y][x-2] == "*":
                    print(f"\033[0;37;45m*\033[0m",end="")
                    if row_y == 2:
                        secret1 = True
                    if row_y == 6:
                        secret2 = True
                else: print(f"\033[0;37;45m{column}\033[0m",end="")
            else: print(column,end="")
            row_x += 1
        print()
        row_y += 1

def clear():
    os.system("cls")

def draw(EndColour):
    EndColour = bool(EndColour)
    if EndColour: print(f"\033[0m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    else: print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")

def save():
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
        str(blood_glasses),
        str(key1),
        str(key2),
        str(secret1),
        str(secret2)]

    f = open("load.txt","w")
    for item in statsList:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        draw(False)
        print(f"│\033[1;34;40m1\033[0m. NEW GAME\n│\033[1;34;40m2\033[0m. LOAD GAME\n│\033[1;34;40m3\033[0m. CONTROLS\n│\033[1;34;40m4\033[0m. QUIT GAME")
        draw(False)
        choice = input("│>\033[1;34;40m")
        print("\033[0m")
        validChoice = False
        if choice == "1":
            floor = 1
            x = 0
            y = 10

            blood_glasses = False
            alive = True

            HP = 80
            MaxHP = HP
            Strength = 10
            Mana = 10
            Wit = 10
            Dexterity = 10
            validChoice = True
            secret1 = False
            secret2 = False
            key1 = False
            key2 = False
            clear()
            print("│WHAT IS YOUR NAME? ")
            name = input("│>\033[1;31;40m")
            menu = False
            play = True
            draw(True)
            print(f"│WELCOME \033[1;31;40m{name}\033[0m!")
            draw(False)
            input("│<")
            statCustom()

        if choice == "2":
            validChoice = True
            try:
                f = open("load.txt","r")
                load_list = f.readlines()
                if len(load_list) == 15:
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
                    blood_glasses = bool(load_list[10][:-1])
                    key1 = bool(load_list[11][:-1])
                    key2 = bool(load_list[12][:-1])
                    secret1 = bool(load_list[13][:-1])
                    secret2 = bool(load_list[14][:-1])
                    clear()
                    draw(False)
                    print(f"│WELCOME BACK \033[1;31;40m{name}\033[0m!")
                    draw(False)
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
            print(f"┣━━━━━━━━━━━━━━━━━━CONTROLS━━━━━━━━━━━━━━━━━━━┫\n│TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK\n│\033[1;32;40mHP\033[0m IS THE AMOUNT OF HEALTH YOU HAVE. DON'T DROP BELOW 0 OR YOU LOSE!\n│\033[1;32;40mSTRENGTH\033[0m IS THE PHYSICAL DAMAGE YOU DEAL.\n│\033[1;32;40mMANA\033[0m IS THE MAGIC DAMAGE YOU DEAL\n│\033[1;32;40mWIT\033[0m IS YOUR INTELLEGENCE AND ABILITY TO SPOT TRAPS AND HIDDEN.\n│\033[1;32;40mDEXTERITY\033[0m IS YOUR REACTION SPEED AND YOUR ABILITY TO AIM AND DODGE.\n│'>' MEANS YOU ARE EXPECTED TO INPUT A COMMAND.\n│'<' MEANS PRESS 'ENTER' TO CONTINUE.\n│\033[1;31;40mRED\033[0m IS YOUR NAME.\n│\033[1;32;40mGREEN\033[0m IS STATS.\n│\033[1;34;40mBLUE\033[0m IS OPTIONS.")
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
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        drawMap()
        draw(False)
        print(f"│NAME: \033[1;31;40m{name}\033[0m")
        print(f"│HP: \033[1;32;40m{HP}\033[0m/\033[1;32;40m{MaxHP}\033[0m")
        print(f"│STRENGTH: \033[1;32;40m{Strength}\033[0m")
        print(f"│MANA: \033[1;32;40m{Mana}\033[0m")
        print(f"│WIT: \033[1;32;40m{Wit}\033[0m")
        print(f"│DEXTERITY: \033[1;32;40m{Dexterity}\033[0m")
        if key1:
            draw(False)
            print(f"│KEY 1")
        if key2:
            draw(False)
            print(f"│KEY 2")
        if blood_glasses:
            draw(False)
            print(f"│BLOODGLASSES")    
        draw(False)
        print(f"│\033[1;34;40m0\033[0m ━ SAVE AND QUIT")
        n_option = False
        s_option = False
        e_option = False
        w_option = False

        f_u_option = False
        f_d_option = False

        if map[y-1][x] in moveList and y > 0:
            print(f"│\033[1;34;40mW \033[0m━ NORTH")
            n_option = True
        if map[y+1][x] in moveList and y < y_max:
            print(f"│\033[1;34;40mS \033[0m━ SOUTH")
            s_option = True
        if map[y][x-2] in moveList and map[y][x-1] in moveList and x-1 > 0:
            print(f"│\033[1;34;40mA \033[0m━ WEST")
            w_option = True
        if map[y][x-1] == "▲" and not w_option:
            print(f"│\033[1;34;40mA \033[0m━ WEST")
            f_u_option = True
            w_option = True
        if map[y][x+2] in moveList and map[y][x+1] in moveList and x+1 < x_max:
            print(f"│\033[1;34;40mD \033[0m━ EAST")
            e_option = True
        if map[y][x+1] == "▼" and not e_option:
            print(f"│\033[1;34;40mD \033[0m━ EAST")
            f_d_option = True
            e_option = True
        print(f"│\033[1;34;40m1 \033[0m━ SEARCH")
        draw(False)
        dest = input("│>\033[1;34;40m")
        print("\033[0m│")
        validCommand = False
        searching = False

        if dest == "0":
            validCommand = True
            save()
            play = False
            menu = True
        if dest == "1":
            validCommand = True
            save()
            searching = True
        if dest == "W" and n_option == True:
            validCommand = True
            if map[y-1][x] in moveList: y -= 1
            else: y -= 2
        if dest == "S" and s_option == True:
            validCommand = True
            if map[y+1][x] in moveList: y += 1
            else: y += 2
        if dest == "A" and w_option == True:
            validCommand = True
            x -= 2
            if f_u_option:
                floor += 1
        if dest == "D" and e_option == True:
            validCommand = True
            x += 2
            if f_d_option:
                floor -= 1

        if map[y][x] == "k":
            print("│YOU FOUND A \033[1;35;40mKEY\033[0m!")
            if key1:
                if key2: print("│\033[1;31;40mCHEATER\033[0m")
                else:
                    key2 = True
                    play = False
                    fight = True
            else: key1 = True
            input("│<")

        if map[y][x] == "B":
            print("│FOUND \033[1;35;40mBLOOD GLASSES\033[0m!")
            blood_glasses = True
            input("│<")

        if validCommand == False:
            print(f"│INVALID COMMAND")
            input("│<")
    
    while fight:
        draw(False)
        if bossFight: ...
        else:
            print("│AS YOU PICK UP THE KEY, TWO \033[1;34;40mSKELETONS\033[0m WALK AROUND THE CORNER, AND READY THEIR WEAPONS.")
            input("│<")
            clear()
            draw(False)
            print("│YOU ARE BEING ATTACKED BY 2 \033[1;34;40mSKELETONS\033[0m!")