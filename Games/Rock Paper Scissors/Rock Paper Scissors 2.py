import random, time, sys, os
from ConcurrentValues import FindReccursion

playerList: list[int] = []
winWith: list[int] = []
startPoint: int = 30
loseStreak = 0
validInputs = [0,1,2]
playing = True

def ComputerInput():
    if len(winWith) >= startPoint and loseStreak < 10:
        recent = [playerList[-1],playerList[-2],playerList[-3],playerList[-4],playerList[-5]]
        matchList = FindReccursion(recent,playerList)
        output = matchList[-1]
        output -= 1
        if output == -1:
            output = 2
    if len(winWith) >= startPoint and loseStreak < 20:
        output = random.choice(winWith)
    elif len(playerList) >= startPoint and loseStreak < 30:
        output = random.choice(playerList)
    else:
        output = random.randint(0,2)
    return output

def ThrowPrint(a,b):
    ab: list[int] = [a,b]
    output: list[int] = []
    for x in ab:
        if x == 0:
            output.append("Rock")
        elif x == 1:
            output.append("Paper")
        elif x == 2:
            output.append("Scissors")
    return list(output)

def WinCalculator(a,b):
    if a+1 == b or a-2 == b:
        player: int = 2
    elif b+1 == a or b-2 == a:
        player: int = 1
    else:
        player: int = 0
    return player

while playing:
    os.system('cls')
    playerInput = 3
    while playerInput not in validInputs:
        try:
            playerInput: int = int(input("Rock, Paper, Scissors! (1,2,3) "))
            playerInput -= 1
        except:
            print("Invalid input")
    compInput: int = ComputerInput()
    throw: list[int] = ThrowPrint(playerInput,compInput)
    print(f"You played {throw[0]} and the computer played {throw[1]}")
    winner = WinCalculator(playerInput,compInput)

    if winner == 1:
        print("You win!")
        loseStreak += 1
    elif winner == 2:
        print("You lost...")
        winWith.append(compInput)
        loseStreak -= 1.5
    else:
        print("It was a tie.")
        loseStreak += 0.5

    if playerInput == 2:
        playerInput: int = -1
    playerList.append((playerInput+1))
    print(f"{len(winWith)/len(playerList)*100}% computer wins ({loseStreak})\n{len(playerList)} matches played\n{playerList}")
    input()