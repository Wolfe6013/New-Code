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
P1Name: str = input("What is P1's name? ")
P2Name: str = input("What is P2's name? ")

while yn:
    if p1Turn and p1Health > 0 and p2Health > 0 and len(currentRound) > 0:
        os.system("cls")
        print(f"{P1Name}'s go. Blanks: {currentRound.count('Blank')}, Rounds: {currentRound.count('Fire')}")
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
            print(f"Invalid Command ('Opponent' or 'Self')")
        time.sleep(1)
    if p2Turn and p1Health > 0 and p2Health > 0 and len(currentRound) > 0:
        os.system("cls")
        print(f"{P2Name}'s go. Blanks: {currentRound.count('Blank')}, Rounds: {currentRound.count('Fire')}")
        p1Move = input(f"Shoot at 'Opponent' ({p1Health} HP) or 'Self' ({p2Health} HP)? ")
        action = random.choice(currentRound)
        if p1Move == "Opponent":
            if action == "Fire":
                p1Health -= 1
            p2Turn = False
            p1Turn = True
            currentRound.remove(action)
            print(action)
        elif p1Move == "Self":
            if action == "Fire":
                p2Health -= 1
            p2Turn = True
            p1Turn = False
            currentRound.remove(action)
            print(action)
        else:
            print(f"Invalid Command ('Opponent' or 'Self')")
        time.sleep(1)

    if p1Health < 1:
        os.system("cls")
        print(f"{P2Name} Won!")
        p2Wins += 1
    elif p2Health < 1:
        os.system("cls")
        print(f"{P1Name} Won!")
        p1Wins += 1
    
    if len(currentRound) == 0 or p1Health == 0 or p2Health == 0:
        currentRound = ["Blank","Blank","Blank","Fire","Fire","Fire"]
        p1Turn = True
        p2Turn = False
        if p1Health == 0 or p2Health == 0:
            print(f"{P1Name} has {p1Wins} wins and {P2Name} has {p2Wins} wins.")
            playAgain = input("Play Again (y/n)? ")
            if playAgain == "n" or playAgain == "N":
                yn = False
            else:
                p1Health = 2
                p2Health = 2