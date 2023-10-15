import random

def CypherA(Word,x):
    for x in Word:
        if x == 'a':
            x = 'l'
        if x == 'b': 
            x = 'f'
        if x == 'c': 
            x = 'b'
        if x == 'd': 
            x = 'o'
        if x == 'e': 
            x = 'g'
        if x == 'f': 
            x = 'w'
        if x == 'g': 
            x = 's'
        if x == 'h': 
            x = 'v'
        if x == 'i': 
            x = 'a'
        if x == 'j': 
            x = 'y'
        if x == 'k': 
            x = 'e'
        if x == 'l': 
            x = 'x'
        if x == 'm': 
            x = 'h'
        if x == 'n': 
            x = 'r'
        if x == 'o': 
            x = 'n'
        if x == 'p': 
            x = 'k'
        if x == 'q': 
            x = 'p'
        if x == 'r': 
            x = 'i'
        if x == 's': 
            x = 'q'
        if x == 't': 
            x = 'c'
        if x == 'u': 
            x = 't'
        if x == 'v': 
            x = 'd'
        if x == 'w': 
            x = 'm'
        if x == 'x': 
            x = 'u'
        if x == 'y': 
            x = 'j'
        if x == 'z': 
            x = 'z'

def CypherB(Word,x):
    for x in Word:
        if x == 'a':
            x = 'd'
        if x == 'b': 
            x = 'b'
        if x == 'c': 
            x = 'e'
        if x == 'd': 
            x = 't'
        if x == 'e': 
            x = 'l'
        if x == 'f': 
            x = 'v'
        if x == 'g': 
            x = 'j'
        if x == 'h': 
            x = 'a'
        if x == 'i': 
            x = 'g'
        if x == 'j': 
            x = 'u'
        if x == 'k': 
            x = 'n'
        if x == 'l': 
            x = 'o'
        if x == 'm': 
            x = 'r'
        if x == 'n': 
            x = 'z'
        if x == 'o': 
            x = 'y'
        if x == 'p': 
            x = 'p'
        if x == 'q': 
            x = 'w'
        if x == 'r': 
            x = 'x'
        if x == 's': 
            x = 'i'
        if x == 't': 
            x = 'q'
        if x == 'u': 
            x = 'c'
        if x == 'v': 
            x = 'k'
        if x == 'w': 
            x = 's'
        if x == 'x': 
            x = 'f'
        if x == 'y': 
            x = 'h'
        if x == 'z': 
            x = 'm'
    Word.append('a')

def CypherC(Word,x):
    for x in Word:
        ...
def CypherD(Word,x):
    for x in Word:
        ...
def CypherE(Word,x):
    for x in Word:
        ...
def CypherF(Word,x):
    for x in Word:
        ...
def CypherG(Word,x):
    for x in Word:
        ...
def CypherH(Word,x):
    for x in Word:
        ...
def CypherI(Word,x):
    for x in Word:
        ...
def CypherJ(Word,x):
    for x in Word:
        ...
def CypherK(Word,x):
    for x in Word:
        ...
def CypherL(Word,x):
    for x in Word:
        ...
def CypherM(Word,x):
    for x in Word:
        ...
def CypherN(Word,x):
    for x in Word:
        ...
def CypherO(Word,x):
    for x in Word:
        ...
def CypherP(Word,x):
    for x in Word:
        ...
def CypherQ(Word,x):
    for x in Word:
        ...
def CypherR(Word,x):
    for x in Word:
        ...
def CypherS(Word,x):
    for x in Word:
        ...
def CypherT(Word,x):
    for x in Word:
        ...
def CypherU(Word,x):
    for x in Word:
        ...
def CypherV(Word,x):
    for x in Word:
        ...
def CypherW(Word,x):
    for x in Word:
        ...
def CypherX(Word,x):
    for x in Word:
        ...
def CypherY(Word,x):
    for x in Word:
        ...
def CypherZ(Word,x):
    for x in Word:
        ...

Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

FullSentence = input('What do you need encoded? ')
SplitSentence = []
WordList = []
WordString = ''

for x in FullSentence:
    if x == ' ' or x == '.':
        for i in WordList:
            WordString += i +''
        SplitSentence.append(WordString)
        WordString = ''
        WordList = []
    else:
        WordList.append(x)

for x in SplitSentence:
    CypherA()
print(SplitSentence)