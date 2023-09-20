WordList = ['apple','boons','corps','dorks','earth','fruit','great','hides','igloo','jewel','krill','lyric','month','ninja','ozone','pluck','quirk','robot','seize','twine','udder','viper','wrung','yeast','zesty']

def GreenLetters():
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Green Letters: ')
    for Word in WordList:
        MatchLevel = 0
        for x, Letter in enumerate(Word):
            if Letter == Wordle[x] or Wordle[x] in AcceptableVoid: MatchLevel += 1
        if MatchLevel == 5: PossibleWords.append(Word)
    for NumberOfMatches, Word in enumerate(PossibleWords): ...
    for Word in PossibleWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")
GreenLetters()