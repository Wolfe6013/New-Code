import time
import sys
import random

beginning = int(input("First number to check?  "))
end = int(input("What is the last number you want to check?  "))
end = end+1
start = beginning
continuestart = start
during = continuestart
attempt = 1
runno = 0

while continuestart < end:
    
    while during > 1:
        print("during:",during,"run",runno,"times - attempt:",attempt,"out of",end-beginning,"(theres",end-beginning-attempt+1,"remaining)")
        if (during % 2) == 0: during = during/2
        else: during = (during+1)*2
        time.sleep(0.2)
        runno = runno+1
    print("Number:",during,"in",runno,"runs - attempt:",attempt,"out of",end-beginning,"(theres",end-beginning-attempt,"remaining)")
    continuestart = continuestart+1
    during = continuestart
    print("attempt",attempt,"done")
    attempt = attempt+1
    runno = 0