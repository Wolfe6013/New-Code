import os, random, time, sys, pyautogui

pyautogui.press('f11')

run = True
menu = True
play = False
fight = False
bossFight = False
mapWalk = False
witchDead = False

boom = 0
godVisit = 0

roll = 0
rollMod = 0

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

searching = False

moveList = f"+","k","B","*"," ","~"

#Gray: \033[1;30;40m \033[0m
#Red: \033[1;31;40m \033[0m
#Green: \033[1;32;40m \033[0m
#Yellow: \033[1;33;40m \033[0m
#Blue: \033[1;34;40m \033[0m
#Purple: \033[1;35;40m \033[0m
#Cyan: \033[1;36;40m \033[0m

#End Line: \033[0m

def statCustom():
    global Strength, Dexterity, Mana, Wit
    changingStats = True
    points = 0
    while changingStats:
        clear()
        print(f"│CHANGE STATS SO THEY ARE CUSTOMISED HOW YOU LIKE (WRITE IN FORM 'W1' FOR RAISE STRENGTH).")
        draw(False)
        print(f"│YOU HAVE {points} POINTS.")
        draw(False)
        print(f"│{Cyan}W{End} - RAISE STAT")
        print(f"│{Cyan}S{End} - LOWER STAT")
        draw(False)
        print(f"│{Cyan}1{End} - STRENGTH = {Green}{Strength}{End}")
        print(f"│{Cyan}2{End} - MANA = {Green}{Mana}")
        print(f"│{Cyan}3{End} - WIT = {Green}{Wit}{End}")
        print(f"│{Cyan}4{End} - DEXTERITY = {Green}{Dexterity}{End}")
        draw(False)
        print(f"│TYPE NUMBER OF ACTION YOU WISH TO PERFORM (YOU CANNOT DROP A STAT BELOW 5, OR ABOVE 15)")
        print(f"│{Cyan}0{End} TO CONTINUE (MAKE SURE TO USE ALL YOUR POINTS)")
        draw(False)
        pointChange = input(f"│>{Cyan}")
        print(f"{End}")
        validCommand = False
        if pointChange == "0":
            validCommand = True
            if points > 0:
                y_n = input(f"YOU HAVE {points} POINTS REMAINING. DO YOU WISH TO CONTINUE (Y/N)? ")
                if y_n == 'Y' or y_n == 'y':
                    changingStats = False
        if pointChange == "W1" and Strength > 5:
            validCommand = True
            points += 1
            Strength -= 1
        if pointChange == "W2" and Mana > 5:
            validCommand = True
            points += 1
            Mana -= 1
        if pointChange == "W3" and Wit > 5:
            validCommand = True
            points += 1
            Wit -= 1
        if pointChange == "W4" and Dexterity > 5:
            validCommand = True
            points += 1
            Dexterity -= 1
        if pointChange == "S1" and Strength < 15 and points > 0:
            validCommand = True
            points -= 1
            Strength += 1
        if pointChange == "S2" and Mana < 15 and points > 0:
            validCommand = True
            points -= 1
            Mana += 1
        if pointChange == "S3" and Wit < 15 and points > 0:
            validCommand = True
            points -= 1
            Wit += 1
        if pointChange == "S4" and Dexterity < 15 and points > 0:
            validCommand = True
            points -= 1
            Dexterity += 1
        if not validCommand:
            print(f"│THAT IS NOT A VALID OPTION.")
            input(f"│{Cyan}<")
            print(f"{End}")

#┣┫┳┻┿┏┓┗┛┃━

y_max = 18
x_max = 21

def move(direction):
    global x, y
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'E':
        x -= 1
    elif direction == 'W':
        x += 1

def damage(atker,atked,dodge,atk,hp):
    draw(False)
    roll = random.randint(1,20)
    print(f"│{atker} ATTACKS {atked}!\n│{atker} ROLLED A {roll}+{atk}={roll+atk} TO HIT {atked}!")
    hp -= damage
    if hp < 0:
        hp = 0

