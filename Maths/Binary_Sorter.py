import os, time, random, math

def BinarySort(unsortedList):
    returnList: list[int] = []
    splitNum: list[int] = []
    runNo: int = 0
    holdCell: list[list] = []
    holdCell.append(unsortedList)
    while True:
        splitList: list[list[int]] = [[],[]]
        mean: int = round((sum(holdCell[0]))/(len(holdCell[0])),3)
        if len(set(holdCell[0])) > 1:
            for x in holdCell[0]:
                if x >= mean:
                    splitList[1].append(x)
                else:
                    splitList[0].append(x)
            holdCell.pop(0)
            holdCell.append(splitList[0])
            holdCell.append(splitList[1])

        else:
            holdCell.append(holdCell[0])
            holdCell.pop(0)
        runNo += 1
        if math.log2(runNo) % 1 == 0 and int(math.log2(runNo)) not in splitNum:
            splitNum.append(math.log2(runNo))
            sortedNum = 0
            runNo = 0
            for x in holdCell:
                if len(set(x)) <= 1:
                    sortedNum += 1
            if sortedNum == len(holdCell):
                for list1 in holdCell:
                    for var in list1:
                        returnList.append(var)
                return returnList

def RandomFloat(listLength):
    list1 = []
    while len(list1) < listLength:
        list1.append(random.randint(1,13))
    return list1

def RandomInt(listLength):
    list1: list[int] = []
    options = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    while len(list1) < listLength:
        list1.append(random.choice(options))
    return list1

if __name__ == "__main__":
    start = time.time()

    listLength = 10
    #sortFile = [4,9,2,2,3,0,4,1,6,5]
    sortFile = RandomFloat(listLength)
    #sortFile: list = RandomInt(listLength)

    sortedList = BinarySort(sortFile)

    os.system("cls")
    print(f"Raw list:    {sortFile}")
    print(f"Sorted list: {sortedList}")

    end = time.time()
    print(f"Final run time: {(end - start)*1000}ms")