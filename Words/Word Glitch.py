import random
import time

Word = input("Word/Sentence: ")
SplitWord = ([*Word])
#print(SplitWord)
NumberOfLetters = len(SplitWord)
TotalDone = 0
TotalRandomLetters = 10
while TotalDone < 10:
    AlphabetDone = 0
    SplitDone = 0
    while SplitDone < 100-TotalRandomLetters:
        for x in SplitWord:
          print(x, end='')
        print()
        SplitDone += 1
        time.sleep(0.01)
    while TotalRandomLetters > AlphabetDone:
        Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        RandomDone = 0
        while RandomDone < NumberOfLetters:
            print(random.choice(Alphabet), end='')
            RandomDone += 1
        AlphabetDone += 1
        print()
    TotalDone += 1
    TotalRandomLetters = TotalRandomLetters*2
