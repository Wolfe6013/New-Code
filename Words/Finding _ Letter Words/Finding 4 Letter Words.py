import random
import time
#there is 456,976 possible combinations (26^4)
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
timesdone = 0
FullWord = input('What is the word you are looking for? ')
FirstLetter = FullWord[0]
SecondLetter = FullWord[1]
ThirdLetter = FullWord[2]
FourthLetter = FullWord[3]
wanttodo = int(input("Maximum Number of Checks: "))
wait = int(input("Wait Time In-Between Checks (seconds): "))
found = 0
if FirstLetter not in Alphabet or SecondLetter not in Alphabet or ThirdLetter not in Alphabet or FourthLetter not in Alphabet:
    timesdone = wanttodo
    print("There is a character in '"+ FullWord+ "' that isn't a letter in the alphabet (make sure its all lowercase)")
while wanttodo > timesdone:
    letter1 = random.choice(Alphabet)
    letter2 = random.choice(Alphabet)
    letter3 = random.choice(Alphabet)
    letter4 = random.choice(Alphabet)
    print("Check",timesdone+1," ",letter1+ letter2+ letter3+ letter4)
    time.sleep(wait/1000)
    if FirstLetter == letter1 and SecondLetter == letter2 and ThirdLetter == letter3 and FourthLetter == letter4:
        print("Done!!!")
        timesdone = wanttodo 
        found = 1
    timesdone = timesdone+1
if found == 0:
    print("'"+ FullWord+ "' not found in",timesdone,'checks')