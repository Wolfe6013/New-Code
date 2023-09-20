WordList = ['apple','boons','corps','dorks','earth','fruit','great','hides','igloo','jewel','krill','lyric','month','ninja','ozone','pluck','quirk','robot','seize','twine','udder','viper','wrung','yeast','zesty']

def BlackLetters(): 
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Black Letters: ')
    for Word in WordList:
        if Wordle[0] in AcceptableVoid or Wordle[0] not in Word:
            if Wordle[1] in AcceptableVoid or Wordle[1] not in Word:
                if Wordle[2] in AcceptableVoid or Wordle[2] not in Word:
                    if Wordle[3] in AcceptableVoid or Wordle[3] not in Word:
                        if Wordle[4] in AcceptableVoid or Wordle[4] not in Word:
                            PossibleWords.append(Word)
    for NumberOfMatches, Word in enumerate(PossibleWords): ...
    for Word in PossibleWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")
BlackLetters()