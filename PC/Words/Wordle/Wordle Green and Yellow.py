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

def YellowLetters(): 
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Yellow Letters: ')
    for Word in WordList:
        if Wordle[0] in AcceptableVoid or Wordle[0] in Word:
            if Wordle[1] in AcceptableVoid or Wordle[1] in Word:
                if Wordle[2] in AcceptableVoid or Wordle[2] in Word:
                    if Wordle[3] in AcceptableVoid or Wordle[3] in Word:
                        if Wordle[4] in AcceptableVoid or Wordle[4] in Word:
                            PossibleWords.append(Word)
    for NumberOfMatches, Word in enumerate(PossibleWords): ...
    for Word in PossibleWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")

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

def GreenAndYellow():
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Green Letters: ')
    for Word in WordList:
        MatchLevel = 0
        for x, Letter in enumerate(Word):
            if Letter == Wordle[x] or Wordle[x] in AcceptableVoid: MatchLevel += 1
        if MatchLevel == 5: PossibleWords.append(Word)
    FinalWords = []
    Wordle = input('Yellow Letters: ')
    for Word in PossibleWords:
        if Wordle[0] in AcceptableVoid or Wordle[0] in Word:
            if Wordle[1] in AcceptableVoid or Wordle[1] in Word:
                if Wordle[2] in AcceptableVoid or Wordle[2] in Word:
                    if Wordle[3] in AcceptableVoid or Wordle[3] in Word:
                        if Wordle[4] in AcceptableVoid or Wordle[4] in Word:
                            FinalWords.append(Word)
    for NumberOfMatches, Word in enumerate(FinalWords): ...
    for Word in FinalWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")

def GreenYellowBlack():
    PossibleWords = []
    AcceptableVoid = ['_','-',' ','.']
    Wordle = input('Green Letters: ')
    for Word in WordList:
        MatchLevel = 0
        for x, Letter in enumerate(Word):
            if Letter == Wordle[x] or Wordle[x] in AcceptableVoid: MatchLevel += 1
        if MatchLevel == 5: PossibleWords.append(Word)
    FinalWords = []
    Wordle = input('Yellow Letters: ')
    for Word in PossibleWords:
        if Wordle[0] in AcceptableVoid or Wordle[0] in Word:
            if Wordle[1] in AcceptableVoid or Wordle[1] in Word:
                if Wordle[2] in AcceptableVoid or Wordle[2] in Word:
                    if Wordle[3] in AcceptableVoid or Wordle[3] in Word:
                        if Wordle[4] in AcceptableVoid or Wordle[4] in Word:
                            FinalWords.append(Word)
    Wordle = input('Black Letters: ')
    BlackFinalWords = []
    for Word in FinalWords:
        if Wordle[0] in AcceptableVoid or Wordle[0] not in Word:
            if Wordle[1] in AcceptableVoid or Wordle[1] not in Word:
                if Wordle[2] in AcceptableVoid or Wordle[2] not in Word:
                    if Wordle[3] in AcceptableVoid or Wordle[3] not in Word:
                        if Wordle[4] in AcceptableVoid or Wordle[4] not in Word:
                            BlackFinalWords.append(Word)
    for NumberOfMatches, Word in enumerate(BlackFinalWords): ...
    for Word in BlackFinalWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")

GreenYellowBlack()