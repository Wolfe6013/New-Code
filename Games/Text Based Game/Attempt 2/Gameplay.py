import os, random, time, sys, pyautogui, keyboard

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

moveList = "+","k","B","*"," ","~"

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
        draw(True)
        validCommand = False
        if pointChange == "0":
            validCommand = True
            if points > 0:
                if points == 1:
                    y_n = input(f"│YOU HAVE {points} POINT   REMAINING. DO YOU WISH TO CONTINUE (Y/N)? ")
                else:
                    y_n = input(f"│YOU HAVE {points} POINTS REMAINING. DO YOU WISH TO CONTINUE (Y/N)? ")
                if y_n == 'Y' or y_n == 'y':
                    changingStats = False
            else:
                changingStats = False
        if pointChange == "S1" and Strength > 5:
            validCommand = True
            points += 1
            Strength -= 1
        if pointChange == "S2" and Mana > 5:
            validCommand = True
            points += 1
            Mana -= 1
        if pointChange == "S3" and Wit > 5:
            validCommand = True
            points += 1
            Wit -= 1
        if pointChange == "S4" and Dexterity > 5:
            validCommand = True
            points += 1
            Dexterity -= 1
        if pointChange == "W1" and Strength < 15 and points > 0:
            validCommand = True
            points -= 1
            Strength += 1
        if pointChange == "W2" and Mana < 15 and points > 0:
            validCommand = True
            points -= 1
            Mana += 1
        if pointChange == "W3" and Wit < 15 and points > 0:
            validCommand = True
            points -= 1
            Wit += 1
        if pointChange == "W4" and Dexterity < 15 and points > 0:
            validCommand = True
            points -= 1
            Dexterity += 1
        if not validCommand:
            print(f"│THAT IS NOT A VALID OPTION.")
            input(f"│<")

#┣┫┳┻┿┏┓┗┛┃━

y_max = 18
x_max = 21

def fightSelectUp():
    global fightOptionSelected
    fightOptionSelected -= 1

def fightSelectDown():
    global fightOptionSelected
    fightOptionSelected += 1

def moveW():
    global x, y, validCommand, moveList
    validCommand = True
    if map[y-1][x] in moveList: y -= 1
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)
    
def moveS():
    global x, y, validCommand, moveList
    validCommand = True
    if map[y+1][x] in moveList: y += 1
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)

def moveA():
    global x, y, validCommand, moveList, f_u_option, floor
    validCommand = True
    x -= 2
    if f_u_option:
        floor += 1
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)

def moveD():
    global x, y, validCommand, moveList, f_u_option, floor
    validCommand = True
    x += 2
    if f_d_option:
        floor -= 1
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)

def search():
    global searching, roll, rollMod, Wit
    validCommand = True
    searching = True
    roll = random.randint(1,20)
    rollMod = Wit
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)

def play0():
    global play, menu
    validCommand = True
    save()
    play = False
    menu = True
    keyboard.unhook_all_hotkeys()
    time.sleep(0.1)

def calFight(atker,atked,dodge,atk,hp):
    global name, e_name, e2_name, HP, e_hp, e2_hp, Strength, Mana, e_str, e2_str
    draw(False)
    roll = random.randint(1,20)
    print(f"│{atker} ATTACKS {atked}!\n│{atker} ROLLED A {Green}{roll}{End}+{Green}{atk}{End}={Green}{roll+atk}{End} TO HIT {atked}!\n│{atked} HAS A DODGE CHANCE OF {Green}{dodge}{End}!")
    if dodge > roll+atk:
        print(f"│IT MISSED!")
    else:
        print(f"│IT HIT FOR {atk} DAMAGE!")
        if str(name) == str(atked):
            HP -= atk
            if HP <= 0:
                HP = 0
                print(f"│{atked} IS SLAIN!")
        if str(e_name) == str(atked):
            e_hp -= atk
            if e_hp <= 0:
                e_hp = 0
                print(f"│{atked} IS SLAIN!")
        if str(e2_name) == str(atked):
            e2_hp -= atk
            if e2_hp <= 0:
                e2_hp = 0
                print(f"│{atked} IS SLAIN!")

