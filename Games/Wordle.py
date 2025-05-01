import random, os

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

dailyWord: list[str] = ["c","l","e","a","r"]
guessList: list[list] = [["a","p","p","l","e"],["c","l","e","r","e"],["c","l","e","a","r"]]

for y in dailyWord:
    print(y,end='')
print("\n")

for x in range(len(guessList)):
    charPre = [dailyWord.count(dailyWord[0]),dailyWord.count(dailyWord[1]),dailyWord.count(dailyWord[2]),dailyWord.count(dailyWord[3]),dailyWord.count(dailyWord[4])]
    charDone: list[int] = [0,0,0,0,0]
    for y in range(len(guessList[x])):
        if guessList[x][y] == dailyWord[y]:
            charDone[y] += 1
            if charDone[y] <= charPre[y]:
                print(Green,end='')
        elif guessList[x][y] in dailyWord:
            charDone[y] += 1
            if charDone[y] <= charPre[y]:
                print(Yellow,end='')
        print(guessList[x][y],End,end='')
    print()