import os

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

def PascalsTriangleNS(n,q):
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
    print("1 1")
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
        for x in newlist:
            if x % q == 0:
                print(f"{Green}{x}{End} ",end="")
            else: print(f"{x} ",end="")
        print()
        newlist.append(0)
        pascalslist = newlist

while True:
    n = int(input())
    os.system("cls")
    PascalsTriangleNS(16,n)