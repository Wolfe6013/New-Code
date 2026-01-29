import random, os, time, sys

def Calculate(Sum,Boxes):
    possibleValues = []
    integerList = [1,2,3,4,5,6,7,8,9]
    elipsedList = integerList
    minTotal = 0
    maxTotal = 0
    elipsed = 0
    while elipsed < Boxes:
        minTotal += integerList[elipsed]
        elipsed += 1
        maxTotal += integerList[-elipsed]
    if minTotal > Sum or maxTotal < Sum:
        return f"'No Possible Values' for {Sum} across {Boxes} boxes.\nSum range is {minTotal} to {maxTotal}."
    if minTotal == Sum:
        possibleValues.append(minTotal)
    done = False
    while not done:
        total = 0
        tested = []
        for x in range(Boxes-1):
            for y in range(9-Boxes):
                total+=elipsedList[x+y]
                tested.append(elipsedList[x+y])
            

while __name__ == "__main__":
    os.system("cls")
    Sum, Boxes = input("Sum/Boxes: ").split("/")
    Sum = int(Sum)
    Boxes = int(Boxes)
    if Boxes > 9:
        Boxes = 9
    if Boxes < 1:
        Boxes = 1
    print(Calculate(Sum,Boxes))
    input()