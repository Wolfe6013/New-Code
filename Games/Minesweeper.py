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

FlagOrBreak = "Break"
GameOver = False
f = f"🚩"
b = f"{Gray}⬛{End}"
s = f"{End}💥"
Zero = "  "
One = "1️⃣ "
Two = "2️⃣ "
Three = "3️⃣ "
Four = "4️⃣ "
Five = "5️⃣ "
Six = "6️⃣ "
Seven = "7️⃣ "
Eight = "8️⃣ "

Map = [[b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b],
       [b,b,b,b,b,b,b,b,b,b]]

BombMap = [[b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b],
           [b,b,b,b,b,b,b,b,b,b]]

def DrawMap():
    global TotalBombs, FlagNum
    print(f"{TotalBombs} - {int(TotalBombs)-int(FlagNum)}")
    Num = -1
    print(f"  {Cyan}{'0 1 2 3 4 5 6 7 8 9':^22}{End}")
    for y in Map:
        Num += 1
        print(f"{Blue}{Num:^2}{End}",end="")
        for x in y:
            print(f"{x}",end="")
        print()
    print(f"{Red}{FlagOrBreak}{End}")

def PlaceBombs():
    BombsPlaced: int = 0
    while int(BombsPlaced) < int(TotalBombs):
        y = random.randint(0,9)
        x = random.randint(0,9)
        try:
            if BombMap[y][x] == b:
                BombMap[y][x] = s
                BombsPlaced += 1
        except:
            ...

def ReBalanceCells():
    for y in range(10):
        for x in range(10):
            NumberOfBombs = 0
            if BombMap[y][x] != s: #Bomb Count
                if y > 0:
                    if BombMap[y-1][x] == s:
                        NumberOfBombs += 1
                if y < 9:
                    if BombMap[y+1][x] == s:
                        NumberOfBombs += 1
                if x > 0:
                    if BombMap[y][x-1] == s:
                        NumberOfBombs += 1
                if x < 9:
                    if BombMap[y][x+1] == s:
                        NumberOfBombs += 1
                if y > 0 and x > 0:
                    if BombMap[y-1][x-1] == s:
                        NumberOfBombs += 1
                if y < 9 and x > 0:
                    if BombMap[y+1][x-1] == s:
                        NumberOfBombs += 1
                if y > 0 and x < 9:
                    if BombMap[y-1][x+1] == s:
                        NumberOfBombs += 1
                if y < 9 and x < 9:
                    if BombMap[y+1][x+1] == s:
                        NumberOfBombs += 1
            if NumberOfBombs == 0 and BombMap[y][x] != s:
                BombMap[y][x] = Zero
            if NumberOfBombs == 1:
                BombMap[y][x] = One
            if NumberOfBombs == 2:
                BombMap[y][x] = Two
            if NumberOfBombs == 3:
                BombMap[y][x] = Three
            if NumberOfBombs == 4:
                BombMap[y][x] = Four
            if NumberOfBombs == 5:
                BombMap[y][x] = Five
            if NumberOfBombs == 6:
                BombMap[y][x] = Six
            if NumberOfBombs == 7:
                BombMap[y][x] = Seven
            if NumberOfBombs == 8:
                BombMap[y][x] = Eight

def ChoosePos():
    global FlagOrBreak
    valid = False
    while not valid:
        try:
            position: str = input(f"Positions: ({Cyan}x{End},{Blue}y{End}) ")
            if (position != "Flag" and position != "Break"):
                coords = position.split(",")
                coords[0] = int(coords[0])
                coords[1] = int(coords[1])
                if coords[0] >= 0 and coords[0] <= 9 and coords[1] >= 0 and coords[1] <= 9:
                    valid = True
                    return coords
            else:
                if position == "Flag":
                    FlagOrBreak = "Flag"
                    valid = True
                    return coords
                elif position == "Break":
                    FlagOrBreak = "Break"
                    valid = True
                    return coords
        except:
            ...

