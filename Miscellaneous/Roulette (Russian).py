import random, time, os

fullRound = ["Blank","Blank","Blank","Fire","Fire","Fire"]
p1Wins = 0
p2Wins = 0
yn = True
currentRound = fullRound
p1Health = 2
p2Health = 2
p1Turn = True
p2Turn = False

while yn:
    os.system("cls")
    if p1Turn and p1Health > 0 and p2Health > 0 and len(currentRound) > 0:
        print(f"Your Go. Blanks: {currentRound.count('Blank')}, Rounds: {currentRound.count('Fire')}")
        p1Move = input(f"Shoot at 'Opponent' ({p2Health} HP) or 'Self' ({p1Health} HP)? ")
        action = random.choice(currentRound)
        if p1Move == "Opponent":
            if action == "Fire":
                p2Health -= 1
            p1Turn = False
            p2Turn = True
            currentRound.remove(action)
            print(action)
        elif p1Move == "Self":
            if action == "Fire":
                p1Health -= 1
            p1Turn = True
            p2Turn = False
            currentRound.remove(action)
            print(action)
        else:
            print("Invalid Command ('Opponent' or 'Self')")
        time.sleep(1)
    if p2Turn and p1Health > 0 and p2Health > 0 and len(currentRound) > 0:
        print(f"Opponent Go. Blanks: {currentRound.count('Blank')}, Rounds: {currentRound.count('Fire')}")
        print(f"Shoot at 'Opponent' ({p2Health} HP) or 'Self' ({p1Health} HP)? Opponent")
        action = random.choice(currentRound)
        currentRound.remove(action)
        print(action)
        if action == "Fire":
            p1Health -= 1
        p1Turn = True
        p2Turn = False
        time.sleep(3)

    if p1Health < 1:
        print("You Lost!")
        p2Wins += 1
    elif p2Health < 1:
        print("You Won!")
        p1Wins += 1
    
    if len(currentRound) == 0 or p1Health == 0 or p2Health == 0:
        currentRound = ["Blank","Blank","Blank","Fire","Fire","Fire"]
        p1Turn = True
        p2Turn = False
        if p1Health == 0 or p2Health == 0:
            print(f"You have {p1Wins} wins and {p2Wins} loses.")
            playAgain = input("Play Again (y/n)? ")
            if playAgain == "n" or playAgain == "N":
                yn = False
            else:
                p1Health = 2
                p2Health = 2