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
totalNumberOfRuns: list = []
startTime = time.time()
longest: list[int] = [0,0,0]

def save():
    global totalNumberOfRuns
    f = open("xPermutation.txt","w")
    for x in totalNumberOfRuns:
        if totalNumberOfRuns.index(x) == 0: f.write(f"{x}")
        else: f.write(f",{x}")
    f.write(f"\n[{longest[0]},{longest[1]},{longest[2]}]\n")
    f.write(f"{endTime - startTime}sec\n")
    f.close()

PrintDuring = False
PrintFinish = False

while continuestart < end:
    while during > 1:
        if during < 10000000 and PrintDuring:
            print(f"during: {during:<7} run {runno:<3} times - attempt: {attempt} out of {end-beginning} (theres {end-beginning-attempt+1} remaining)")
        elif PrintDuring:
            print(f"during: {during} run {runno:<3} times - attempt: {attempt} out of {end-beginning} (theres {end-beginning-attempt+1} remaining)")
        if (during % 2) == 0: during = during/2
        else: during = (during+1)*2
        #time.sleep(0.2)
        runno = runno+1
    if runno < 3 and PrintFinish:
        print(f"Number: {during} in {runno:<2} runs - attempt: {attempt} out of {end-beginning} (theres {end-beginning-attempt} remaining)")
    elif PrintFinish:
        print(f"Number: {during} in {runno} runs - attempt: {attempt} out of {end-beginning} (theres {end-beginning-attempt} remaining)")
    totalNumberOfRuns.append(runno)
    if runno > longest[0]:
        longest[0] = runno
        longest[1] = 1
        longest[2] = attempt
    elif runno == longest[0]:
        longest[1] += 1
    continuestart = continuestart+1
    during = continuestart
    attempt = attempt+1
    runno = 0
print()
endTime = time.time()
print(f"Time elapsed: {endTime - startTime}sec, {(endTime - startTime)/60}min and {(endTime - startTime)/60/60}hours.")
print(f"Highest permutation: {longest[0]}, occuring {longest[1]} times from the origin number {longest[2]}.")
#for x in totalNumberOfRuns:
#    if totalNumberOfRuns.index(x) == 0:
#        print(f"{x}",end="")
#    else: print(f"{x}",end="")
save()