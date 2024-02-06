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
        print(f"│CHANGE STATS SO THEY ARE CUSTOMISED HOW YOU LIKE.")
        draw(False)
        print(f"│YOU HAVE {points} POINTS.")
        draw(False)
        if Strength > 5: print(f"│{Cyan}1{End} - STRENGTH = {Strength}-1")
        elif Strength >= 5: print(f"│{Cyan}1{End} - STRENGTH = {Strength}")
        if Mana > 5: print(f"│{Cyan}2{End} - MANA = {Mana}-1")
        elif Mana >= 5: print(f"│{Cyan}2{End} - MANA = {Mana}")
        if Wit > 5: print(f"│{Cyan}3{End} - WIT = {Wit}-1")
        elif Wit >= 5: print(f"│{Cyan}3{End} - WIT = {Wit}")
        if Dexterity > 5: print(f"│{Cyan}4{End} - DEXTERITY = {Dexterity}-1")
        elif Dexterity >= 5: print(f"│{Cyan}4{End} - DEXTERITY = {Dexterity}")
        draw(False)
        if points > 0:
            if Strength < 15: print(f"│{Cyan}5{End} - STRENGTH = {Strength}+1")
            else: print(f"│{Cyan}5{End} - STRENGTH = {Strength}")
            if Mana < 15: print(f"│{Cyan}6{End} - MANA = {Mana}+1")
            else: print(f"│{Cyan}6{End} - MANA = {Mana}")
            if Wit < 15: print(f"│{Cyan}7{End} - WIT = {Wit}+1")
            else: print(f"│{Cyan}7{End} - WIT = {Wit}")
            if Dexterity < 15: print(f"│{Cyan}8{End} - DEXTERITY = {Dexterity}+1")
            else: print(f"│{Cyan}8{End} - DEXTERITY = {Dexterity}")
            draw(False)
        print(f"│TYPE NUMBER OF ACTION YOU WISH TO PERFORM (YOU CANNOT DROP A STAT BELOW 5, OR ABOVE 15)")
        print(f"│{Cyan}0{End} TO CONTINUE (MAKE SURE TO USE ALL YOUR POINTS)")
        draw(False)
        pointChange = input(f"│>{Cyan}")
        print(f"{End}")
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
            input(f"│{Cyan}<")
            print(f"{End}")

#┣┫┳┻┿┏┓┗┛┃━