def Start():
    coords = ChoosePos()
    x = coords[0]
    y = coords[1]
    BombMap[y][x] = Zero
    BombMap[y+1][x] = Zero
    BombMap[y-1][x] = Zero
    BombMap[y][x+1] = Zero
    BombMap[y][x-1] = Zero
    BombMap[y+1][x+1] = Zero
    BombMap[y+1][x-1] = Zero
    BombMap[y-1][x+1] = Zero
    BombMap[y-1][x-1] = Zero
    BombMap[y+2][x-2] = Zero
    BombMap[y+2][x-1] = Zero
    BombMap[y+2][x] = Zero
    BombMap[y+2][x+1] = Zero
    BombMap[y+2][x+2] = Zero
    BombMap[y-2][x-2] = Zero
    BombMap[y-2][x-1] = Zero
    BombMap[y-2][x] = Zero
    BombMap[y-2][x+1] = Zero
    BombMap[y-2][x+2] = Zero
    BombMap[y+1][x+2] = Zero
    BombMap[y][x+2] = Zero
    BombMap[y-1][x+2] = Zero
    BombMap[y+1][x-2] = Zero
    BombMap[y][x-2] = Zero
    BombMap[y-1][x-2] = Zero
    Map[y][x] = BombMap[y][x]
    Map[y+1][x] = BombMap[y+1][x]
    Map[y-1][x] = BombMap[y-1][x]
    Map[y][x+1] = BombMap[y][x+1]
    Map[y][x-1] = BombMap[y][x-1]
    Map[y+1][x+1] = BombMap[y+1][x+1]
    Map[y+1][x-1] = BombMap[y+1][x-1]
    Map[y-1][x+1] = BombMap[y-1][x+1]
    Map[y-1][x-1] = BombMap[y-1][x-1]
    PlaceBombs()
    ReBalanceCells()

def BreakCell():
    global GameOver, b
    coords = ChoosePos()
    if type(coords) == list:
        x = coords[0]
        y = coords[1]
        if FlagOrBreak == "Break" and Map[y][x] != f:
            Map[y][x] = BombMap[y][x]
            if BombMap[y][x] == s:
                GameOver = True
                for a in range(10):
                    for b in range(10):
                        if BombMap[a][b] == s:
                            Map[a][b] = BombMap[a][b]
            else:
                if BombMap[y][x] == Zero:
                    try: Map[y+1][x] = BombMap[y+1][x]
                    except: ...
                    try: Map[y+1][x+1] = BombMap[y+1][x+1]
                    except: ...
                    try: Map[y+1][x-1] = BombMap[y+1][x-1]
                    except: ...
                    try: Map[y-1][x] = BombMap[y-1][x]
                    except: ...
                    try: Map[y-1][x+1] = BombMap[y-1][x+1]
                    except: ...
                    try: Map[y-1][x-1] = BombMap[y-1][x-1]
                    except: ...
                    try: Map[y][x+1] = BombMap[y][x+1]
                    except: ...
                    try: Map[y][x-1] = BombMap[y][x-1]
                    except: ...
        elif FlagOrBreak == "Flag":
            if Map[y][x] == f:
                Map[y][x] = b
            elif Map[y][x] == b:
                Map[y][x] = f

if __name__ == "__main__":
    SearchedCells = 0
    FlagNum = 0
    TotalBombs: int = input("How Many Bombs? ")
    if int(TotalBombs) > 75:
        TotalBombs = 75
    os.system("cls")
    DrawMap()
    Start()
    ReBalanceCells()
    while (not GameOver) and (SearchedCells < (100-int(TotalBombs))):
        os.system("cls")
        DrawMap()
        BreakCell()
        SearchedCells = 0
        FlagNum = 0
        for y in range(10):
            for x in range(10):
                if Map[y][x] != b and Map[y][x] != f:
                    SearchedCells += 1
                if Map[y][x] == f or Map[y][x] == s:
                    FlagNum += 1
    os.system("cls")
    DrawMap()
    if GameOver:
        print(f"YOU LOST!")
    else:
        print(f"YOU WON!")