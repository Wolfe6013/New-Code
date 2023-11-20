import os, random, time, sys, pyautogui, keyboard

Gray = f"\033[1;30;40m"
Red = f"\033[1;31;40m"
Green = f"\033[1;32;40m"
Yellow = f"\033[1;33;40m"
Blue = f"\033[1;34;40m"
Purple = f"\033[1;35;40m"
Cyan = f"\033[1;36;40m"
End = f"\033[0m"

def clear():
    os.system("cls")

while True:
    clear()
    percent = float(input("What percent? "))

    vType = input("M or V? ")

    if vType == "M":
        rangeNum = 150
        spaceNum = 15
        outOf = float(input("Out of? "))
        percent = (percent/outOf)*100
    elif vType == "V":
        rangeNum = 100
        spaceNum = 10

    if vType == "M" or vType == "V":
        print(f"{round(percent,3)}/{rangeNum} - {vType}")

        percent = round(percent)
        totalPercent = percent

        numbers = ['⒈','⒉','⒊','⒋','⒌','⒍','⒎','⒏','⒐','⒑','⒒','⒓','⒔','⒕','⒖']

        for a, b in enumerate(numbers):
            if a < spaceNum:
                print(f"{b} ",end="")
        print()

        for z, y in enumerate(range(rangeNum)):
            if y+1 > 100-percent and vType == "V":
                print(Green,end="")
            elif ((y+1) % spaceNum == 1 or y == 0) and vType == "M":
                print(Blue,end="")
            elif (y+1) % spaceNum == 0 and vType == "M" and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 14 and vType == "M" and totalPercent > 10 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 13 and vType == "M" and totalPercent > 20 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 12 and vType == "M" and totalPercent > 30 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 11 and vType == "M" and totalPercent > 40 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 10 and vType == "M" and totalPercent > 50 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 9 and vType == "M" and totalPercent > 60 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 8 and vType == "M" and totalPercent > 70 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 7 and vType == "M" and totalPercent > 80 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 6 and vType == "M" and totalPercent > 90 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 5 and vType == "M" and totalPercent > 100 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 4 and vType == "M" and totalPercent > 110 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 3 and vType == "M" and totalPercent > 120 and percent > 0:
                print(Green,end="")
                percent -= 1
            elif (y+1) % spaceNum == 3 and vType == "M" and totalPercent > 130 and percent > 0:
                print(Green,end="")
                percent -= 1
            else:
                print(Gray,end="")
            print(f"⬚ {End}",end="")
            if (y+1) % spaceNum == 0:
                print(numbers[int((y+1)/spaceNum-1)])
        print(End)
        input()