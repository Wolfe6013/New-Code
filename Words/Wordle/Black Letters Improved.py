def BlackLetters():
    WordList = ['apple','boons','corps','dorks','earth','fruit','great','hides','igloo','jewel','krill','lyric','month','ninja','ozone','pluck','quirk','robot','seize','twine','udder','viper','wrung','yeast','zesty']
    PossibleWords = []
    Wordle = input('Black Letters: ')
    for WordLength, q in enumerate(Wordle): ...
    for Word in WordList:
        Score = 0
        x = int(0)
        for letter in Wordle:
            print(f'{Word} {Wordle} {WordLength+1} {x} {Wordle[x]}')
            if Wordle[x] not in Word:
                Score +=1
                x += 1
        if Score == 5:
            PossibleWords.append(Word)
    print(PossibleWords)
    for NumberOfMatches, Word in enumerate(PossibleWords): ...
    for Word in PossibleWords:
        if NumberOfMatches > 0:
            print(f"{Word}, ", end='')
            NumberOfMatches -= 1
        else:
            print(f"{Word}.")
BlackLetters()