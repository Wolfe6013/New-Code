import os, random, time, sys, pyautogui, keyboard

###--- Screen is 198 characters long       ---###
###--- Ctrl -- to make screen correct size ---###

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

Library1 = []
Library2 = []
Hand1 = []
Hand2 = []
Graveyard1 = []
Graveyard2 = []
Exile1 = []
Exile2 = []
Life1 = 40
Life2 = 40
Board1 = []
Board2 = ["Archelos, Lagoon Mystic","Isperia, Supreme Judge"]
MVList = [f"1BGU",f"4WU"]
TextList = ["As long as Archelos, Lagoon Mystic is untapped, other permanants enter the battlefield untapped. As long as Archelos, Lagoon Mystic is tapped, other permanants enter the battlefield tapped.",f"{'Flying':<34}When a creature attacks you or a planeswalker you control, you may draw a card."]
NewTestList = []
###--- Text is up to 34 characters per line ---###

def SetUp():
    Deck1 = open(f"C:\\Users\\210108\\Downloads\\Texted Based MTG\\Deck1.txt")
    Deck2 = open(f"C:\\Users\\210108\\Downloads\\Texted Based MTG\\Deck2.txt")
    data = Deck1.read()
    fileCards = data.split("\n") 
    for x in fileCards:
        xList = list(x)
        for y in xList:
            Library1.append(y)
    data = Deck2.read()
    fileCards = data.split("\n") 
    for x in fileCards:
        xList = list(x)
        for y in xList:
            Library2.append(y)
    for x in TextList:
        for num, char in enumerate(x):
            if (num+1)%34 == 0:
                NewTestList.append("\n")
            

def GainLife1(LifeGainNo):
    global Life1
    Life1 += LifeGainNo

def GainLife2(LifeGainNo):
    global Life2
    Life2 += LifeGainNo

def Damage1(DamageNo):
    global Life1
    Life1 -= DamageNo

def Damage2(DamageNo):
    global Life2
    Life2 -= DamageNo

def Draw1():
    global Library1, Hand1
    card = random.choice(Library1)
    Library1.remove(card)
    Hand1.append(card)

def DrawField():
    #os.system("cls")
    global Hand1, Life1, Life2, Board1, Board2, Gray, Red, Green, Yellow, Blue, Purple, Cyan, End, ScreenSize
    print(f"{Green}{Life2:^198}")
    for x in Board2:
        print(f"{End}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ ",end="")
    print()
    for x in Board2:
        mvPos = Board2.index(x)
        ManaValue = MVList[mvPos]
        ManaValue = f"{ManaValue:>6}"
        MV: list[str] = []
        for y in ManaValue:
            if y == "W":
                MV.append(End)
            elif y == "U":
                MV.append(Blue)
            elif y == "B":
                MV.append(Gray)
            elif y == "R":
                MV.append(Red)
            elif y == "G":
                MV.append(Green)
            MV.append(y)
        MV.append(End)
        MV = "".join(MV)
        print(f"{End}┃ {x:<27} {MV} ┃ ",end="")
    print()
    for x in Board2:
        print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ",end="")
    print()
    #for x in Board2:
        #print(f"{End}┃ {CardText:<34} ┃ ",end="")
    #print()
    for x in Board2:
        print(f"{End}┃ {'':<34} ┃ ",end="")
    print()
    for x in Board2:
        print(f"{End}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ",end="")
    print()

Finished = False
if __name__ == '__main__':
    SetUp()
    while not Finished:
        time.sleep(1)
        DrawField()
        Finished = True