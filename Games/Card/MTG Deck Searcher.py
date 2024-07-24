import os, time

path = r'C:\Users\210108\Downloads\Archelos, Lagoon Mystic MTG Decks'

folder = []
cardList = []
fileNum: int = 0
for file in os.listdir(path):
    if file.endswith('.txt'):
        folder.append(file)
        fileNum += 1
for x in folder:
    file1 = open(f"C:\\Users\\210108\\Downloads\\Archelos, Lagoon Mystic MTG Decks\\{x}")
    data = file1.read()
    fileCards = data.split("\n") 
    for x in fileCards:
        xList = list(x)
        end = False
        appendList: list[str] = []
        for y in xList:
            if y == "(":
                end = True
                appendList.pop(-1)
            elif not end:
                appendList.append(y)
        x: str = "".join(appendList) 
        if "1x " in x:
            x = x[3:]
        elif "1 " in x:
            x = x[2:]
        elif "2x " in x:
            x = x[3:]
        elif "2 " in x:
            x = x[2:]
        elif "3x " in x:
            x = x[3:]
        elif "3 " in x:
            x = x[2:]
        elif "4x " in x:
            x = x[3:]
        elif "4 " in x:
            x = x[2:]
        elif "5x " in x:
            x = x[3:]
        elif "5 " in x:
            x = x[2:]
        elif "6x " in x:
            x = x[3:]
        elif "6 " in x:
            x = x[2:]
        elif "7x " in x:
            x = x[3:]
        elif "7 " in x:
            x = x[2:]
        elif "8x " in x:
            x = x[3:]
        elif "8 " in x:
            x = x[2:]
        elif "9x " in x:
            x = x[3:]
        elif "9 " in x:
            x = x[2:]
        elif "10x " in x:
            x = x[4:]
        elif "10 " in x:
            x = x[3:]
        elif "11x " in x:
            x = x[4:]
        elif "11 " in x:
            x = x[3:]
        elif "12x " in x:
            x = x[4:]
        elif "12 " in x:
            x = x[3:]
        elif "13x " in x:
            x = x[4:]
        elif "13 " in x:
            x = x[3:]
        elif "14x " in x:
            x = x[4:]
        elif "14 " in x:
            x = x[3:]
        elif "15x " in x:
            x = x[4:]
        elif "15 " in x:
            x = x[3:]
        elif "16x " in x:
            x = x[4:]
        elif "16 " in x:
            x = x[3:]
        elif "17x " in x:
            x = x[4:]
        elif "17 " in x:
            x = x[3:]
        elif "18x " in x:
            x = x[4:]
        elif "18 " in x:
            x = x[3:]
        elif "19x " in x:
            x = x[4:]
        elif "19 " in x:
            x = x[3:]

        if " Plains" in x:
            x = x[7:]
        elif " Swamp" in x:
            x = x[6:]
        elif " Island" in x:
            x = x[7:]
        elif " Mountain" in x:
            x = x[9:]
        elif " Forest" in x:
            x = x[7:]
        elif " Wastes" in x:
            x = x[7:]

        if x in cardList:
            print("in cardList")
            pos = cardList.index(x)
            cardList[pos+1] += 1
        else:
            print("Not in cardList")
            cardList.append(x)
            cardList.append(int(1))
    file1.close()

for x in range(len(cardList)):
    if x % 2 == 0:
        print(f"{(cardList[x+1])/fileNum*100} - '{cardList[x]}'")

oneCopy: list[str] = []
twoCopy: list[str] = []
threeCopy: list[str] = []
fourCopy: list[str] = []
fiveCopy: list[str] = []
sixCopy: list[str] = []
sevenCopy: list[str] = []
eightCopy: list[str] = []
nineCopy: list[str] = []
tenPlusCopy: list[str] = []
tenPlusNums: list[int] = []

for x in range(len(cardList)):
    if x % 2 == 1:
        if cardList[x] == 1:
            oneCopy.append(cardList[x-1])
        if cardList[x] == 2:
            twoCopy.append(cardList[x-1])
        if cardList[x] == 3:
            threeCopy.append(cardList[x-1])
        if cardList[x] == 4:
            fourCopy.append(cardList[x-1])
        if cardList[x] == 5:
            fiveCopy.append(cardList[x-1])
        if cardList[x] == 6:
            sixCopy.append(cardList[x-1])
        if cardList[x] == 7:
            sevenCopy.append(cardList[x-1])
        if cardList[x] == 8:
            eightCopy.append(cardList[x-1])
        if cardList[x] == 9:
            nineCopy.append(cardList[x-1])
        if cardList[x] >= 10:
            tenPlusCopy.append(cardList[x-1])
            tenPlusNums.append(cardList[x])

oneCopy.sort()
twoCopy.sort()
threeCopy.sort()
fourCopy.sort()
fiveCopy.sort()
sixCopy.sort()
sevenCopy.sort()
eightCopy.sort()
nineCopy.sort()
tenPlusNums, tenPlusCopy = (list(t) for t in zip(*sorted(zip(tenPlusNums, tenPlusCopy))))

fullList: list[list[str]] = [oneCopy,twoCopy,threeCopy,fourCopy,fiveCopy,sixCopy,sevenCopy,eightCopy,nineCopy,tenPlusCopy]
finalList: list[str] = []
file2 = open(f"C:\\Users\\210108\\Downloads\\Archelos, Lagoon Mystic MTG Decks\\Final List\\Final List","w")
for list in fullList:
    for card in list:
        if fullList.index(list) != 9: finalList.append(f"{round((fullList.index(list)+1)/fileNum*100,1)}% - {card}\n")
        else: finalList.append(f"{round((tenPlusNums[list.index(card)])/fileNum*100,1)}% - {card}\n")
finalList.reverse()
finalList.pop(0)
for x in finalList:
    file2.write(x)
file2.close()