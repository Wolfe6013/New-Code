import random, sys, os, time
import numpy as np
import matplotlib.pyplot as plt

def BaseD8Dist():
    global data_dict
    #NoSides: int = input("Dice Size? ")
    NoSides: int = 8
    Rolls: list[int] = []
    done = 0
    FinalSum = 0

    for d1 in range(NoSides):
        for d2 in range(NoSides):
            Rolls.append(int(d1+d2+2))

    no2 = 0
    no3 = 0
    no4 = 0
    no5 = 0
    no6 = 0
    no7 = 0
    no8 = 0
    no9 = 0
    no10 = 0
    no11 = 0
    no12 = 0
    no13 = 0
    no14 = 0
    no15 = 0
    no16 = 0

    for x in Rolls:
        FinalSum += x
        if x == 2: no2 += 1
        if x == 3: no3 += 1
        if x == 4: no4 += 1
        if x == 5: no5 += 1
        if x == 6: no6 += 1
        if x == 7: no7 += 1
        if x == 8: no8 += 1
        if x == 9: no9 += 1
        if x == 10: no10 += 1
        if x == 11: no11 += 1
        if x == 12: no12 += 1
        if x == 13: no13 += 1
        if x == 14: no14 += 1
        if x == 15: no15 += 1
        if x == 16: no16 += 1
    data_dict = {'2':no2,'3':no3,'4':no4,'5':no5,'6':no6,'7':no7,'8':no8,'9':no9,'10':no10,'11':no11,'12':no12,'13':no13,'14':no14,'15':no15,'16':no16}
    ReturnList = [data_dict,f"{no2}-{no3}-{no4}-{no5}-{no6}-{no7}-{no8}-{no9}-{no10}-{no11}-{no12}-{no13}-{no14}-{no15}-{no16}"]
    return(ReturnList)

def Graph2D8(data):
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    #  Bar plot
    plt.bar(courses, values, color ='green',
            width = 0.95)
    plt.show()

if __name__ == "__main__":
    BaseD8Dist()
    Graph2D8(data_dict)