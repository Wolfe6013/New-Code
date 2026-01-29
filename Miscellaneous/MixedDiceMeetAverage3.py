import random, sys, os, time
import numpy as np
import matplotlib.pyplot as plt

def TwoDice(sideCount):
    diceCount = 2
    distribution: list[int] = []
    length: list[int] = []
    maximum = sideCount*diceCount
    for x in range(maximum):
        distribution.append(0)
        length.append(x+1)

    for x in range(sideCount):
        for y in range(sideCount):
            distribution[x+y+1] += 1

    return distribution

if __name__ == "__main__":
    sideCount = int(input("Number of sides? "))
    print(TwoDice(sideCount))