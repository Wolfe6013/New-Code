import random, os, time

Bold = f"\033[1;37;40m"
Gray = f"\033[0;30;40m"
Red = f"\033[0;31;40m"
Green = f"\033[0;32;40m"
Yellow = f"\033[0;33;40m"
Blue = f"\033[0;34;40m"
Purple = f"\033[0;35;40m"
Cyan = f"\033[0;36;40m"
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
        if len(load_list) == 6:
            totalClicks: int = load_list[0][:-1]
            maxScore: int = load_list[1][:-1]
            totalResets: int = load_list[2][:-1]
            score: int = load_list[3][:-1]
            colour: str = load_list[4][:-1]
            circleButton: bool = load_list[5][:-1]
            scoresList: list = [totalClicks,maxScore,totalResets,score,colour,circleButton]
        else:
            print(f"│CORRUPT SAVE FILE!")
            input(f"│<")
    except OSError:
        print(f"│NO LOADABLE SAVE FILE!")
        input(f"│<")
    return scoresList
    
def buttonUp(scoreList):
    clear()
    Settings: str = f"Settings"
    print(f"{Bold}{Settings:^28}{colour}")
    scores(scoreList)
    print(f"╭──────────────────────────╮")
    print(f"│                          │")
    print(f"│{scoreList[3]:^26}│")
    print(f"│                          │")
    print(f"├──────────────────────────┤")
    print(f"╰──────────────────────────╯{End}")
    time.sleep(0.2)

def buttonDown(scoreList):
    clear()
    Settings: str = f"Settings"
    print(f"{Bold}{Settings:^28}{colour}")
    scores(scoreList)
    print(f"                            ")
    print(f"╭──────────────────────────╮")
    print(f"│                          │")
    print(f"│{scoreList[3]:^26}│")
    print(f"│                          │")
    print(f"╰──────────────────────────╯{End}")
    time.sleep(0.3)

def circleButtonUp(scoreList):
    clear()
    Settings: str = f"Settings"
    print(f"{Bold}{Settings:^28}{colour}")
    scores(scoreList)
    print(f"         .────────.         ")
    print(f"      .─/          \─.      ")
    print(f"     /                \     ")
    print(f"    /                  \    ")
    print(f"    │{scoreList[3]:^18}│    ")
    print(f"    \                  /    ")
    print(f"     \                /     ")
    print(f"     \*─\          /─*/     ")
    print(f"      *─\*────────*/─*      ")
    print(f"         *────────*         {End}")
    time.sleep(0.2)

def circleButtonDown(scoreList):
    clear()
    Settings: str = f"Settings"
    print(f"{Bold}{Settings:^28}{colour}")
    scores(scoreList)
    print(f"                            ")
    print(f"         .────────.         ")
    print(f"      .─/          \─.      ")
    print(f"     /                \     ")
    print(f"    /                  \    ")
    print(f"    │{scoreList[3]:^18}│    ")
    print(f"    \                  /    ")
    print(f"     \                /     ")
    print(f"      *─\          /─*      ")
    print(f"         *────────*         {End}")
    time.sleep(0.3)

def scores(scoreList):
    maxScore: int = scoreList[1]
    totalClicks: int = scoreList[0]
    totalResets: int = scoreList[2]
    score1: str = f"Max Score: {maxScore}"
    score2: str = f"Total Clicks: {totalClicks}"
    score3: str = f"Total Resets: {totalResets}"
    print(f"{score1:^28}")
    print(f"{score2:^28}")
    print(f"{score3:^28}")

def Settings(colour):
    done = False
    newColour = colour
    while not done:
        clear()
        if loadList[5] == "True":
            print(f"{newColour}Button Settings: ◉")
        else:
            print(f"{newColour}Button Settings: ▣")
        print(f"{End}-----------------")
        print(f"{End}1. White")
        print(f"{Gray}2. Gray")
        print(f"{Red}3. Red")
        print(f"{Green}4. Green")
        print(f"{Yellow}5. Yellow")
        print(f"{Blue}6. Blue")
        print(f"{Purple}7. Purple")
        print(f"{Cyan}8. Cyan{End}")
        print(f"{End}9{Gray}. {Red}R{Green}a{Yellow}n{Blue}d{Purple}o{Cyan}m{End}")
        print("-----------------")
        print(f"A. Round Button")
        print(f"B. Square Button")
        print("-----------------")
        print(f"0. Leave Settings")
        userInput: str = input(f"{newColour}>")
        if userInput == "1" or userInput == "White":
            newColour = End
        elif userInput == "2" or userInput == "Gray":
            newColour = Gray
        elif userInput == "3" or userInput == "Red":
            newColour = Red
        elif userInput == "4" or userInput == "Green":
            newColour = Green
        elif userInput == "5" or userInput == "Yellow":
            newColour = Yellow
        elif userInput == "6" or userInput == "Blue":
            newColour = Blue
        elif userInput == "7" or userInput == "Purple":
            newColour = Purple
        elif userInput == "8" or userInput == "Cyan":
            newColour = Cyan
        elif userInput == "9" or userInput == "Random":
            newColour = "Random"
        elif userInput == "A" or userInput == "Square":
            loadList[5] = "True"
        elif userInput == "B" or userInput == "Round":
            loadList[5] = "False"
        elif userInput == "0" or userInput == "Leave" or userInput == "Leave Settings" or userInput == "Exit":
            done = True
    return [newColour,loadList[5]]

if __name__ == "__main__":
    score: int = 0
    randomColour = False
    while True:
        loadList: list = load()
        colour: str = loadList[4]
        #maxScore: int = loadList[1]
        #totalClicks: int = loadList[0]
        #totalResets: int = loadList[2]
        Random = random.choice([End,Gray,Red,Green,Yellow,Blue,Purple,Cyan])
        if colour == "Random":
            randomColour = True
            colour = Random
        else:
            randomColour = False
        if loadList[5] == "True":
            circleButtonUp(loadList)
        else:
            buttonUp(loadList)
        userInput: str = input()
        if userInput == "":
            if loadList[5] == "True":
                circleButtonDown(loadList)
            else:
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
        elif userInput == "Settings":
            settingsResults = Settings(colour)
            input()
            colour = settingsResults[0]
            loadList[4] = colour
            loadList[5] = settingsResults[1]
            save(loadList)
        else:
            print("Unknown Command!")
            time.sleep(1)
        if randomColour:
            colour = "Random"