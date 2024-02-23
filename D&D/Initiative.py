import os, random, time, sys, pyautogui, keyboard, logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"
 
p1 = [0,0]
p2 = [0,0]
p3 = [0,0]
p4 = [0,0]
p5 = [0,0]
p6 = [0,0]
p7 = [0,0]
p8 = [0,0]
p9 = [0,0]
pList = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

name = "p1"
HP = 0
MaxHP = 0
Str = 0
Dex = 0
Con = 0
Int = 0
Wis = 0
Cha = 0

def clear():
    os.system("cls")

def draw():
    print(f"{End}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")

def save():
    f = open("Initiative.txt","w")
    for x in pList:
        if x != [0,0]:
            for item in x:
                f.write(str(item) + "\n")
    f.close()

def load():
    try:
        f = open("Initiative.txt","r")
        load_list = f.readlines()
        done = 0
        pos = 0
        while done != len(load_list):
            if (len(load_list) % 10) == 0:
                initiative = int(load_list[0+done][:-1])
                name = load_list[1+done][:-1]
                HP = int(load_list[2+done][:-1])
                MaxHP = int(load_list[3+done][:-1])
                Str = int(load_list[4+done][:-1])
                Dex = int(load_list[5+done][:-1])
                Con = int(load_list[6+done][:-1])
                Int = int(load_list[7+done][:-1])
                Wis = int(load_list[8+done][:-1])
                Cha = int(load_list[9+done][:-1])

                if pos < len(pList):
                    pList[pos] = initiative,name,HP,MaxHP,Str,Dex,Con,Int,Wis,Cha
                done += 10
                pos += 1
            else:
                logging.debug('CORRUPT SAVE FILE')
                done = len(load_list)
    except OSError:
        logging.debug("NO LOADABLE SAVE FILE")

load()
save()
Combat = True
combatPos = 0

while Combat:
    zeroNum = 0
    clear()
    draw()
    for x in pList:
        if x != [0,0]:
            print(f"│{Red}{x[1]}{End}'s Stats - HP: {Green}{x[2]}{End}/{Green}{x[3]}{End}, Str: {x[4]}, Dex: {x[5]}, Con: {x[6]}, Int: {x[7]}, Wis: {x[8]}, Cha: {x[9]}")
        elif x == [0,0]:
            zeroNum += 1
        
    for x in range(zeroNum):
        pList.remove([0,0])

    draw()
    initiativeOrder = pList
    initiativeOrder.sort(reverse = True)

    charPos = 1
    for x in initiativeOrder:
        print("│",end="")
        if x == initiativeOrder[combatPos]: print(Yellow,end="")
        print(f"{charPos} - {x[0]} - {x[1]} - HP: {x[2]}/{x[3]}{End}")
        charPos += 1
    draw()

    target = int(input("Target Pos: "))
    load()
    if target > 0 and target < len(initiativeOrder):
        damage = int(input("Damage Amount: "))
        targetHealth = initiativeOrder[target-1][2]
        logging.debug(target)
        logging.debug(type(initiativeOrder))
        for x in initiativeOrder:
            x = list(x)
        initiativeOrder[target-1] = list(initiativeOrder[target-1])
        logging.debug(type(initiativeOrder[target-1]))
        logging.debug(initiativeOrder[target-1])
        logging.debug(targetHealth)
        targetHealth -= damage
        initiativeOrder[target-1][2] = int(targetHealth)
        input()
        save()

    combatPos += 1
    if combatPos >= len(initiativeOrder):
        combatPos = 0