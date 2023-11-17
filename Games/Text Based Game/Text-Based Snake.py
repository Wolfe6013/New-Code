import os, random, time, sys, pyautogui, keyboard

def clear():
    os.system("cls")

moved = False

def See_Coords():
    global coords, moved, head
    for l in coords:
        print(coords,end="")
    print()
    keyboard.release("c")

def Move_Up():
    global coords, moved, head
    if moved == False:
        moved = True
        del coords[-1]
        y = coords[0][0]
        x = coords[0][1]
        newCoord = [y-1,x]
        coords.reverse()
        coords.append(newCoord)
        coords.reverse()
        head = newCoord

def Move_Down():
    global coords, moved, head
    if moved == False:
        moved = True
        del coords[-1]
        y = coords[0][0]
        x = coords[0][1]
        newCoord = [y+1,x]
        coords.reverse()
        coords.append(newCoord)
        coords.reverse()
        head = newCoord

def Move_Left():
    global coords, moved, head
    if moved == False:
        moved = True
        del coords[-1]
        y = coords[0][0]
        x = coords[0][1]
        newCoord = [y,x-1]
        coords.reverse()
        coords.append(newCoord)
        coords.reverse()
        head = newCoord

def Move_Right():
    global coords, moved, head
    if moved == False:
        moved = True
        del coords[-1]
        y = coords[0][0]
        x = coords[0][1]
        newCoord = [y,x+1]
        coords.reverse()
        coords.append(newCoord)
        coords.reverse()
        head = newCoord

if True: #Colours
    Gray = f"\033[1;30;40m"
    Red = f"\033[1;31;40m"
    Green = f"\033[1;32;40m"
    Yellow = f"\033[1;33;40m"
    Blue = f"\033[1;34;40m"
    Purple = f"\033[1;35;40m"
    Cyan = f"\033[1;36;40m"
    End = f"\033[0m"

if True: #Title
    clear()
    print(f"{Green}",end="")
    title = "SNAKE GAME"
    for char in title:
        print(char,end="")
        sys.stdout.flush()
        time.sleep(0.05)

coords = [[5,10],[5,9],[5,8],[5,7]]

head = 5,10

applePos = 5,15

print(f"{End}")
input("<")
clear()
time.sleep(0.5)

def drawMap():
    global moved
    if moved == False:
        vert = coords[1][0]-head[0]
        hori = coords[1][1]-head[1]

        if vert == 1:
            Move_Up()
        elif vert == -1:
            Move_Down()
        elif hori == 1:
            Move_Right()
        elif hori == -1:
            Move_Left()

    clear()
    map = ["┏━━━━━━━━━━━━━━━━━━━━┓",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "│                    │",
            "┗━━━━━━━━━━━━━━━━━━━━┛"]

    y = 0
    x = 0
    for mapY in map:
        for mapX in mapY:
            space = True
            for a in coords:
                if y == head[0] and x == head[1]:
                    print(f"{Red}#{End}",end="")
                    space = False
                if y == a[0] and x == a[1]:
                    print(f"{Green}#{End}",end="")
                    space = False
            if y == applePos[0] and x == applePos[1]:
                print(f"{Red}O{End}",end="")
            elif space:
                print(f"{Gray}{mapX}{End}",end="")
            x += 1
        print()
        y += 1
        x = 0
    moved = False

keyboard.add_hotkey('W', Move_Up)
keyboard.add_hotkey('S', Move_Down)
keyboard.add_hotkey('A', Move_Left)
keyboard.add_hotkey('D', Move_Right)
keyboard.add_hotkey('C', See_Coords)

while True:
    drawMap()
    time.sleep(0.5)