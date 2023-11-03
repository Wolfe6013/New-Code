import os

pi = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534'
while True:
    digitPos = 0
    bonus = 0
    wrongAmount = 0
    correctAmount = 0
    correctTotal = 0
    wrongTotal = 0
    skips = 0
    correctSequence = []
    playerInput = input('>')
    if playerInput == 'End':
        break
    if playerInput == 'Skip' or playerInput == '':
        os.system("cls")
    else:
        print('  ', end='')
        for x in playerInput:
            if x == pi[digitPos]:
                print(' ', end='')
                correctAmount += 1
                if wrongTotal == 0:
                    correctTotal += 1
            else:
                print(pi[digitPos], end='')
                wrongAmount += 1
                wrongTotal = 1
            correctSequence.append(pi[digitPos])
            digitPos += 1
        for x in range(10):
            print(pi[digitPos], end='')
            correctSequence.append(pi[digitPos])
            digitPos += 1
        print()
        for z in correctSequence:
            print(z, end='')
        print()
        if wrongAmount > 0:
            print("You got",wrongAmount,"incorrect and",correctAmount-2,"correct (with a score of",correctAmount-2-wrongAmount,"). \nYou got",correctTotal-2,"decimal places right in a row!")
        else: print("That is",correctTotal-2,"digits correct!")
        print()