y_max = 18
x_max = 21

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
        validChoice = False
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
            validChoice = True
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
            validChoice = True
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
            validChoice = True
            clear()
            print(f"┣━━━━━━━━━━━━━━━━━━CONTROLS━━━━━━━━━━━━━━━━━━━┫\n│TYPE THE NUMBER OF THE OPTION YOU WISH TO PICK\n│{Green}HP{End} IS THE AMOUNT OF HEALTH YOU HAVE. DON'T DROP BELOW 0 OR YOU LOSE!\n│{Green}STRENGTH{End} IS THE PHYSICAL DAMAGE YOU DEAL.\n│{Green}MANA{End} IS THE MAGIC DAMAGE YOU DEAL\n│{Green}WIT{End} IS YOUR INTELLEGENCE AND ABILITY TO SPOT TRAPS AND HIDDEN.\n│{Green}DEXTERITY{End} IS YOUR REACTION SPEED AND YOUR ABILITY TO AIM AND DODGE.\n│'>' MEANS YOU ARE EXPECTED TO INPUT A COMMAND.\n│'<' MEANS PRESS 'ENTER' TO CONTINUE.\n│{Red}RED{End} IS YOUR NAME.\n│{Green}GREEN{End} IS STATS.\n│{Cyan}CYAN{End} IS OPTIONS.\n│{Blue}BLUE{End} IS ENEMY NAMES.\n│{Purple}PURPLE{End} IS ITEMS.")
            input(f"│<")

        if choice == "4":
            validChoice = True
            clear()
            quit()

        if validChoice == False:
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
        else:
            validChoice = False
            while validChoice == False:
                clear()
                draw(False)
                print(f"│{Yellow}",end="")
                text = "HELLO "
                for char in text:
                    print(char,end="")
                    sys.stdout.flush()
                    time.sleep(0.05)
                print(f"{Red}",end="")
                for char in name:
                    print(char,end="")
                    sys.stdout.flush()
                    time.sleep(0.05)
                print(f"{End}\n│{Yellow}",end="")
                text = "YOU DIED.│YOU MADE IT TO THE AFTERLIFE!│HOWEVER, YOU HAVE UNFINISHED BUSINESS, SO I CAN'T LET YOU PASS.│I WILL GIVE YOU A BLESSING.│DO YOU WISH FOR ME TO BLESS YOUR STRENGTH OR MANA (S/M)?"
                for char in text:
                    if char == "│":
                        print(f"\n{End}│{Yellow}",end="")
                    else:
                        print(char,end="")
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
                draw(True)
                choice = input(f"│>")
                if choice == "M":
                    Mana = 100
                    validChoice = True
                    godVisit = 0
                    HP = MaxHP
                elif choice == "S":
                    Strength = 100
                    validChoice = True
                    godVisit = 0
                    HP = MaxHP
                else:
                    print(f"│{Yellow}")
                    text = " IS NOT A VALID CHOICE. PLEASE TYPE 'M' FOR MANA OR 'S' FOR STRENGTH."
                    for char in choice:
                        print(char,end="")
                        sys.stdout.flush()
                        time.sleep(0.05)
                    for char in text:
                        print(char,end="")
                        sys.stdout.flush()
                        time.sleep(0.05)
                    print()
                    input(f"│<")
    while mapWalk:
        while y != 9:
            clear()
            draw(False)
            print(f"│LOCATION: FLOOR {floor}")
            draw(False)
            drawMap()
            draw(False)
            print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
            draw(False)
            print("│<")
            time.sleep(0.5)
            y -= 1
        while x != 11:
            clear()
            draw(False)
            print(f"│LOCATION: FLOOR {floor}")
            draw(False)
            drawMap()
            draw(False)
            print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
            draw(False)
            print("│<")
            time.sleep(0.5)
            x -= 1

        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        drawMap()
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        time.sleep(0.5)

        time.sleep(1.5)
        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        s = f"\033[0;37;42m {End}"
        X = f"\033[0;31;42mX{End}"
        x = f"\033[0;31;40mX{End}"
        U = f"\033[1;30;42mU{End}"
        u = f"{Gray}U{End}"

        print(f"                   ") #\033[0;37;42m
        print(f"   ┏━━━━━━━━━━━━━┓ ") #\033[0m
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃ ┏━━━━━━━━━━━┫ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃     {x}     ┃ ")
        print(f"   ┃ ┃     {U}     ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┗━━┳━━━━━━━+┫ ")
        print(f"   ┃   ▼┗┓       ┃ ")
        print(f"   ┃     +       ┃ ")
        print(f"   ┗━━━━━┻━━━━━━━┛ ")
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        print("│<")
        time.sleep(0.5)

        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        print(f"                   ")
        print(f"   ┏━━━━━━━━━━━━━┓ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃ ┏━━━━━━━━━━━┫ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃   {s}{s}{X}{s}{s}   ┃ ")
        print(f"   ┃ ┃   {s}{s}{u}{s}{s}   ┃ ")
        print(f"   ┃ ┃   {s}{s}{s}{s}{s}   ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┗━━┳━━━━━━━+┫ ")
        print(f"   ┃   ▼┗┓       ┃ ")
        print(f"   ┃     +       ┃ ")
        print(f"   ┗━━━━━┻━━━━━━━┛ ")
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        print("│<")
        time.sleep(0.5)

        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        print(f"                   ")
        print(f"   ┏━━━━━━━━━━━━━┓ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃ ┏━━━━━━━━━━━┫ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┃  {s}{s}{s}{s}{s}{s}{s}  ┃ ")
        print(f"   ┃ ┃  {s}{s} {x} {s}{s}  ┃ ")
        print(f"   ┃ ┃  {s}{s} {u} {s}{s}  ┃ ")
        print(f"   ┃ ┃  {s}{s}   {s}{s}  ┃ ")
        print(f"   ┃ ┃  {s}{s}{s}{s}{s}{s}{s}  ┃ ")
        print(f"   ┃ ┃           ┃ ")
        print(f"   ┃ ┗━━┳━━━━━━━+┫ ")
        print(f"   ┃   ▼┗┓       ┃ ")
        print(f"   ┃     +       ┃ ")
        print(f"   ┗━━━━━┻━━━━━━━┛ ")
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        print("│<")
        time.sleep(0.5)

        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        print(f"                   ")
        print(f"   ┏━━━━━━━━━━━━━┓ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃ ┏━━━━━━━━━━━┫ ")
        print(f"   ┃ ┃{s}{s}{s}{s}{s}{s}{s}{s}{s}{s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}       {s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}   {x}   {s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}   {u}   {s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}       {s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}       {s}{s}┃ ")
        print(f"   ┃ ┃{s}{s}{s}{s}{s}{s}{s}{s}{s}{s}{s}┃ ")
        print(f"   ┃ ┗━━┳━━━━━━━+┫ ")
        print(f"   ┃   ▼┗┓       ┃ ")
        print(f"   ┃     +       ┃ ")
        print(f"   ┗━━━━━┻━━━━━━━┛ ")
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        print("│<")
        time.sleep(0.5)
        _ = f"\033[0;32;40m━{End}"
        l = f"\033[0;32;40m┃{End}"
        t = f"\033[0;32;40m┫{End}"
        k = f"\033[0;32;40m┏{End}"
        T = f"\033[0;32;40m┳{End}"
        L = f"\033[0;32;40m┗{End}"
        X = f"\033[0;32;40m+{End}"

        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        print(f"                   ")
        print(f"   ┏━━━━━━━━━━━━━┓ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃             ┃ ")
        print(f"   ┃ {k}{_}{_}{_}{_}{_}{_}{_}{_}{_}{_}{_}{t} ")
        print(f"   ┃ {l}           {l} ")
        print(f"   ┃ {l}           {l} ")
        print(f"   ┃ {l}     {x}     {l} ")
        print(f"   ┃ {l}     {u}     {l} ")
        print(f"   ┃ {l}           {l} ")
        print(f"   ┃ {l}           {l} ")
        print(f"   ┃ {l}           {l} ")
        print(f"   ┃ {L}{_}{_}{T}{_}{_}{_}{_}{_}{_}{_}{X}{t} ")
        print(f"   ┃   ▼┗┓       ┃ ")
        print(f"   ┃     +       ┃ ")
        print(f"   ┗━━━━━┻━━━━━━━┛ ")
        draw(False)
        print(f"│NAME: {Red}{name}{End}\n│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}\n│STRENGTH: {Green}{Strength}{End}\n│MANA: {Green}{Mana}{End}\n│WIT: {Green}{Wit}{End}\n│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        print("│<")
        time.sleep(0.5)
        os.system("cls")

        mapWalk = False

        colList = [Red,Green,Yellow,Blue,Purple,Cyan]

        text1 = f"THE "
        text2 = f"WITCH"
        text3 = f" APPEARS!"

        for char in text1:
            print(char,end="")
            sys.stdout.flush()
            time.sleep(0.05)
        print(Gray,end="")
        for char in text2:
            print(char,end="")
            sys.stdout.flush()
            time.sleep(0.05)
        print(End,end="")
        for char in text3:
            print(char,end="")
            sys.stdout.flush()
            time.sleep(0.05)

        time.sleep(1)
        os.system("cls")

        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        print(f"THE {Gray}WIT{Rand1}C{Gray}H{End} APPEARS!")
        time.sleep(0.9)
        os.system("cls")
            
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        print(f"THE {Gray}W{Rand1}I{Gray}TCH{End} APPEARS!")
        time.sleep(0.8)
        os.system("cls")
            
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        print(f"THE {Gray}WITC{Rand1}H{End} APPEARS!")
        time.sleep(0.7)
        os.system("cls")
            
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        print(f"THE {Rand1}W{Rand2}I{Gray}TCH{End} APPEARS!")
        time.sleep(0.6)
        os.system("cls")
        
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        print(f"THE {Gray}WI{Rand1}T{Gray}C{Rand2}H{End} APPEARS!")
        time.sleep(0.5)
        os.system("cls")
        
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        print(f"THE {Gray}W{Rand1}I{Gray}T{Gray}C{Rand2}H{End} APPEARS!")
        time.sleep(0.4)
        os.system("cls")
        
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        colList.remove(Rand2)
        Rand3 = random.choice(colList)
        print(f"THE {Gray}W{Rand1}I{Rand2}T{Gray}C{Rand3}H{End} APPEARS!")
        time.sleep(0.3)
        os.system("cls")
            
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        colList.remove(Rand2)
        Rand3 = random.choice(colList)
        print(f"THE {Rand1}W{Gray}I{Rand2}T{Gray}C{Rand3}H{End} APPEARS!")
        time.sleep(0.2)
        os.system("cls")
            
        colList = [Red,Green,Yellow,Blue,Purple,Cyan]
        Rand1 = random.choice(colList)
        colList.remove(Rand1)
        Rand2 = random.choice(colList)
        colList.remove(Rand2)
        Rand3 = random.choice(colList)
        colList.remove(Rand3)
        Rand4 = random.choice(colList)
        print(f"THE {Rand1}W{Rand2}I{Rand3}T{Gray}C{Rand4}H{End} APPEARS!")
        time.sleep(0.1)
        os.system("cls")
        for x, y in enumerate(range(100)):        
            colList = [Red,Green,Yellow,Blue,Purple,Cyan]
            Rand1 = random.choice(colList)
            colList.remove(Rand1)
            Rand2 = random.choice(colList)
            colList.remove(Rand2)
            Rand3 = random.choice(colList)
            colList.remove(Rand3)
            Rand4 = random.choice(colList)
            colList.remove(Rand4)
            Rand5 = random.choice(colList)
            print(f"THE {Rand1}W{Rand2}I{Rand3}T{Rand4}C{Rand5}H{End} APPEARS!")
            os.system("cls")

        print(f"THE {Gray}WITCH{End} APPEARS!")
        time.sleep(1)
        os.system("cls")
        time.sleep(1)
        input(f"│<")

    while fight:
        clear()
        draw(False)
        if bossFight:
            clear()
            draw(False)
            text = "│YOU BELIVE YOU CAN DEFEAT ME?I KNOW EVERY MOVE YOU MAKE BEFORE YOU DO!I CONTROL THE ENTIRETY OF TIME AND SPACE!GIVE IN."
            for char in text:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.05)
                if char == "?" or char == "!":
                    time.sleep(0.05)
                    print(f"\n│",end="")
            print()
            draw(True)
            input("│<")
            e_name = f"{Gray}WITCH{End}"
            e_hp = 155
            e_maxhp = e_hp
            e_str = 1
            e_mana = 50
            e_wit = 50
            e_dex = (Dexterity+20)/2
            atkTimes = 0
            while bossFight:
                if True:
                    clear()
                    draw(False)
                    print(f"│{Red}{name}{End} IS BEING ATTACKED BY {e_name}!")
                    draw(False)
                    print(f"│NAME: {Red}{name}{End}")
                    print(f"│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}")
                    print(f"│STRENGTH: {Green}{Strength}{End}")
                    print(f"│MANA: {Green}{Mana}{End}")
                    print(f"│WIT: {Green}{Wit}{End}")
                    print(f"│DEXTERITY: {Green}{Dexterity}{End}")
                    draw(False)
                    if e_hp > 0:
                        print(f"│NAME: {e_name}")
                        print(f"│HP: {Green}{e_hp}{End}/{Green}{e_maxhp}{End}")
                        print(f"│STRENGTH: {Green}{e_str}{End}")
                        print(f"│MANA: {Green}{e_mana}{End}")
                        print(f"│WIT: {Green}{e_wit}{End}")
                        print(f"│DEXTERITY: {Green}{e_dex}{End}")
                    else: print(f"│{e_name} IS SLAIN!")
                    draw(False)
                    print(f"│{Red}{name}{End} DEXTERITY IS {Green}{Dexterity}{End}")
                    print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}")
                    print(f"│COMBAT ORDER IS: ",end="")
                    if HP > 0:
                        if Dexterity >= e_dex:
                            print(f"{Red}{name}{End} - {e_name}.")
                            CO1 = "P1"
                            CO2 = "E1"
                        else:
                            print(f"{e_name} - {Red}{name}{End}.")
                            CO1 = "E1"
                            CO2 = "P1"
                    draw(False)
                    print(f"│{Cyan}1 {End}━ ATTACK {e_name}")
                    print(f"│{Cyan}2 {End}━ MAGIC ATTACK {e_name}")
                    print(f"│{Cyan}3 {End}━ TRICK")
                    print(f"│{Cyan}4 {End}━ RUN")
                    draw(False)
                    combatChoice = input(f"│>{Cyan}")
                    print(f"{End}")
                    clear()
                    validChoice = False
                    bossLines = ["YOU ARE BLINDED BY AMBITION!","IF YOU BELIEVE YOU CAN KILL ME, YOU ARE A FOOL!","YOUR INABILITY TO JUDGE THE HOPELESSNESS OF YOUR SITUATION WILL LEAD TO YOUR DEATH!","DESPAIR!","YOUR FATE LIES IN THE PALM OF MY HAND!","DO YOU KNOW THE DEFINITION OF INSANITY? YOU WILL LEARN SOON.","ONLY A MASOCHIST WOULD CONTINUE TRYING.","THERE IS AN EASTER EGG WHERE, UPON PRESSING THE KEYS 'ALT' AND 'F4', YOU GET TO SURVIVE!"]
                    if combatChoice == "1":
                        atkTimes += 1
                        draw(False)
                        validChoice = True
                        if CO1 == "P1" and HP > 0:
                            toHit = random.randint(1,20)
                            print(f"│{Red}{name}{End} ATTACKS {e_name}!")
                            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                            print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                            print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                            if toHit+Strength >= e_dex*2:
                                print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                                e_hp -= Strength
                                if e_hp <= 0:
                                    print(f"{Red}{name}{End} KILLED {e_name}!")
                            else: print(f"│{e_name} DODGES THE ATTACK!")
                            draw(False)
                        elif CO1 == "E1" and HP > 0 and fight:
                            if atkTimes < 10:
                                print(f"│{random.choice(bossLines)}")
                            elif atkTimes == 10:
                                print(f"│ENOUGH! YOU WILL CONTINUE NO LONGER, OR I SHALL KILL YOU!")
                            elif atkTimes > 10:
                                print(f"│YOU HAVE MADE A GRAVE MISTAKE!")
                                toHit = random.randint(1,20)
                                print(f"│{e_name} CASTS A SPELL AT {Red}{name}{End}!")
                                print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                                print(f"│{e_name} MANA IS {Green}{e_mana}{End}.")
                                print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_mana}{End}={Green}{toHit+e_mana}{End}.")
                                if toHit+e_str >= Dexterity*2:
                                    print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_mana}{End} DAMAGE!")
                                    HP -= e_mana
                                    if HP <= 0:
                                        fight = False
                                        play = False
                                        run = False
                                        godVisit = 1
                                        dead = True
                                else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                            draw(False)
                        if CO2 == "P1" and HP > 0:
                            toHit = random.randint(1,20)
                            print(f"│{Red}{name}{End} ATTACKS {e_name}!")
                            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                            print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                            print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                            if toHit+Strength >= e_dex*2:
                                print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                                e_hp -= Strength
                                if e_hp <= 0:
                                    print(f"{Red}{name}{End} KILLED {e_name}!")
                            else: print(f"│{e_name} DODGES THE ATTACK!")
                            input(f"│<")
                        elif CO2 == "E1" and HP > 0 and fight:
                            if atkTimes < 10:
                                print(f"│{random.choice(bossLines)}")
                                input(f"│<")
                            elif atkTimes == 10:
                                print(f"│ENOUGH! YOU WILL CONTINUE NO LONGER, OR I SHALL KILL YOU!")
                            elif atkTimes > 10:
                                print(f"│YOU HAVE MADE A GRAVE MISTAKE!")
                                toHit = random.randint(1,20)
                                print(f"│{e_name} CASTS A SPELL AT {Red}{name}{End}!")
                                print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                                print(f"│{e_name} MANA IS {Green}{e_mana}{End}.")
                                print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_mana}{End}={Green}{toHit+e_mana}{End}.")
                                if toHit+e_str >= Dexterity*2:
                                    print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_mana}{End} DAMAGE!")
                                    HP -= e_mana
                                    if HP <= 0:
                                        fight = False
                                        play = False
                                        run = False
                                        godVisit = 1
                                        dead = True
                                else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                                input(f"│<")
                    if combatChoice == "2":
                        atkTimes += 1
                        draw(False)
                        validChoice = True
                        if CO1 == "P1" and HP > 0:
                            toHit = random.randint(1,20)
                            print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
                            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                            print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                            print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                            if toHit+Mana >= e_dex*2:
                                print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                                e_hp -= Mana
                                if e_hp <= 0:
                                    print(f"{Red}{name}{End} KILLED {e_name}!")
                            else: print(f"│{e_name} DODGES THE ATTACK!")
                            draw(False)
                        elif CO1 == "E1" and HP > 0 and fight:
                            if atkTimes < 10:
                                print(f"│{random.choice(bossLines)}")
                            elif atkTimes == 10:
                                print(f"│ENOUGH! YOU WILL CONTINUE NO LONGER, OR I SHALL KILL YOU!")
                            elif atkTimes > 10:
                                print(f"│YOU HAVE MADE A GRAVE MISTAKE!")
                                toHit = random.randint(1,20)
                                print(f"│{e_name} CASTS A SPELL AT {Red}{name}{End}!")
                                print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                                print(f"│{e_name} MANA IS {Green}{e_mana}{End}.")
                                print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_mana}{End}={Green}{toHit+e_mana}{End}.")
                                if toHit+e_mana >= Dexterity*2:
                                    print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_mana}{End} DAMAGE!")
                                    HP -= e_mana
                                    if HP <= 0:
                                        fight = False
                                        play = False
                                        run = False
                                        godVisit = 1
                                        dead = True
                                else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                            draw(False)
                        if CO2 == "P1" and HP > 0:
                            toHit = random.randint(1,20)
                            print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
                            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                            print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                            print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                            if toHit+Mana >= e_dex*2:
                                print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                                e_hp -= Mana
                                if e_hp <= 0:
                                    print(f"{Red}{name}{End} KILLED {e_name}!")
                            else: print(f"│{e_name} DODGES THE ATTACK!")
                            input(f"│<")
                        elif CO2 == "E1" and HP > 0 and fight:
                            if atkTimes < 10:
                                print(f"│{random.choice(bossLines)}")
                                input(f"│<")
                            elif atkTimes == 10:
                                print(f"│ENOUGH! YOU WILL CONTINUE NO LONGER, OR I SHALL KILL YOU!")
                            elif atkTimes > 10:
                                print(f"│YOU HAVE MADE A GRAVE MISTAKE!")
                                toHit = random.randint(1,20)
                                print(f"│{e_name} CASTS A SPELL AT {Red}{name}{End}!")
                                print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                                print(f"│{e_name} MANA IS {Green}{e_mana}{End}.")
                                print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_mana}{End}={Green}{toHit+e_mana}{End}.")
                                if toHit+e_mana >= Dexterity*2:
                                    print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_mana}{End} DAMAGE!")
                                    HP -= e_mana
                                    if HP <= 0:
                                        fight = False
                                        play = False
                                        run = False
                                        godVisit = 1
                                        dead = True
                                else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                                input(f"│<")
                    if combatChoice == "3":
                        draw(False)
                        validChoice = True
                        print(f"│YOU TRULY BELIVE I WOULD FALL FOR YOUR PATHETIC TRICKS?")
                        draw(False)
                        if CO1 == "E1" and HP > 0 and fight:
                            print(f"│{random.choice(bossLines)}")
                            input(f"│<")
                        if CO2 == "E1" and HP > 0 and fight:
                            print(f"│{random.choice(bossLines)}")
                            input(f"│<")
                    if combatChoice == "4":
                        draw(False)
                        validChoice = True
                        print(f"│YOU REALLY THINK YOU CAN ESCAPE!")
                        draw(False)
                        if CO1 == "E1" and HP > 0 and fight:
                            print(f"│{random.choice(bossLines)}")
                            input(f"│<")
                        if CO2 == "E1" and HP > 0 and fight:
                            print(f"│{random.choice(bossLines)}")
                            input(f"│<")
                    if not validChoice and HP > 0:
                        draw(False)
                        print(f"│INVALID INPUT!")
                        draw(False)
                        input(f"│<")
                    if e_hp <= 0:
                        play = False
                        fight = False
                        bossFight = False
                        witchDead = True
                        clear()
                        draw(False)
                        print(f"│{Red}{name}{End} KILLED {e_name}!")
                        draw(False)
                        input(f"│<")
                    if HP <= 0:
                        play = False
                        fight = False
                        bossFight = False
                        dead = True
                        godVisit = 1
                        x = 16
                        y = 14
                        save()
            
        else:
            e_name = f"{Blue}SKELETON 1{End}"
            e_hp = 20
            e_maxhp = e_hp
            e_str = 10
            e_dex = 12

            e2_name = f"{Blue}SKELETON 2{End}"
            e2_hp = 20
            e2_maxhp = e_hp
            e2_str = 12
            e2_dex = 10
            while fight:
                if Speak == True:
                    print(f"│AS YOU PICK UP THE KEY, TWO {Blue}SKELETONS{End} WALK AROUND THE CORNER, AND READY THEIR WEAPONS.")
                    draw(False)
                    input(f"│<")
                    Speak = False

                clear()
                draw(False)
                print(f"│{Red}{name}{End} IS BEING ATTACKED BY 2 {Blue}SKELETONS{End}!")
                draw(False)
                print(f"│NAME: {Red}{name}{End}")
                print(f"│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}")
                print(f"│STRENGTH: {Green}{Strength}{End}")
                print(f"│MANA: {Green}{Mana}{End}")
                print(f"│WIT: {Green}{Wit}{End}")
                print(f"│DEXTERITY: {Green}{Dexterity}{End}")
                draw(False)
                if e_hp > 0:
                    print(f"│NAME: {e_name}")
                    print(f"│HP: {Green}{e_hp}{End}/{Green}{e_maxhp}{End}")
                    print(f"│STRENGTH: {Green}{e_str}{End}")
                    print(f"│MANA: {Green}1{End}")
                    print(f"│WIT: {Green}1{End}")
                    print(f"│DEXTERITY: {Green}{e_dex}{End}")
                else: print(f"│{e_name} IS SLAIN!")
                draw(False)
                if e2_hp > 0:
                    print(f"│NAME: {e2_name}")
                    print(f"│HP: {Green}{e2_hp}{End}/{Green}{e2_maxhp}{End}")
                    print(f"│STRENGTH: {Green}{e2_str}{End}")
                    print(f"│MANA: {Green}1{End}")
                    print(f"│WIT: {Green}1{End}")
                    print(f"│DEXTERITY: {Green}{e2_dex}{End}")
                else: print(f"│{e2_name} IS SLAIN!")
                draw(False)
                print(f"│{Red}{name}{End} DEXTERITY IS {Green}{Dexterity}{End}")
                if e_hp > 0:
                    print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}")
                if e2_hp > 0:
                    print(f"│{e2_name} DEXTERITY IS {Green}{e2_dex}{End}")
                print(f"│COMBAT ORDER IS: ",end="")
                if HP > 0 and e_hp > 0 and e2_hp > 0:
                    if Dexterity >= e_dex and Dexterity >= e2_dex:
                        print(f"{Red}{name}{End} - ",end="")
                        CO1 = "P1"
                        if e_dex >= e2_dex:
                            print(f"{e_name} - {e2_name}.")
                            CO2 = "E1"
                            CO3 = "E2"
                        else:
                            print(f"{e2_name} - {e_name}.")
                            CO2 = "E2"
                            CO3 = "E1"
                    elif Dexterity >= e_dex or Dexterity >= e2_dex:
                        CO2 = "P1"
                        if e_dex >= e2_dex:
                            print(f"{e_name} - ",end="")
                            CO1 = "E1"
                            CO3 = "E2"
                        else:
                            print(f"{e2_name} - ",end="")
                            CO1 = "E2"
                            CO3 = "E1"
                        print(f"{Red}{name}{End} - ",end="")
                        if e2_dex >= e_dex*2:
                            print(f"{e_name}.")
                        else:
                            print(f"{e2_name}.")
                    elif Dexterity < e_dex and Dexterity < e2_dex:
                        CO3 = "P1"
                        if e_dex >= e2_dex:
                            print(f"{e_name} - {e2_name} - ",end="")
                            CO1 = "E1"
                            CO2 = "E2"
                        else:
                            print(f"{e2_name} - {e_name} - ",end="")
                            CO1 = "E2"
                            CO2 = "E1"
                        print(f"{Red}{name}{End}.")
                if HP > 0 and e_hp <= 0 and e2_hp > 0:
                    if Dexterity >= e2_dex: print(f"{Red}{name}{End} - {e2_name}.")
                    else: print(f"{e2_name} - {Red}{name}{End}.")
                if HP > 0 and e_hp > 0 and e2_hp <= 0:
                    if Dexterity >= e_dex: print(f"{Red}{name}{End} - {e_name}.")
                    else: print(f"{e_name} - {Red}{name}{End}.")
                draw(False)
                if e_hp > 0:
                    print(f"│{Cyan}1 {End}━ ATTACK {e_name}")
                if e2_hp > 0:
                    print(f"│{Cyan}2 {End}━ ATTACK {e2_name}")
                if e_hp > 0:
                    print(f"│{Cyan}3 {End}━ MAGIC ATTACK {e_name}")
                if e2_hp > 0:
                    print(f"│{Cyan}4 {End}━ MAGIC ATTACK {e2_name}")
                print(f"│{Cyan}5 {End}━ TRICK")
                print(f"│{Cyan}6 {End}━ RUN")
                draw(False)
                combatChoice = input(f"│>{Cyan}")
                print(f"{End}")
                clear()
                validChoice = False
                if combatChoice == "1" and e_hp > 0:
                    validChoice = True
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e_hp -= Strength
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e_hp -= Strength
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e_hp -= Strength
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                
                if combatChoice == "2" and e2_hp > 0:
                    validChoice = True
                    if CO1 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e2_hp -= Strength
                            if e2_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e2_hp -= Strength
                            if e2_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} ATTACKS {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Strength}{End}={Green}{toHit+Strength}{End}.")
                        if toHit+Strength >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
                            e2_hp -= Strength
                            if e2_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")

                if combatChoice == "3" and e_hp > 0:
                    validChoice = True
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
                        print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e_dex*2:
                            print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e_name}!")
                        else: print(f"│{e_name} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                
                if combatChoice == "4" and e2_hp > 0:
                    validChoice = True
                    if CO1 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e2_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e2_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "P1" and HP > 0 and e2_hp > 0:
                        toHit = random.randint(1,20)
                        print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e2_name}!")
                        print(f"│{e2_name} HAS A {Green}DEXTERITY{End} OF {Green}{e2_dex}{End}, AND A DODGE CHANCE OF {Green}{e2_dex*2}{End}.")
                        print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{toHit}{End}+{Green}{Mana}{End}={Green}{toHit+Mana}{End}.")
                        if toHit+Mana >= e2_dex*2:
                            print(f"│{e2_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
                            e2_hp -= Mana
                            if e_hp <= 0:
                                print(f"{Red}{name}{End} KILLED {e2_name}!")
                        else: print(f"│{e2_name} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")

                if combatChoice == "5":
                    validChoice = True
                    enemyTrick = random.randint(1,20)
                    if e_hp > 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TELLS THE {Blue}SKELETONS{End} THAT THEY WORKS FOR THE {Gray}WITCH{End}.")
                        print(f"│{e_name} AND {e2_name} ROLLED A {Green}{enemyTrick}{End}+{Green}1{End}+{Green}1{End}={Green}{enemyTrick+2}{End}.")
                        print(f"│{Red}{name}{End} WIT IS {Green}{Wit}{End}.")
                        if Wit >= enemyTrick+2:
                            print(f"│{e_name} AND {e2_name} FALL FOR THE TRICK AND LEAVE!")
                            fight = False
                            play = True
                        else: print(f"│{e_name} AND {e2_name} DON'T FALL FOR THE TRICK!")
                        input(f"│<")
                    elif e_hp > 0 and e2_hp <= 0:
                        print(f"│{Red}{name}{End} TELLS {e_name} THAT THEY WORKS FOR THE {Gray}WITCH{End}.")
                        print(f"│{e_name} ROLLED A {Green}{enemyTrick}{End}+{Green}1{End}={Green}{enemyTrick+1}{End}.")
                        print(f"│{Red}{name}{End} WIT IS {Green}{Wit}{End}.")
                        if Wit >= enemyTrick+1:
                            print(f"│{e_name} FALLS FOR THE TRICK AND LEAVE!")
                            fight = False
                            play = True
                        else: print(f"│{e_name} DOESN'T FALL FOR THE TRICK!")
                        input(f"│<")
                    elif e_hp <= 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TELLS {e2_name} THAT THEY WORKS FOR THE {Gray}WITCH{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{enemyTrick}{End}+{Green}1{End}={Green}{enemyTrick+1}{End}.")
                        print(f"│{Red}{name}{End} WIT IS {Green}{Wit}{End}.")
                        if Wit >= enemyTrick+1:
                            print(f"│{e2_name} FALLS FOR THE TRICK AND LEAVE!")
                            fight = False
                            play = True
                        else: print(f"│{e2_name} DOESN'T FALL FOR THE TRICK!")
                        input(f"│<")
                    if CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")

                if combatChoice == "6":
                    validChoice = True
                    EscapeRoll = random.randint(1,20)
                    if e_hp > 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TRIES TO RUN AWAY.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{EscapeRoll}{End}+{Green}{Dexterity}{End}={Green}{EscapeRoll+Dexterity}{End}.")
                        print(f"│{Blue}SKELETONS{End} COMBINED DEXTERITY IS {Green}{e_dex+e2_dex}{End}.")
                        if EscapeRoll+Dexterity >= e_dex+e2_dex:
                            print(f"│{Red}{name}{End} GOT AWAY!")
                            fight = False
                            play = True
                        else: print(f"│{Red}{name}{End} FAILED TO GET AWAY!")
                        input(f"│<")
                    elif e_hp > 0 and e2_hp <= 0:
                        print(f"│{Red}{name}{End} TRIES TO RUN AWAY.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{EscapeRoll}{End}+{Green}{Dexterity}{End}={Green}{EscapeRoll+Dexterity}{End}.")
                        print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}.")
                        if EscapeRoll+Dexterity >= e_dex:
                            print(f"│{Red}{name}{End} GOT AWAY!")
                            fight = False
                            play = True
                        else: print(f"│{Red}{name}{End} FAILED TO GET AWAY!")
                        input(f"│<")
                    elif e_hp <= 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TRIES TO RUN AWAY.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{EscapeRoll}{End}+{Green}{Dexterity}{End}={Green}{EscapeRoll+Dexterity}{End}.")
                        print(f"│{e2_name} DEXTERITY IS {Green}{e2_dex}{End}.")
                        if EscapeRoll+Dexterity >= e2_dex:
                            print(f"│{Red}{name}{End} GOT AWAY!")
                            fight = False
                            play = True
                        else: print(f"│{Red}{name}{End} FAILED TO GET AWAY!")
                        input(f"│<")
                    if CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        draw(False)
                    if CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e_name} STRENGTH IS {Green}{e_str}{End}.")
                        print(f"│{e_name} ROLLED A {Green}{toHit}{End}+{Green}{e_str}{End}={Green}{toHit+e_str}{End}.")
                        if toHit+e_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e_str}{End} DAMAGE!")
                            HP -= e_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        toHit = random.randint(1,20)
                        print(f"│{e2_name} ATTACKS {Red}{name}{End}!")
                        print(f"│{Red}{name}{End} HAS A {Green}DEXTERITY{End} OF {Green}{Dexterity}{End}, AND A DODGE CHANCE OF {Green}{Dexterity*2}{End}.")
                        print(f"│{e2_name} STRENGTH IS {Green}{e2_str}{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{toHit}{End}+{Green}{e2_str}{End}={Green}{toHit+e2_str}{End}.")
                        if toHit+e2_str >= Dexterity*2:
                            print(f"│{Red}{name}{End} IS HIT FOR {Green}{e2_str}{End} DAMAGE!")
                            HP -= e2_str
                            if HP <= 0:
                                fight = False
                                play = False
                                run = False
                                dead = True
                        else: print(f"│{Red}{name}{End} DODGES THE ATTACK!")
                        input(f"│<")
                
                if not validChoice:
                    draw(False)
                    print(f"│INVALID INPUT!")
                    draw(False)
                    input(f"│<")
                if e_hp <= 0 and e2_hp <= 0:
                    play = True
                    fight = False
                    clear()
                    draw(False)
                    print(f"│{Red}{name}{End} KILLED {e_name} and {e2_name}!")
                    draw(False)
                    input(f"│<")
                if HP <= 0:
                    play = False
                    fight = False
                    dead = True

    while witchDead:
        print("│ITS DONE. BIT ANTICLIMATIC REALLY.")
        print("│WAIT",end="")
        sys.stdout.flush()
        time.sleep(0.1)
        print(".",end="")
        sys.stdout.flush()
        time.sleep(0.1)
        print(".",end="")
        sys.stdout.flush()
        time.sleep(0.1)
        print(".")
        time.sleep(0.1)
        input(f"│<")
        clear()
        draw(False)
        print(f"│THE {Gray}WITCHES SOUL{End} ATTACKS!")
        draw(False)
        input(f"│<")
        while HP > 1:
            HP -= 1
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
            time.sleep(0.1)
        time.sleep(1)
        clear()
        e_name = f"{Gray}WITCHES SOUL{End}"
        e_hp = 5
        e_maxhp = e_hp
        e_str = 1
        e_mana = 500
        e_wit = 50
        e_dex = Dexterity-1
        atkTimes = 0
        draw(False)
        print(f"│{Red}{name}{End} IS BEING ATTACKED BY {e_name}!")
        draw(False)
        print(f"│NAME: {Red}{name}{End}")
        print(f"│HP: {Green}{HP}{End}/{Green}{MaxHP}{End}")
        print(f"│STRENGTH: {Green}{Strength}{End}")
        print(f"│MANA: {Green}{Mana}{End}")
        print(f"│WIT: {Green}{Wit}{End}")
        print(f"│DEXTERITY: {Green}{Dexterity}{End}")
        draw(False)
        if e_hp > 0:
            print(f"│NAME: {e_name}")
            print(f"│HP: {Green}{e_hp}{End}/{Green}{e_maxhp}{End}")
            print(f"│STRENGTH: {Green}{e_str}{End}")
            print(f"│MANA: {Green}{e_mana}{End}")
            print(f"│WIT: {Green}{e_wit}{End}")
            print(f"│DEXTERITY: {Green}{e_dex}{End}")
        else: print(f"│{e_name} IS SLAIN!")
        draw(False)
        print(f"│{Red}{name}{End} DEXTERITY IS {Green}{Dexterity}{End}")
        print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}")
        print(f"│COMBAT ORDER IS: ",end="")
        if HP > 0:
            if Dexterity >= e_dex:
                print(f"{Red}{name}{End} - {e_name}.")
                CO1 = "P1"
                CO2 = "E1"
            else:
                print(f"{e_name} - {Red}{name}{End}.")
                CO1 = "E1"
                CO2 = "P1"
        draw(False)
        print(f"│{Cyan}1 {End}━ ATTACK {e_name}")
        print(f"│{Cyan}2 {End}━ MAGIC ATTACK {e_name}")
        print(f"│{Cyan}3 {End}━ TRICK")
        print(f"│{Cyan}4 {End}━ RUN")
        draw(False)
        combatChoice = input(f"│>{Cyan}")
        print(f"{End}")
        clear()
        validChoice = False
        bossLines = ["YOU ARE BLINDED BY AMBITION!","IF YOU BELIEVE YOU CAN KILL ME, YOU ARE A FOOL!","YOUR INABILITY TO JUDGE THE HOPELESSNESS OF YOUR SITUATION WILL LEAD TO YOUR DEATH!","DESPAIR!","YOUR FATE LIES IN THE PALM OF MY HAND!","DO YOU KNOW THE DEFINITION OF INSANITY? YOU WILL LEARN SOON.","ONLY A MASOCHIST WOULD CONTINUE TRYING.","THERE IS AN EASTER EGG WHERE, UPON PRESSING THE KEYS 'ALT' AND 'F4', YOU GET TO SURVIVE!"]
        if combatChoice == "1":
            atkTimes += 1
            draw(False)
            validChoice = True
            print(f"│{Red}{name}{End} ATTACKS {e_name}!")
            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
            print(f"│{Red}{name}{End} {Green}STRENGTH{End} IS {Green}{Strength}{End}.")
            print(f"│{Red}{name}{End} ROLLED A {Green}{e_dex*2-Strength}{End}+{Green}{Strength}{End}={Green}{e_dex*2}{End}.")
            print(f"│{e_name} IS HIT FOR {Green}{Strength}{End} DAMAGE!")
            e_hp -= Strength
            if e_hp <= 0:
                print(f"{Red}{name}{End} KILLED {e_name}!")

        if combatChoice == "2":
            draw(False)
            validChoice = True
            print(f"│{Red}{name}{End} CASTS A SPELL TOWARD {e_name}!")
            print(f"│{e_name} HAS A {Green}DEXTERITY{End} OF {Green}{e_dex}{End}, AND A DODGE CHANCE OF {Green}{e_dex*2}{End}.")
            print(f"│{Red}{name}{End} {Green}MANA{End} IS {Green}{Mana}{End}.")
            print(f"│{Red}{name}{End} ROLLED A {Green}{e_dex*2-Mana}{End}+{Green}{Mana}{End}={Green}{e_dex*2}{End}.")
            print(f"│{e_name} IS HIT FOR {Green}{Mana}{End} DAMAGE!")
            e_hp -= Mana
            if e_hp <= 0:
                print(f"{Red}{name}{End} KILLED {e_name}!")
            input(f"│<")
        
        if not validChoice and HP > 0:
            draw(False)
            print(f"│INVALID INPUT!")
            draw(False)
            input(f"│<")

        if e_hp <= 0:
            play = False
            fight = False
            bossFight = False
            witchDead = True
            clear()
            draw(False)
            print(f"│{Red}{name}{End} KILLED {e_name}!")
            draw(False)
            input(f"│<")
            clear()
            draw(False)
            print(f"│CONGRATULATIONS, YOU WON!")
            input(f"│<")
            HP = 9999
            MaxHP = HP
            Strength = 999
            Mana = 999
            Dexterity = 999
            Wit = 999

            floor = 1
            x = 0
            y = 10
            blood_glasses = 0
            alive = True
            validChoice = True
            secret1 = 0
            secret2 = 0
            key1 = 0
            key2 = 0
            save()
            text = "│GOOD BYE, AND GOOD LUCK!"
            for char in text:
                print(char,end="")
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(1)
            quit()

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