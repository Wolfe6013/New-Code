import random, os, time

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

def clear():
    os.system("cls")

def save(saveList):
    f = open("TheButton.txt","w")
    for x in saveList:
        f.write(f"{x}\n")
    f.close()

def load():
    try:
        f = open("TheButton.txt","r")
        load_list = f.readlines()
        if len(load_list) == 4:
            totalClicks: int = load_list[0][:-1]
            maxScore: int = load_list[1][:-1]
            totalResets: int = load_list[2][:-1]
            score: int = load_list[3][:-1]
            scoresList: list = [totalClicks,maxScore,totalResets,score]
        else:
            print(f"│CORRUPT SAVE FILE!")
            input(f"│<")
    except OSError:
        print(f"│NO LOADABLE SAVE FILE!")
        input(f"│<")
    print(scoresList)
    return scoresList
    
def buttonUp(scoreList):
    clear()
    print(colour)
    scores(scoreList)
    print(f"╭────────────────────╮")
    print(f"│                    │")
    print(f"│{scoreList[3]:^20}│")
    print(f"│                    │")
    print(f"├────────────────────┤")
    print(f"╰────────────────────╯")

def buttonDown(scoreList):
    clear()
    print(f"{colour}")
    scores(scoreList)
    print(f"                      ")
    print(f"╭────────────────────╮")
    print(f"│                    │")
    print(f"│{scoreList[3]:^20}│")
    print(f"│                    │")
    print(f"╰────────────────────╯")
    time.sleep(0.5)

def scores(scoreList):
    maxScore: int = scoreList[1]
    totalClicks: int = scoreList[0]
    totalResets: int = scoreList[2]
    score1: str = f"Max Score: {maxScore}"
    score2: str = f"Total Clicks: {totalClicks}"
    score3: str = f"Total Resets: {totalResets}"
    print(f"{score1:^22}")
    print(f"{score2:^22}")
    print(f"{score3:^22}")

if __name__ == "__main__":
    score: int = 0
    colour = Green
    while True:
        loadList: list[int] = load()
        #maxScore: int = loadList[1]
        #totalClicks: int = loadList[0]
        #totalResets: int = loadList[2]
        buttonUp(loadList)
        input()
        buttonDown(loadList)
        resetChance: int = random.randint(1,100)
        loadList[0] = int(loadList[0]) + 1
        if resetChance > int(loadList[3]):
            loadList[3] = int(loadList[3]) + 1
            if loadList[3] > int(loadList[1]):
                loadList[1] = int(loadList[3])
        else:
            loadList[3] = 0
            loadList[2] = int(loadList[2]) + 1
        save(loadList)