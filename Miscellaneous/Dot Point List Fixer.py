LinesDone = 0
List = []
while LinesDone == 0:
    Line = input('Line: ')
    if Line == '':
        LinesDone = 1
    else:
        List.append(Line)
for Word in List:
    CurrentLetter = -1
    WordString = ([*Word])
    for letter in WordString:
        CurrentLetter += 1
        if letter == '.':
            del WordString[CurrentLetter]
    del List[0]
    WordString.append(', ')
    WordStringFixed = ""
    for i in WordString:
        WordStringFixed += i +''
    List.append(WordStringFixed)
ListFixed = ""
for i in List:
    ListFixed += i +''
List.append(ListFixed)
print(ListFixed)