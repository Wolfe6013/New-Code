def Wordle():
    WordList = ['apple','boons','corps','dorks','earth','fruit','great','hides','igloo','jewel','krill','lyric','month','ninja','ozone','pluck','quirk','robot','seize','twine','udder','viper','wrung','yeast','zesty']
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Green Letters: ')
    for Word in WordList:
        if Wordle[0] in AcceptableVoid or Wordle[0] == Word[0]:
            if Wordle[1] in AcceptableVoid or Wordle[1] == Word[1]:
                if Wordle[2] in AcceptableVoid or Wordle[2] == Word[2]:
                    if Wordle[3] in AcceptableVoid or Wordle[3] == Word[3]:
                        if Wordle[4] in AcceptableVoid or Wordle[4] == Word[4]:
                            PossibleWords.append(Word)
    for NumberOfMatches, Word in enumerate(PossibleWords): ...
    for Word in PossibleWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")
Wordle()