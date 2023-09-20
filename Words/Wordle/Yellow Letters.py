WordList = ['apple','boons','corps','dorks','earth','fruit','great','hides','igloo','jewel','krill','lyric','month','ninja','ozone','pluck','quirk','robot','seize','twine','udder','viper','wrung','yeast','zesty']

def Wordle(): 
    PossibleWords1 = []
    ActualWords1 = []
    PossibleWords2 = []
    ActualWords2 = []
    Wordle = input('Yellow Letters: ')
    WordleList = list(Wordle)
    if len(list(Wordle)) == 1:
        for Word in WordList:
            SplitWord = list(Word)
            for WordLetter in SplitWord:
                for YellowLetter in WordleList:
                    if WordLetter == YellowLetter:
                        PossibleWords1.append(Word)
        if PossibleWords1 == 1:
            ActualWords1.append(PossibleWords1)
        else:
            for ListCheck, current in enumerate(PossibleWords1):
                if PossibleWords1[ListCheck] == PossibleWords1[ListCheck-1]:    ...
                else:
                    ActualWords1.append(current)
        print(ActualWords1)
    else:
        for WordX in WordList:
            Score = 0
            for ListLength, j in enumerate(WordleList):
                if WordleList[ListLength] in WordX:
                    print(f'{WordX} {ListLength} {WordleList[ListLength]}')
                    PossibleWords2.append(WordX)
                    Score += 1
            if Score >= len(list(Wordle)):
                ActualWords2.append(WordX)
        print(ActualWords2)
Wordle()