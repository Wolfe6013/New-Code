import random, sys, os, time
import numpy as np
import matplotlib.pyplot as plt
from MixedDiceMeetAverage2 import BaseD8Dist, Graph2D8

if __name__ == "__main__":
    ReturnList = BaseD8Dist()
    BaseDist = ReturnList[1]
    DataDictNormal = ReturnList[0]
    print(BaseDist)
    Graph2D8(DataDictNormal)