import random

sentence = input('What sentence needs grammatical fixing? ')
finalSentence = []
sPos = 0

for x in sentence:
    if x == 'l' or x == 'L':
        x = '| '
    if x == 'o' or x == 'O':
        x = '||  '
    if x == 's' or x == 'S':
        sList = ['|| ','|_']
        x = sList[sPos]
        if sPos == 0:
            sPos += 1
        else: sPos -= 1
    finalSentence.append(x)

for x in finalSentence:
    print(x, end='')
print()