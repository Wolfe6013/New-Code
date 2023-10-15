import random

def MakeSeed():
    done = 0
    boxChoices = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','1','2','3','4','5','6','7','8','9']

    while True:
        allNumbers = 0
        finalSeed = []
        for x in range(81):
            finalSeed.append(random.choice(boxChoices))
        for x in boxChoices:
            if x in finalSeed:
                allNumbers += 1
        if allNumbers == len(boxChoices):
            break

    for x in finalSeed:
        print(x, end='')

while True:
    MakeSeed()
    input()