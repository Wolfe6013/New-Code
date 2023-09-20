pi = '14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534'
while True:
    digitPos = 0
    bonus = 0
    wrongAmount = 0
    correctAmount = 0
    correctTotal = 0
    wrongTotal = 0
    skips = 0
    correctSequence = ['3','.']
    playerInput = input('3.')
    if playerInput == 'End':
        break
    if playerInput == 'Skip' or playerInput == '':
        while skips < 12:
            print()
            skips += 1
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
        while bonus < 10:
            print(pi[digitPos], end='')
            correctSequence.append(pi[digitPos])
            digitPos += 1
            bonus += 1
        print()
        for z in correctSequence:
            print(z, end='')
        print()
        if wrongAmount > 0:
            print("You got",wrongAmount,"incorrect and",correctAmount,"correct (with a score of",correctAmount-wrongAmount,"). \nYou got",correctTotal,"decimal places right in a row!")
        else: print("That is",correctTotal,"digits correct!")
        print()