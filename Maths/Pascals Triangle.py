def PascalsTriangle(n):
    done = 0
    linesdone = 1
    spacesdone = 0
    newlistdone = 0
    pascalslist = [1,1]
    print('1', end=' ')
    while (n-linesdone) > spacesdone:
        print('', end=' ')
        spacesdone = spacesdone+1
    if n > 9:
        if linesdone < 10:
            print('', end=' ')
    if n > 99:
        if linesdone < 100:
            print('', end=' ')
    print(pascalslist)
    pascalslist.append(0)
    while linesdone < n:
        newlistdone = 0
        spacesdone = 0
        newlist = [1]
        done = 0
        linesdone = linesdone+1
        while newlistdone == 0:
            topleft = pascalslist[done]
            topright = pascalslist[done+1]
            newnumber = topleft+topright
            newlist.append(newnumber)
            if topright == 0:
                newlistdone = 1
            done = done+1
        print(linesdone, end=' ')
        while (n-linesdone) > spacesdone:
            print('', end=' ')
            spacesdone = spacesdone+1
        if n > 9:
            if linesdone < 10:
                print('', end=' ')
        if n > 99:
            if linesdone < 100:
                print('', end=' ')
        print(newlist)
        newlist.append(0)
        pascalslist = newlist
        
def PascalsTriangleNS(n):
    done = 0
    linesdone = 1
    newlistdone = 0
    pascalslist = [1,1]
    print('1 -', end=' ')
    print(pascalslist)
    pascalslist.append(0)
    while linesdone < n:
        newlistdone = 0
        newlist = [1]
        done = 0
        linesdone = linesdone+1
        while newlistdone == 0:
            topleft = pascalslist[done]
            topright = pascalslist[done+1]
            newnumber = topleft+topright
            newlist.append(newnumber)
            if topright == 0:
                newlistdone = 1
            done = done+1
        print(linesdone,'-', end=' ')
        print(newlist)
        newlist.append(0)
        pascalslist = newlist
        
def PascalsTriangleOLL(n):
    done = 1
    linesdone = 1
    newlistdone = 0
    pascalslist = [1,1,0]
    while linesdone < n:
        newlistdone = 0
        newlist = [1]
        done = 0
        linesdone = linesdone+1
        while newlistdone == 0:
            topleft = pascalslist[done]
            topright = pascalslist[done+1]
            newnumber = topleft+topright
            newlist.append(newnumber)
            if topright == 0:
                newlistdone = 1
            done = done+1
        newlist.append(0)
        pascalslist = newlist
    print(newlist)

def PascalsTriangleQOLL(n):
    done = 0
    pascalslist = [1]
    divide = 1
    multiply = n
    number = 1
    while n > done:
        number = number*multiply/divide
        pascalslist.append(int(number))
        multiply = multiply-1
        divide = divide+1
        done = done+1
    print(pascalslist)

print('The functions are as follows:')
Functions = ['PascalsTriangle()','PascalsTriangleNS()','PascalsTriangleOLL()','PascalsTriangleQOLL()']
for x in Functions:
    print(x)
while True:
    print()
    WhichFunction = input()
    print()
    found = 0
    NumberOfLetters = 0
    WhichFunctionList = []
    for x in WhichFunction:
        NumberOfLetters += 1
        WhichFunctionList.append(x)
    n = WhichFunctionList[NumberOfLetters-2]
    WhichFunctionList.pop(n)
    WhichFunction = ""
    for i in WhichFunctionList:
        WhichFunction += i +''
    if WhichFunction == 'PascalsTriangle()':
        PascalsTriangle(n)
        found += 1
    if WhichFunction == 'PascalsTriangleNS()':
        PascalsTriangleNS(n)
        found += 1
    if WhichFunction == 'PascalsTriangleOLL()':
        PascalsTriangleOLL(n)
        found += 1
    if WhichFunction == 'PascalsTriangleQOLL()':
        PascalsTriangleQOLL(n)
        found += 1
    if found == 0:
        print('No function found with that specifications.')