def drawMap():
    global map, x, y, moveList, secret1, secret2, blood_glasses, roll, rollMod, searching
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
    searching = False

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
            name = f"\033[1;31;40m{name}\033[0m"
            print(f"│WELCOME {name}!")
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
                    print(f"│WELCOME BACK {name}!")
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
    while play:
        clear()
        draw(False)
        print(f"│LOCATION: FLOOR {floor}")
        draw(False)
        drawMap()
        draw(False)
        print(f"│NAME: {name}")
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
        print(f"│{Cyan}1 {End}━ SEARCH")
        print(f"│{Cyan}2 {End}━ SAVE")
        n_option = False
        s_option = False
        e_option = False
        w_option = False
        f_u_option = False
        f_d_option = False
        keyboard.add_hotkey('0', play0)
        keyboard.add_hotkey('1', search)
        keyboard.add_hotkey('2', save)

        if map[y-1][x] in moveList and y > 0:
            print(f"│{Cyan}W {End}━ NORTH")
            keyboard.add_hotkey('W', moveW)
        if map[y+1][x] in moveList and y < y_max:
            print(f"│{Cyan}S {End}━ SOUTH")
            keyboard.add_hotkey('S', moveS)
        if map[y][x-2] in moveList and map[y][x-1] in moveList and x-1 > 0:
            print(f"│{Cyan}A {End}━ WEST")
            keyboard.add_hotkey('A', moveA)
        if map[y][x-1] == "▲" and not w_option:
            print(f"│{Cyan}A {End}━ WEST")
            f_u_option = True
            keyboard.add_hotkey('A', moveA)
        if map[y][x+2] in moveList and map[y][x+1] in moveList and x+1 < x_max:
            print(f"│{Cyan}D {End}━ EAST")
            keyboard.add_hotkey('D', moveD)
        if map[y][x+1] == "▼" and not e_option:
            print(f"│{Cyan}D {End}━ EAST")
            f_d_option = True
            keyboard.add_hotkey('D', moveD)
        draw(False)
        keyboard.read_key()

        if map[y][x] == "k":
            print(f"│YOU FOUND A {Purple}KEY{End}!")
            if key1 == 1:
                if key2 == 1: print(f"│{Red}CHEATER{End}")
                else:
                    key2 = 1
                    play = False
                    fight = True
                    save()
                    fightOptionSelected = 1
                    fightID = 1
            else: key1 = 1
            save()
            input(f"│<")

        if map[y][x] == "B":
            print(f"│FOUND {Purple}BLOOD GLASSES{End}!")
            blood_glasses = 1
            save()
            input(f"│<")

        if map[y][x] == "~":
            fight = True
            save()
            fightOptionSelected = 1
            fightID = 2
            play = False
    while fight:
        if HP > 0:
            clear()
            draw(False)
            if fightID == 1:
                print(f"│{name} IS BEING ATTACKED BY 2 {Blue}SKELETONS{End}!")

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
            elif fightID == 2:
                print(f"│{name} IS BEING ATTACKED BY AN UNFINISHED WITCH!")

                e_name = f"{Gray}WITCH{End}"
                e_hp = 20
                e_maxhp = e_hp
                e_str = 10
                e_dex = 12

                e2_name = f"{Blue}N/A{End}"
                e2_hp = 0
                e2_maxhp = e_hp
                e2_str = 0
                e2_dex = 0
            else:
                print(f"│{name} IS BEING ATTACKED BY A GLITCH! IT BROKE! FUCK! RELOAD YOUR GAME...")

                e_name = f"{Blue}GLITCH{End}"
                e_hp = 9999999999
                e_maxhp = e_hp+1
                e_str = 9999999999
                e_dex = 9999999999

                e2_name = f"{Blue}GLITCH{End}"
                e2_hp = 9999999999
                e2_maxhp = e2_hp+1
                e2_str = 9999999999
                e2_dex = 9999999999
            keyboard.unhook_all_hotkeys()
            draw(False)
            print(f"│NAME: {name}")
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
                draw(False)
            if e2_hp > 0:
                print(f"│NAME: {e2_name}")
                print(f"│HP: {Green}{e2_hp}{End}/{Green}{e2_maxhp}{End}")
                print(f"│STRENGTH: {Green}{e2_str}{End}")
                print(f"│MANA: {Green}1{End}")
                print(f"│WIT: {Green}1{End}")
                print(f"│DEXTERITY: {Green}{e2_dex}{End}")
                draw(False)
            print(f"│{name} DEXTERITY IS {Green}{Dexterity}{End}")
            if e_hp > 0:
                print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}")
            if e2_hp > 0:
                print(f"│{e2_name} DEXTERITY IS {Green}{e2_dex}{End}")
            print(f"│COMBAT ORDER IS: ",end="")
            if HP > 0 and e_hp > 0 and e2_hp > 0:
                if Dexterity >= e_dex and Dexterity >= e2_dex:
                    print(f"{name} - ",end="")
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
                    print(f"{name} - ",end="")
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
                    print(f"{name}.")
            if HP > 0 and e_hp <= 0 and e2_hp > 0:
                if Dexterity >= e2_dex: print(f"{name} - {e2_name}.")
                else: print(f"{e2_name} - {name}.")
            if HP > 0 and e_hp > 0 and e2_hp <= 0:
                if Dexterity >= e_dex: print(f"{name} - {e_name}.")
                else: print(f"{e_name} - {name}.")
            draw(False)
            if e_hp > 0:
                print(f"│ATTACK {e_name}",end="")
            if fightOptionSelected == 1:
                print(" ◄─")
                keyboard.add_hotkey("down",fightSelectDown)
            elif fightOptionSelected < 1:
                print(" ◄─")
                keyboard.add_hotkey("down",fightSelectDown)
                fightOptionSelected = 1
            else:
                print()
            if e2_hp > 0:
                print(f"│ATTACK {e2_name}",end="")
            if fightOptionSelected == 2:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
                keyboard.add_hotkey("down",fightSelectDown)
            else:
                print()
            if e_hp > 0:
                print(f"│MAGIC ATTACK {e_name}",end="")
            if fightOptionSelected == 3:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
                keyboard.add_hotkey("down",fightSelectDown)
            else:
                print()
            if e2_hp > 0:
                print(f"│MAGIC ATTACK {e2_name}",end="")
            if fightOptionSelected == 4:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
                keyboard.add_hotkey("down",fightSelectDown)
            else:
                print()
            print(f"│TRICK",end="")
            if fightOptionSelected == 5:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
                keyboard.add_hotkey("down",fightSelectDown)
            else:
                print()
            print(f"│RUN",end="")
            if fightOptionSelected == 6:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
            elif fightOptionSelected > 6:
                print(" ◄─")
                keyboard.add_hotkey("up",fightSelectUp)
                fightOptionSelected = 6
            else:
                print()
            draw(False)
            KEY = keyboard.read_key()
            if KEY == "space":
                clear()
                if fightOptionSelected == 1:
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Strength,e_hp)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Strength,e_hp)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Strength,e_hp)
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                if fightOptionSelected == 2:
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Strength,e2_hp)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Strength,e2_hp)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Strength,e2_hp)
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                if fightOptionSelected == 3:
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Mana,e_hp)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Mana,e_hp)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e_name,e_dex*2,Mana,e_hp)
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                if fightOptionSelected == 4:
                    if CO1 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Mana,e2_hp)
                    elif CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Mana,e2_hp)
                    elif CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "P1" and HP > 0 and e_hp > 0:
                        calFight(name,e2_name,e2_dex*2,Mana,e2_hp)
                    elif CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                if fightOptionSelected == 5:
                    draw(False)
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
                    elif e_hp > 0 and e2_hp <= 0:
                        print(f"│{Red}{name}{End} TELLS {e_name} THAT THEY WORKS FOR THE {Gray}WITCH{End}.")
                        print(f"│{e_name} ROLLED A {Green}{enemyTrick}{End}+{Green}1{End}={Green}{enemyTrick+1}{End}.")
                        print(f"│{Red}{name}{End} WIT IS {Green}{Wit}{End}.")
                        if Wit >= enemyTrick+1:
                            print(f"│{e_name} FALLS FOR THE TRICK AND LEAVE!")
                            fight = False
                            play = True
                        else: print(f"│{e_name} DOESN'T FALL FOR THE TRICK!")
                    elif e_hp <= 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TELLS {e2_name} THAT THEY WORKS FOR THE {Gray}WITCH{End}.")
                        print(f"│{e2_name} ROLLED A {Green}{enemyTrick}{End}+{Green}1{End}={Green}{enemyTrick+1}{End}.")
                        print(f"│{Red}{name}{End} WIT IS {Green}{Wit}{End}.")
                        if Wit >= enemyTrick+1:
                            print(f"│{e2_name} FALLS FOR THE TRICK AND LEAVE!")
                            fight = False
                            play = True
                        else: print(f"│{e2_name} DOESN'T FALL FOR THE TRICK!")
                    if CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                if fightOptionSelected == 6:
                    draw(False)
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
                    elif e_hp > 0 and e2_hp <= 0:
                        print(f"│{Red}{name}{End} TRIES TO RUN AWAY.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{EscapeRoll}{End}+{Green}{Dexterity}{End}={Green}{EscapeRoll+Dexterity}{End}.")
                        print(f"│{e_name} DEXTERITY IS {Green}{e_dex}{End}.")
                        if EscapeRoll+Dexterity >= e_dex:
                            print(f"│{Red}{name}{End} GOT AWAY!")
                            fight = False
                            play = True
                        else: print(f"│{Red}{name}{End} FAILED TO GET AWAY!")
                    elif e_hp <= 0 and e2_hp > 0:
                        print(f"│{Red}{name}{End} TRIES TO RUN AWAY.")
                        print(f"│{Red}{name}{End} ROLLED A {Green}{EscapeRoll}{End}+{Green}{Dexterity}{End}={Green}{EscapeRoll+Dexterity}{End}.")
                        print(f"│{e2_name} DEXTERITY IS {Green}{e2_dex}{End}.")
                        if EscapeRoll+Dexterity >= e2_dex:
                            print(f"│{Red}{name}{End} GOT AWAY!")
                            fight = False
                            play = True
                        else: print(f"│{Red}{name}{End} FAILED TO GET AWAY!")
                    if CO1 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO1 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO2 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO2 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                    if CO3 == "E1" and HP > 0 and e_hp > 0 and fight:
                        calFight(e_name,name,Dexterity*2,e_dex,HP)
                    elif CO3 == "E2" and HP > 0 and e2_hp > 0 and fight:
                        calFight(e2_name,name,Dexterity*2,e2_dex,HP)
                draw(False)
                input(f"│<")
        else:
            dead = True
            fight = False

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