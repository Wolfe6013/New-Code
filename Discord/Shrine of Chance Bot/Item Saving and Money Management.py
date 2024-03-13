from random import choice, randint

playerList = []
nameList = []

def save():
    f = open("Gamble.txt","w")
    done = 0
    for player in playerList:
        f.write(f"{nameList[done]}:")
        for item in player:
            f.write(f"/{item}")
        done += 1
        f.write("/\n")
    f.close()

def load():
    try:
        f = open("Gamble.txt","r")
        load_list = f.readlines()
        done = 0
        while done != len(load_list):
            playerName = (load_list[done]).split(':')[0]
            items = (load_list[done]).split('/')[1:]
            done += 1
            items.pop(len(items)-1)
            items.sort()
            print(f"{playerName}: {items}")
            playerList.append(items)
            nameList.append(playerName)
    except OSError:
        print("NO LOADABLE SAVE FILE")

load()
save()