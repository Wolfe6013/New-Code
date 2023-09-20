import random
import time
#there is 26 possible combinations
timesdone = 0
firstletter = input("Letter: ")
wanttodo = int(input("Maximum Number of Checks: "))
wait = int(input("Wait Time In-Between Checks (in milliseconds): "))
found = 0
while wanttodo > timesdone:
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter1 = random.choice(Alphabet)
    print("Check",timesdone+1," ",letter1)
    time.sleep(wait/1000)
    if firstletter == letter1:
        print("Done!!!")
        timesdone = wanttodo
        found = 1
    timesdone = timesdone+1
if found == 0:
    print("'"+ firstletter+ "' not found in",timesdone,'checks')