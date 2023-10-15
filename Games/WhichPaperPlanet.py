import random

def allRandom():
    sugarsList = ['Honey','More','Paperjam','Shyness','The Underdog']
    spicesList = ['Zoomies','Scavengers','Dakka','Swarms','Champions']
    planetList = ['Plane Planet','Pyro Planet','Square Planet','Prairie Planet']
    #planetList.append('Paper Planet')
    whichPlanet = random.choice(planetList)
    print(f'The planet you are playing is the {whichPlanet}')

    difficultyNum = 4

    totalDifficultyMods = random.randint(0,3)
    totalDifficultyMods += 2

    sugarNum = random.randint(0, totalDifficultyMods)

    spiceNum = totalDifficultyMods - sugarNum

    if sugarNum < 0:
        sugarNum = 0
    if spiceNum < 0:
        spiceNum = 0

    print(f'The diffulty mods you are using is {sugarNum} sugar(s) and {spiceNum} spice(s)')
    while sugarNum > 0:
        randomSugar = random.randint(0, difficultyNum)
        if sugarsList[randomSugar] == 'Honey':
            sugarLevel = random.randint(1,4)
        if sugarsList[randomSugar] == 'More':
            sugarLevel = random.randint(1,2)
        if sugarsList[randomSugar] == 'Paperjam':
            sugarLevel = random.randint(1,4)
        if sugarsList[randomSugar] == 'Shyness':
            sugarLevel = random.randint(1,4)
        if sugarsList[randomSugar] == 'The Underdog':
            sugarLevel = random.randint(1,3)
        print(f'Use Sugar of {sugarsList[randomSugar]} with a level of {sugarLevel}')
        sugarsList.remove(sugarsList[randomSugar])
        spicesList.remove(spicesList[randomSugar])
        difficultyNum -= 1
        sugarNum -= 1

    while spiceNum > 0:
        randomSpice = random.randint(0, difficultyNum)
        if spicesList[randomSpice] == 'Zoomies':
            spicesLevel = random.randint(1,4)
        if spicesList[randomSpice] == 'Scavengers':
            spicesLevel = random.randint(1,3)
        if spicesList[randomSpice] == 'Dakka':
            spicesLevel = random.randint(1,3)
        if spicesList[randomSpice] == 'Swarms':
            spicesLevel = random.randint(1,4)
        if spicesList[randomSpice] == 'Champions':
            spicesLevel = random.randint(1,3)
        print(f'Use Spice of {spicesList[randomSpice]} with a level of {spicesLevel}')
        sugarsList.remove(sugarsList[randomSpice])
        spicesList.remove(spicesList[randomSpice])
        difficultyNum -= 1
        spiceNum -= 1

    seedNum = 0
    seed = []

    while seedNum < 9:
        seedNum += 1
        seed.append(random.randint(0,9))

    print('The seed you will use is: ', end = '')
    e = ['','-']
    print(random.choice(e), end = '')
    for x in seed:
        print(x, end = '')
    print()
allRandom()

while True:
    break
    whatCheck = input('Random what? ')
    if whatCheck == 'Shop':
        print(random.randint(1, 6),random.randint(1, 5),random.randint(1, 4),random.randint(1, 3),random.randint(1, 2),random.randint(1, 1))
    if whatCheck == 'End':
        break
    if whatCheck != 'Shop' and whatCheck != '':
        print(random.randint(1, int(whatCheck)))

while True:
    #break
    input()
    allRandom()