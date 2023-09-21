import random
import time
#there is 141,167,095,653,3766 possible combinations (26^10)
fullWord = input('What is the word you are looking for? ')
waitTime = input("Wait Time In-Between Checks (seconds): ")

if waitTime == "":
    waitTime = 0
found = 0

FirstLetter = fullWord[0]
SecondLetter = fullWord[1]
ThirdLetter = fullWord[2]
FourthLetter = fullWord[3]
FifthLetter = fullWord[4]
SixthLetter = fullWord[5]
SeventhLetter = fullWord[6]
EighthLetter = fullWord[7]
NinthLetter = fullWord[8]
TenthLetter = fullWord[9]

Actual1 = 0
Actual2 = 0
Actual3 = 0
Actual4 = 0
Actual5 = 0
Actual6 = 0
Actual7 = 0
Actual8 = 0
Actual9 = 0
Actual10 = 0

timesdone = 0
found = 0
while found == 0:
    timesdone += 1
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    if Actual1 == 0:
        letter1 = random.choice(Alphabet)
    if Actual2 == 0:
        letter2 = random.choice(Alphabet)
    if Actual3 == 0:
        letter3 = random.choice(Alphabet)
    if Actual4 == 0:
        letter4 = random.choice(Alphabet)
    if Actual5 == 0:
        letter5 = random.choice(Alphabet)
    if Actual6 == 0:
        letter6 = random.choice(Alphabet)
    if Actual7 == 0:
        letter7 = random.choice(Alphabet)
    if Actual8 == 0:
        letter8 = random.choice(Alphabet)
    if Actual9 == 0:
        letter9 = random.choice(Alphabet)
    if Actual10 == 0:
        letter10 = random.choice(Alphabet)
    print(f"Check {timesdone}   {letter1}{letter2}{letter3}{letter4}{letter5}{letter6}{letter7}{letter8}{letter9}{letter10}")
    time.sleep(float(waitTime))
    if letter1 == FirstLetter:
        Actual1 = 1
    if letter2 == SecondLetter:
        Actual2 = 2
    if letter3 == ThirdLetter:
        Actual3 = 3
    if letter4 == FourthLetter:
        Actual4 = 4
    if letter5 == FifthLetter:
        Actual5 = 5
    if letter6 == SixthLetter:
        Actual6 = 6
    if letter7 == SeventhLetter:
        Actual7 = 7
    if letter8 == EighthLetter:
        Actual8 = 8
    if letter9 == NinthLetter:
        Actual9 = 9
    if letter10 == TenthLetter:
        Actual10 = 10
    if FirstLetter == letter1 and SecondLetter == letter2 and ThirdLetter == letter3 and FourthLetter == letter4 and FifthLetter == letter5 and SixthLetter == letter6 and SeventhLetter == letter7 and EighthLetter == letter8 and NinthLetter == letter9 and TenthLetter == letter10:
        print(f"Done in only {timesdone} checks!!!")
        found = 1