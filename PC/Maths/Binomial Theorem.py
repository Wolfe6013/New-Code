def Numbers():
    a = int(input("What is variable 'a' "))
    b = int(input("What is variable 'b' "))
    n = int(input("What is 'n' "))
    Total = 0
    done = 1      ###Generates Pascals Triangle
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
    binomialdone = -1      ###(a+b)^n
    ae = n
    be = 0
    while binomialdone < n:
        ce = newlist[0]
        print(ce*((a**ae)*(b**be)), end=' ')
        Total += (ce*((a**ae)*(b**be)))
        binomialdone = binomialdone+1
        if binomialdone != n:
            print('+', end=' ')
        else:   print('=',end=' ')
        ae = ae-1
        be = be+1
        newlist.pop(0)
    print(Total)
        
def Variable():
    a = input("What is variable 'a' ")
    b = input("What is variable 'b' ")
    n = int(input("What is 'n' "))
    done = 1      ###Generates Pascals Triangle
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
    binomialdone = -1      ###(a+b)^n
    ae = n
    be = 0
    while binomialdone < n:
        if newlist[0] != 1:
            print(newlist[0], end=' ', sep = '')
        if ae > 0:
            print(a,'^',ae, end=' ', sep = '')
        if be > 0:
            print(b,'^',be, end=' ', sep = '')
        binomialdone = binomialdone+1
        if binomialdone != n:
            print('+', end=' ')
        ae = ae-1
        be = be+1
        newlist.pop(0)

def VariableNum():
    NumbersList = ['1','2','3','4','5','6','7','8','9']
    a = input("What is variable 'a' ")
    b = input("What is variable 'b' ")
    n = int(input("What is 'n' "))
    done = 1      ###Generates Pascals Triangle
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
    NumberOrVariableA = 0
    NumberOrVariableB = 0
    for x in a:
        if x in NumbersList: ...
        else: NumberOrVariableA = 1
    for x in b:
        if x in NumbersList: ...
        else: NumberOrVariableB = 1
    binomialdone = 0      ###(a+b)^n
    ae = n
    be = 0
    if a + b == 2:
        while binomialdone < n:
            if newlist[0] != 1:
                print(newlist[0], end=' ', sep = '')
            if ae > 0:
                print(a,'^',ae, end=' ', sep = '')
            if be > 0:
                print(b,'^',be, end=' ', sep = '')
            binomialdone = binomialdone+1
            if binomialdone != n:
                print('+', end=' ')
            ae = ae-1
            be = be+1
    if a == 0 and b == 1:
        while binomialdone < n:
            if ae > 0:
                print(newlist[0]*a**ae, end=' ')
            if be > 0:
                print(b,'^',be, end=' ', sep = '')
            binomialdone = binomialdone+1
            if binomialdone != n:
                print('+', end=' ')
            ae = ae-1
            be = be+1

def FunctionList():
    print(' \nThe functions are as follows:')
    Functions = ['Numbers()','Variable()','VariableNum()']
    for x in Functions: 
        print(x)
    print()
    WhichFunction = input()
    print()
    found = 0
    if WhichFunction == 'Numbers()' or WhichFunction == '1':
        found = 1
        Numbers()
    if WhichFunction == 'Variable()' or WhichFunction == '2':
        found = 1
        Variable()
    if WhichFunction == 'VariableNum()' or WhichFunction == '3':
        found = 1
        VariableNum()
    if found == 0:
        print('No function found with that specifications.')
    FunctionList()
FunctionList()