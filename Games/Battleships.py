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
first = True

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

def P1Turn():
    validShot = False
    while not validShot:
        os.system("cls")
        placeP2Hit()
        placeP1Map()
        xy: str = input("Where to attack (Top Board x,y)? ")
        coords = xy.split(",")
        try:
            x = int(coords[0])-1
            y = int(coords[1])-1
            if p2Map[y][x] == s:
                if p2Hit[y][x] == b:
                    p2Hit[y][x] = h
                    validShot = True
            else:
                if p2Hit[y][x] == b:
                    p2Hit[y][x] = m
                    validShot = True
        except:
            ...

def P2Turn():
    global first
    if first == True:
        hitcoords = [10]
        first = False
    tries = 0
    validShot = False
    directionList: list[str] = ["U","L","R","D"]
    direction: list[str] = ["U","L","R","D"]
    move = random.choice(direction)
    while not validShot:
        tries += 1
        print(tries)
        time.sleep(0.1)
        try:
            if len(hitcoords) == 1 or tries > 50:
                print("Hitcoords =",hitcoords)
                time.sleep(1)
                x = random.randint(0,9)
                y = random.randint(0,9)
                move = "A"
                direction.append("A")
            else:
                print("Hitcoords =",hitcoords)
                x = hitcoords[2]
                y = hitcoords[1]
                if move == "U":
                    y += 1
                elif move == "D":
                    y -= 1
                elif move == "R":
                    x += 1
                else:
                    x -= 1
            if p1Map[y][x] == s:
                p1Map[y][x] = h
                validShot = True
                direction = directionList
                hitcoords: list[int] = [y,x]
                print(hitcoords)
                input()
            elif p1Map[y][x] == h:
                hitcoords = [y,x]
            elif p1Map[y][x] == b:
                p1Map[y][x] = m
                validShot = True
                direction.remove(move)
                if len(direction) < 1:
                    direction = directionList
                    hitcoords = [10]
            else:
                direction.remove(move)
        except:
            ...
    print(f"Try: {tries}")
    input()

if __name__ == "__main__":
    #placeShips()
    os.system("cls")
    placeShips()
    enemyShips()
    done = False
    while not done:
        sunkShipsP1 = 0
        sunkShipsP2 = 0
        P1Turn()
        P2Turn()
        for x in p1Map:
            for y in x:
                if y == h:
                    sunkShipsP1 += 1
        for x in p2Hit:
            for y in x:
                if y == h:
                    sunkShipsP2 += 1
        if sunkShipsP1 == 17 or sunkShipsP2 == 17:
            done = True
    if sunkShipsP1 == 17:
        os.system("cls")
        print(f"┏━━━━━━━━━━━━━━━━━━━━┓")
        print(f"┃{'COMPUTER WINS!':^20}┃")
        print(f"┗━━━━━━━━━━━━━━━━━━━━┛")
    if sunkShipsP2 == 17:
        os.system("cls")
        print(f"┏━━━━━━━━━━━━━━━━━━━━┓")
        print(f"┃{'PLAYER WINS!':^20}┃")
        print(f"┗━━━━━━━━━━━━━━━━━━━━┛")