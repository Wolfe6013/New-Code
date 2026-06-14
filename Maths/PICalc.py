from random import randint
from decimal import Decimal
import time

def Read():
    with open("PIwithCoins.txt", "r") as file:
        numLines = sum(1 for line in file)

    sumLines = 0
    with open("PIwithCoins.txt", "r") as file:
        for line in file:
            sumLines += (Decimal(line.strip()))
    pi = (sumLines/numLines)*4
    return pi

def Write(line):
    global first
    with open("PIwithCoins.txt", "a") as file:
        if not first:   file.write(f"\n")
        else:           first = False
        file.write(f"{str(line)}")

def FlipCoin():
    return randint(0,1)

def Run(runCount):
    valid: int = 0
    heads: int = 0
    tails: int = 0
    for x in range(int(runCount)):
        flip = FlipCoin()
        valid += flip
        if flip > 0:    heads += 1
        else:           tails += 1
        if valid > 0:
            Write(Decimal(heads/(heads+tails)))
            valid = 0
            heads = 0
            tails = 0
    return Read()

def TestFirst():
    with open("PIwithCoins.txt", "r") as file:
        numLines = sum(1 for line in file)
        if numLines == 0:   return True
        else:               return False

def Timer(start):
    global startTime
    if start:
        startTime = time.perf_counter()
    else:
        endTime = time.perf_counter()
        print(f"The code took {(endTime-startTime):.6f} seconds to run.")

def Main():
    global first
    first = TestFirst()
    runCount = int(input("Run count? "))
    Timer(True)
    print(f"Rounded down\nPI calc: {Run(runCount)}")
    Timer(False)

if __name__ == "__main__":
    Main()