def drawMap():
    global map, x, y, moveList, secret1, secret2, blood_glasses, roll, rollMod
    if secret1 == 1 and secret2 == 1:
        blood_glasses = 1
        secret1 = 0
        secret2 = 0
    if floor == 0 and blood_glasses == 0:
        map = ["  ┏━━━━━━━━━━━━┓     ",
               "  ┃            ┃     ",
               "  ┣━+━━━━━━━━┓ ┃     ",
               "  ┃         B┃ ┃     ",
               "  ┣━━━━━━━━━━┛ ┣━━━┓ ",
               "  ┃▲           +   ┃ ",
               "  ┗━━━━━━━━━━━━┻━━━┛ "]
    
    if floor == 0 and blood_glasses == 1:
        map = ["  ┏━━━━━━━━━━━━┓     ",
               "  ┃            ┃     ",
               "  ┣━+━━━━━━━━┓ ┃     ",
               "  ┃          ┃ ┃     ",
               "  ┣━━━━━━━━━━┛ ┣━━━┓ ",
               "  ┃▲           +   ┃ ",
               "  ┗━━━━━━━━━━━━┻━━━┛ "]

    if floor == 1 and blood_glasses == 0 and key1 == 0:
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

    if floor == 1 and blood_glasses == 0 and key1 == 1:
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

    if floor == 1 and blood_glasses == 1 and key1 == 0:
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

    if floor == 1 and blood_glasses == 1 and key1 == 1:
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
    
    if floor == 1 and blood_glasses == 0 and key1 == 0 and secret2 == 1:
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

    if floor == 1 and blood_glasses == 0 and key1 == 1 and secret2 == 1:
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
    
    if floor == 1 and blood_glasses == 0 and key1 == 0 and secret1 == 1:
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

    if floor == 1 and blood_glasses == 0 and key1 == 1 and secret1 == 1:
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

    if floor == 2 and key2 == 1:
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
               "   ┃ ┃     U     ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃          ~┃ ",
               "   ┃ ┗━━┳━━━━━━━+┫ ",
               "   ┃   ▼┗┓       ┃ ",
               "   ┃     +       ┃ ",
               "   ┗━━━━━┻━━━━━━━┛ "]
    
    if floor == 2 and key2 == 0 :
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
               "   ┃ ┃     U     ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃           ┃ ",
               "   ┃ ┃          ~┃ ",
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
            if column == "U" and boom < 1 and not searching: print(f"{Gray}{column}{End}",end="")
            elif row_y == y and row_x == x and map[y][x] in moveList and searching: print(f"\033[0;37;45mX{End}",end="")
            elif row_y == y and row_x == x and map[y][x] in moveList and not searching: print(f"{Red}X{End}",end="")
            elif column == "B" and not searching: print(f"\033[0;35;40m{column}{End}",end="")
            elif column == "k" and not searching: print(f"\033[0;35;40m{column}{End}",end="")
            elif row_y == y+1 and row_x == x and searching:
                if fullMap[y+1][x] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif row_y == y-1 and row_x == x and searching:
                if fullMap[y-1][x] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif row_y == y and row_x == x+1 and searching:
                if fullMap[y][x+1] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif row_y == y and row_x == x-1 and searching:
                if fullMap[y][x-1] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif row_y == y and row_x == x+2 and searching:
                if fullMap[y][x+2] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif row_y == y and row_x == x-2 and searching:
                if fullMap[y][x-2] == "*":
                    if roll+rollMod >= 30:
                        print(f"\033[0;37;45m*{End}",end="")
                        if row_y == 2:
                            secret1 = 1
                        if row_y == 6:
                            secret2 = 1
                    else: print(f"\033[0;37;45m{column}{End}",end="")
                else: print(f"\033[0;37;45m{column}{End}",end="")
            elif floor == 2 and column == "~":
                print(f"\033[0;30;40m{column}{End}",end="")
            elif not searching: print(column,end="")
            elif searching: print(f"{Gray}{column}{End}",end="")
            row_x += 1
        print()
        row_y += 1

def clear():
    os.system("cls")

