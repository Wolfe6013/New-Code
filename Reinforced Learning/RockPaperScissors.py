import random, time, os, sys

playerList = []
computerOptions = ["r","p","s"]
rPlays = 0
pPlays = 0
sPlays = 0
wins: int = 0 #for computer
loses: int = 0 #for computer

def RunRound(computerInput):
    global wins, loses, rPlays, pPlays, sPlays
    playerInput = input("r, p, s - ")
    playerList.append(playerInput)
    if playerInput == "r":
        rPlays += 1
        if computerInput == "p":
            print(f"{computerInput} beats {playerInput}. Computer wins!")
            wins += 1
        elif playerInput == computerInput: print(f"Both played {playerInput}! Tie!")
        else:
            print(f"{playerInput} beats {computerInput}. Player wins!")
            loses += 1
        
    elif playerInput == "p":
        pPlays += 1
        if computerInput == "s":
            print(f"{computerInput} beats {playerInput}. Computer wins!")
            wins += 1
        elif playerInput == computerInput: print(f"Both played {playerInput}! Tie!")
        else:
            print(f"{playerInput} beats {computerInput}. Player wins!")
            loses += 1
    elif playerInput == "s":
        sPlays += 1
        if computerInput == "r":
            print(f"{computerInput} beats {playerInput}. Computer wins!")
            wins += 1
        elif playerInput == computerInput: print(f"Both played {playerInput}! Tie!")
        else:
            print(f"{playerInput} beats {computerInput}. Player wins!")
            loses += 1

def FindInput():
    checkList: list = []
    if len(playerList) > 0:
        checkList.append(playerList[-1-len(checkList)])
    largestFound = False
    moveFound = False
    pOptions = [rPlays,pPlays,sPlays]
    if len(playerList) < 6:
        moveFound = True
        move = random.choice(computerOptions)
        print(playerList)
        print(pOptions)
    elif len(playerList) > 2:
        while not largestFound:
            if checkList in playerList:
                checkList.append(playerList[-1-len(checkList)])
                print(checkList)
                print(playerList)
            else:
                largestFound = True
        if len(checkList) > 2:
            for x, y in playerList:
                if x > len(playerList)-len(checkList):
                    if checkList[0] == y:
                        if checkList[1] == playerList[x+1]:
                            for a, b in checkList:
                                score = 1
                                if checkList[a] == playerList[x+a]:
                                    score += 1
                            if score >= len(checkList):
                                moveFound = True
                                move = playerList[x+len(checkList)+1]
        if moveFound == False:
            if max(pOptions) == rPlays: move = "p"
            elif max(pOptions) == pPlays: move = "s"
            elif max(pOptions) == sPlays: move = "r"
            else: move = random.choice(computerOptions)
    return move

if __name__ == "__main__":
    playNum: int = input("Games to play: ")
    for x, y in enumerate(range(int(playNum))):
        RunRound(FindInput())

    print(f"{wins} wins and {loses} loses over {playNum} games ({int(playNum)-int(wins)-int(loses)} ties).")
    print(f"{round(int(wins)*100/int(playNum),2)}% win rate (for computer).")