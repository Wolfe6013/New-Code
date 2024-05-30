import random, os, time
os.system("cls")

if True: #Colours
    Bold = f"\033[1;37;40m"
    Gray = f"\033[0;30;40m"
    Red = f"\033[0;31;40m"
    Green = f"\033[0;32;40m"
    Yellow = f"\033[0;33;40m"
    Blue = f"\033[0;34;40m"
    Purple = f"\033[0;35;40m"
    Cyan = f"\033[0;36;40m"
    End = f"\033[0m"

placedShips = 17
h = f"{Red}◉{End}"
m = f"{End}◉"
b = f"{Gray}▢{End}"
s = f"{End}☗"


p1Map = [[b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b]]
p1Hit = [[b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b]]

p2Map = [[b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b]]
p2Hit = [[b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b,b,b]]

def placeP1Map():
    print(f"{Cyan}   1 2 3 4 5 6 7 8 9 10")
    pos = 0
    for y in p1Map:
        pos += 1
        if pos < 10 and pos > 0:
            print(f"{Blue}{pos}  ",end="")
        else:
            print(f"{Blue}{pos} ",end="")
        for x in y:
            print(f"{x} ",end="")
        print()

def placeP2Map():
    print(f"{Cyan}   1 2 3 4 5 6 7 8 9 10")
    pos = 0
    for y in p2Map:
        pos += 1
        if pos < 10 and pos > 0:
            print(f"{Blue}{pos}  ",end="")
        else:
            print(f"{Blue}{pos} ",end="")
        for x in y:
            print(f"{x} ",end="")
        print()

def placeP2Hit():
    print(f"{Cyan}   1 2 3 4 5 6 7 8 9 10")
    pos = 0
    for y in p2Hit:
        pos += 1
        if pos < 10 and pos > 0:
            print(f"{Blue}{pos}  ",end="")
        else:
            print(f"{Blue}{pos} ",end="")
        for x in y:
            print(f"{x} ",end="")
        print()

def P1Turn():
    placeP2Hit()

def placeShips():
    global placedShips
    while placedShips > 0:
        os.system("cls")
        print(f"{Green}PLACE YOUR SHIPS!\nPLACE 5, 4, 3, 3 AND 2 LONG SHIPS (NO DIAGONALS)!{End}")
        placeP1Map()
        position: str = input(f"Positions: ({Cyan}x{End},{Blue}y{End}) ")
        coords = position.split(",")
        try:
            x = int(coords[0])-1
            y = int(coords[1])-1
            if p1Map[y][x] == b:
                p1Map[y][x] = s
                placedShips -= 1
        except:
            ...

def enemyShips():
    shipsList: list[int] = [5,4,3,3,2]
    while len(shipsList) > 0:
        print(shipsList)
        try:
            whichShip = random.randint(0,4)
            xPos = random.randint(0,9)
            yPos = random.randint(0,9)
            print(f"{whichShip} which ship")
            print(f"{xPos},{yPos}")
            vertOrHorz = random.choice(["Down","Right"])
            print(f"{vertOrHorz}")
            if vertOrHorz == "Down":
                works = True
                for y in range(yPos,yPos+shipsList[whichShip]):
                    if p2Map[y][xPos] != b:
                        works = False
                if works:
                    for y in range(yPos,yPos+shipsList[whichShip]):
                        p2Map[y][xPos] = s
                    print(f"Removing {shipsList[whichShip]}")
                    shipsList.pop(whichShip)
            if vertOrHorz == "Right":
                works = True
                for x in range(xPos,xPos+shipsList[whichShip]):
                    if p2Map[yPos][x] != b:
                        works = False
                if works:
                    for x in range(xPos,xPos+shipsList[whichShip]):
                        p2Map[yPos][x] = s
                    print(f"Removing {shipsList[whichShip]}")
                    shipsList.pop(whichShip)
        except:
            ...
    os.system("cls")

if __name__ == "__main__":
    #placeShips()
    os.system("cls")
    placeShips()
    enemyShips()
    placeP1Map()
    placeP2Map()