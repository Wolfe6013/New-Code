#credit to https://germanna.edu/sites/default/files/2022-03/Change%20of%20Number%20Bases.pdf for the conversion maths
import math, os

while True:
    os.system("cls")
    ogNo = input("Number That Needs Converting: ")
    base1 = int(input("Original Base: "))
    base2 = int(input("New Base: "))

    numbers = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    base10Numbers = ["0","1","2","3","4","5","6","7","8","9"]
    subscript = ['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']

    if base1 == 10:
        during = int(ogNo)
        number = []
        number = list(number)

        while during >= 1:
            remainder = during % base2
            during = math.floor(during/base2)
            remainder = numbers[remainder]
            number.insert(0,remainder)

    else:
        powerOf = len(str(ogNo))-1
        NoList = list(str(ogNo))
        NoPos = 0
        number = 0

        while powerOf > -1:
            if NoList[0] not in base10Numbers:
                addNum = numbers.index(NoList[0])
            else:
                addNum = int(NoList[0])
            NoList.pop(0)
            number += int(addNum)*(base1**powerOf)
            powerOf -= 1

        if base2 != 10:
            during = int(number)
            number = []
            number = list(number)

            while during >= 1:
                remainder = during % base2
                during = math.floor(during/base2)
                remainder = numbers[remainder]
                number.insert(0,remainder)

        else: number = list(str(number))

    print(f"{ogNo}",end="")
    for x in list(str(base1)):
        print(f"{subscript[int(x)]}",end="")
    print(f" in Base {base2} is ",end='')
    for x in number:
        print(x,end="")
    for x in list(str(base2)):
        print(f"{subscript[int(x)]}",end="")
    print(".",end="")
    input()