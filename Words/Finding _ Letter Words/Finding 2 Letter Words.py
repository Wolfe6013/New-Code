import random
import time
#there is 676 possible combinations (26^2)
timesdone = 0
FullWord = input('What is the word you are looking for? ')
FirstLetter = FullWord[0]
SecondLetter = FullWord[1]
wanttodo = int(input("Maximum Number of Checks: "))
wait = int(input("Wait Time In-Between Checks (seconds): "))
found = 0
while wanttodo > timesdone:
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter1 = random.choice(Alphabet)
    letter2 = random.choice(Alphabet)
    print("Check",timesdone+1," ",letter1+ letter2)
    time.sleep(wait/1000)
    if FirstLetter == letter1 and SecondLetter == letter2:
        print("Done!!!")
        timesdone = wanttodo
        found = 1
    timesdone = timesdone+1
if found == 0:
    print("'"+ FullWord+ "' not found in",timesdone,'checks')