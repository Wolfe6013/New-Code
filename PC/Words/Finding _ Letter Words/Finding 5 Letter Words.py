import random
import time
#there is 11,881,376 possible combinations (26^5)
timesdone = 0
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
FullWord = input('What is the word you are looking for? ')
FirstLetter = FullWord[0]
SecondLetter = FullWord[1]
ThirdLetter = FullWord[2]
FourthLetter = FullWord[3]
FifthLetter = FullWord[4]
wanttodo = int(input("Maximum Number of Checks: "))
wait = int(input("Wait Time In-Between Checks (seconds): "))
if FirstLetter not in Alphabet or SecondLetter not in Alphabet or ThirdLetter not in Alphabet or FourthLetter not in Alphabet or FifthLetter not in Alphabet:
    timesdone = wanttodo
    print("There is a character in '"+ FullWord+ "' that isn't a letter in the alphabet (make sure its all lowercase)")
if wait == "":
    wait = 0
found = 0
while wanttodo > timesdone:
    letter1 = random.choice(Alphabet)
    letter2 = random.choice(Alphabet)
    letter3 = random.choice(Alphabet)
    letter4 = random.choice(Alphabet)
    letter5 = random.choice(Alphabet)
    print("Check",timesdone+1," ",letter1+ letter2+ letter3+ letter4+ letter5)
    time.sleep(wait)
    if FirstLetter == letter1 and SecondLetter == letter2 and ThirdLetter == letter3 and FourthLetter == letter4 and FifthLetter == letter5:
        print("Done!!!")
        timesdone = wanttodo
        found = 1
    timesdone = timesdone+1
if found == 0:
    print("'"+ FullWord+ "' not found in",timesdone,'checks')