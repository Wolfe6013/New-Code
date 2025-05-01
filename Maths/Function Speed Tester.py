import time, sys, os, math
from Binary_Sorter import BinarySort, RandomFloat

#Don't forget to move this file into same directory as the function file
if __name__ == "__main__":
    RunNum = 10000
    start = time.time()
    for x in range(RunNum):
        list1 = RandomFloat(10000)
        BinarySort(list1)
        if (math.log10(x)) %1 == 0:
            print(f"{x}th iteration")
    end = time.time()
    decimalPlaces1 = 9-len(str(int(end - start)))
    decimalPlaces2 = 9-len(str(int((end - start)*1000)))
    decimalPlaces3 = 9-len(str(int((end - start)/RunNum)))
    decimalPlaces4 = 9-len(str(int((end - start)*1000/RunNum)))
    print(f"Total run time:   {round(end - start,decimalPlaces1)}sec - {round((end - start)*1000,decimalPlaces2)}ms")
    print(f"Average run time: {round((end - start)/RunNum,decimalPlaces3)}sec - {round((end - start)*1000/RunNum,decimalPlaces4)}ms")