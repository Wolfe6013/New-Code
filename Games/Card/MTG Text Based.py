import os, random, time, sys, pyautogui, keyboard

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

Isperia_Supreme_Judge = ["Isperia, Supreme Judge"]
Archon_of_Redemption = ["Archon of Redemption"]
Cartographers_Hawk = ["Cartographer's Hawk"]
Cleansing_Nova = ["Cleansing Nova"]
Emeria_Angel = ["Emeria Angel"]
Plains = ["Plains"]

full_deck = [Isperia_Supreme_Judge,Archon_of_Redemption,Cartographers_Hawk,Cleansing_Nova,Emeria_Angel,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains,Plains]
Library = []
Hand = []
Graveyard = []
Exile = []
Life1 = 40
Life2 = 40
Board1 = []
Board2 = []

for x in full_deck:
    Library.append(x)

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
    global Library, Hand
    card = random.choice(Library)
    Library.remove(card)
    Hand.append(card)

def DrawField():
    global Hand, Life1, Life2, Board1, Board2, Gray, Red, Green, Yellow, Blue, Purple, Cyan, End
    print(f"     {Green}{Life2}{End}\n\n")
    for x in Board2:
        print("/--------\ ",end="")
    print()
    for x in Board2:
        print("|        | ",end="")