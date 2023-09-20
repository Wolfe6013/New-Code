import random
import time
#there is 308,915,776 possible combinations (26^6)
timesdone = 0
FullWord = input('What is the word you are looking for? ')
FirstLetter = FullWord[0]
SecondLetter = FullWord[1]
ThirdLetter = FullWord[2]
FourthLetter = FullWord[3]
FifthLetter = FullWord[4]
SixthLetter = FullWord[5]
wanttodo = int(input("Maximum Number of Checks: "))
wait = int(input("Wait Time In-Between Checks (seconds): "))

if wait == "":
    wait = 0
found = 0
while wanttodo > timesdone:
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter1 = random.choice(Alphabet)
    letter2 = random.choice(Alphabet)
    letter3 = random.choice(Alphabet)
    letter4 = random.choice(Alphabet)
    letter5 = random.choice(Alphabet)
    letter6 = random.choice(Alphabet)
    print(f"Check {timesdone+1}   {letter1}{letter2}{letter3}{letter4}{letter5}{letter6}")
    time.sleep(wait)
    if FirstLetter == letter1 and SecondLetter == letter2 and ThirdLetter == letter3 and FourthLetter == letter4 and FifthLetter == letter5 and SixthLetter == letter6:
        print("Done!!!")
        timesdone = wanttodo  
        found = 1 
    timesdone += 1
if found == 0:
    print(f"'{FullWord}' not found in {timesdone} checks")