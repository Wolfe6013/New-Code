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
Board2 = ["Archelos, Lagoon Mystic","Isperia, Bird Bitch"]
MVList = [f"{End}1{Gray}B{Green}G{Blue}U{End}",f"{End}4{Blue}U{End}"]
TextList = ["If ~ is untapped, all permanants ETB untapped. If ~ is tapped, all permanants ETB tapped.","When a creature attacks you or a planeswalker you control, draw a card."]

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
        print(f"{End}┃ {x:<29} {ManaValue:>6} ┃ ",end="")
    print()
    for x in Board2:
        print(f"┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫ ",end="")
    print()
    for x in Board2:
        mvPos = Board2.index(x)
        CardText = TextList[mvPos]
        if len(CardText) > 32:
            CardText = CardText[:32]
        print(f"{End}┃ {CardText:<34} ┃ ",end="")
    print()
    for x in Board2:
        mvPos = Board2.index(x)
        CardText = TextList[mvPos]
        if len(CardText) > 32:
            CardText2 = CardText[32:]
            CardText = CardText[:10]
        else:
            CardText2 = ""
        if len(CardText2) > 32:
            CardText2 = CardText2[:32]
        print(f"{End}┃ {CardText2:<34} ┃ ",end="")
    print()
    for x in Board2:
        mvPos = Board2.index(x)
        CardText = TextList[mvPos]
        if len(CardText) > 32:
            CardText2 = CardText[32:]
            CardText = CardText[:32]
        else:
            CardText2 = ""
        if len(CardText2) > 32:
            CardText3 = CardText2[32:]
            CardText2 = CardText2[:32]
        else:
            CardText3 = ""
        print(f"{End}┃ {CardText3:<34} ┃ ",end="")
    print()
    for x in Board2:
        mvPos = Board2.index(x)
        CardText = TextList[mvPos]
        try:
            if len(CardText) > 32:
                if CardText[33] == " ":
                    CardText2 = CardText[33:]
                    CardText = CardText[:33]
                else:
                    CardText2 = CardText[32:]
                    CardText = CardText[:32]
            else:
                CardText2 = ""
            if len(CardText2) > 32:
                if CardText[33] == " ":
                    CardText2 = CardText2[33:]
                    CardText3 = CardText3[:33]
                else:
                    CardText2 = CardText2[32:]
                    CardText3 = CardText3[:32]
            else:
                CardText3 = ""
            if len(CardText3) > 32:
                if CardText[33] == " ":
                    CardText3 = CardText3[33:]
                    CardText4 = CardText4[:33]
                else:
                    CardText3 = CardText3[32:]
                    CardText4 = CardText4[:32]
            else:
                CardText4 = ""
            print(f"{End}┃ {CardText4:<34} ┃ ",end="")
        except:
            ...
        print(f"{End}┃ {'':<34} ┃ ",end="")
    print()
    for x in Board2:
        print(f"{End}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ ",end="")
    print()

Finished = False
if __name__ == '__main__':
    while not Finished:
        time.sleep(1)
        DrawField()
        Finished = True