def draw(EndColour):
    EndColour = bool(EndColour)
    if EndColour: print(f"{End}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
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
        str(secret2),
        str(godVisit)]

    f = open("save.txt","w")
    for item in statsList:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        draw(False)
        print(f"│{Cyan}1{End}. NEW GAME\n│{Cyan}2{End}. LOAD GAME\n│{Cyan}3{End}. CONTROLS\n│{Cyan}4{End}. QUIT GAME")
        draw(False)
        choice = input(f"│>{Cyan}")
        print(f"{End}")
        validCommand = False
        if choice == "1":
            floor = 1
            x = 0
            y = 10

            blood_glasses = 0
            alive = True

            HP = 80
            MaxHP = HP
            Strength = 10
            Mana = 10
            Wit = 10
            Dexterity = 10
            validCommand = True
            secret1 = 0
            secret2 = 0
            key1 = 0
            key2 = 0
            clear()
            print(f"│WHAT IS YOUR NAME? ")
            name = input(f"│>{Red}")
            menu = False
            play = True
            draw(True)
            print(f"│WELCOME {Red}{name}{End}!")
            draw(False)
            input(f"│<")
            statCustom()

        if choice == "2":
            validCommand = True
            try:
                f = open("save.txt","r")
                load_list = f.readlines()
                if len(load_list) == 16:
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
                    blood_glasses = int(load_list[10][:-1])
                    key1 = int(load_list[11][:-1])
                    key2 = int(load_list[12][:-1])
                    secret1 = int(load_list[13][:-1])
                    secret2 = int(load_list[14][:-1])
                    godVisit = int(load_list[15][:-1])
                    clear()
                    draw(False)
                    print(f"│WELCOME BACK {Red}{name}{End}!")
                    draw(False)
                    input(f"│<")
                    menu = False
                    play = True
                else:
                    print(f"│CORRUPT SAVE FILE!")
                    input(f"│<")
            except OSError:
                print(f"│NO LOADABLE SAVE FILE!")
                input(f"│<")

        if choice == "3":
            validCommand = True
            clear()
            print(f"┣━━━━━━━━━━━━━━━━━━CONTROLS━━━━━━━━━━━━━━━━━━━┫\n│TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK\n│{Green}HP{End} IS THE AMOUNT OF HEALTH YOU HAVE. DON'T DROP BELOW 0 OR YOU LOSE!\n│{Green}STRENGTH{End} IS THE PHYSICAL DAMAGE YOU DEAL.\n│{Green}MANA{End} IS THE MAGIC DAMAGE YOU DEAL\n│{Green}WIT{End} IS YOUR INTELLEGENCE AND ABILITY TO SPOT TRAPS AND HIDDEN.\n│{Green}DEXTERITY{End} IS YOUR REACTION SPEED AND YOUR ABILITY TO AIM AND DODGE.\n│'>' MEANS YOU ARE EXPECTED TO INPUT A COMMAND.\n│'<' MEANS PRESS 'ENTER' TO CONTINUE.\n│{Red}RED{End} IS YOUR NAME.\n│{Green}GREEN{End} IS STATS.\n│{Cyan}CYAN{End} IS OPTIONS.\n│{Blue}BLUE{End} IS ENEMY NAMES.\n│{Purple}PURPLE{End} IS ITEMS.")
            input(f"│<")

        if choice == "4":
            validCommand = True
            clear()
            quit()

        if validCommand == False:
            print(f"│THAT IS NOT A VALID CHOICE. ONLY TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK.")
            input(f"│<")

    while play:
        if godVisit == 0:
            clear()
            draw(False)
            print(f"│LOCATION: FLOOR {floor}")
            draw(False)
            drawMap()
            draw(False)
            print(f"│NAME: {Red}{name}{End}")
            print(f"│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}")
            print(f"│STRENGTH: {Green}{Strength}{End}")
            print(f"│MANA: {Green}{Mana}{End}")
            print(f"│WIT: {Green}{Wit}{End}")
            print(f"│DEXTERITY: {Green}{Dexterity}{End}")
            if key1 == 1:
                draw(False)
                print(f"│KEY 1")
            if key2 == 1:
                draw(False)
                print(f"│KEY 2")
            if blood_glasses == 1:
                draw(False)
                print(f"│BLOODGLASSES")    
            draw(False)

            if roll > 0:
                print(f"│YOU ROLLED A {Green}{roll}+{rollMod} = {roll+rollMod}{End}")
                draw(False)
                roll = 0
                rollMod = 0

            print(f"│{Cyan}0{End} ━ SAVE AND QUIT")
            n_option = False
            s_option = False
            e_option = False
            w_option = False

            f_u_option = False
            f_d_option = False

            if map[y-1][x] in moveList and y > 0:
                print(f"│{Cyan}W {End}━ NORTH")
                n_option = True
            if map[y+1][x] in moveList and y < y_max:
                print(f"│{Cyan}S {End}━ SOUTH")
                s_option = True
            if map[y][x-2] in moveList and map[y][x-1] in moveList and x-1 > 0:
                print(f"│{Cyan}A {End}━ WEST")
                w_option = True
            if map[y][x-1] == "▲" and not w_option:
                print(f"│{Cyan}A {End}━ WEST")
                f_u_option = True
                w_option = True
            if map[y][x+2] in moveList and map[y][x+1] in moveList and x+1 < x_max:
                print(f"│{Cyan}D {End}━ EAST")
                e_option = True
            if map[y][x+1] == "▼" and not e_option:
                print(f"│{Cyan}D {End}━ EAST")
                f_d_option = True
                e_option = True
            print(f"│{Cyan}1 {End}━ SEARCH")
            draw(False)
            dest = input(f"│>{Cyan}")
            print(f"{End}│")
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
                roll = random.randint(1,20)
                rollMod = Wit
            if dest == "W" and n_option == True:
                save()
                validCommand = True
                if map[y-1][x] in moveList: y -= 1
                else: y -= 2
            if dest == "S" and s_option == True:
                save()
                validCommand = True
                if map[y+1][x] in moveList: y += 1
                else: y += 2
            if dest == "A" and w_option == True:
                save()
                validCommand = True
                x -= 2
                if f_u_option:
                    floor += 1
            if dest == "D" and e_option == True:
                save()
                validCommand = True
                x += 2
                if f_d_option:
                    floor -= 1

            if map[y][x] == "k":
                print(f"│YOU FOUND A {Purple}KEY{End}!")
                if key1 == 1:
                    if key2 == 1: print(f"│{Red}CHEATER{End}")
                    else:
                        key2 = 1
                        play = False
                        fight = True
                        Speak = True
                else: key1 = 1
                input(f"│<")

            if map[y][x] == "B":
                print(f"│FOUND {Purple}BLOOD GLASSES{End}!")
                blood_glasses = 1
                input(f"│<")

            if map[y][x] == "~":
                fight = True
                bossFight = True
                mapWalk = True
                play = False

            if validCommand == False:
                print(f"│INVALID COMMAND")
                input(f"│<")

if dead:
    clear()
    draw(False)
    print(f"│{Red}",end="")
    for char in name:
        print(char,end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"{End}",end="")
    text =  " WAS SLAIN!"
    for char in text:
        print(char,end="")
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    draw(False)
    input(f"│<")