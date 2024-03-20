def Encode(Word):
    newWord: list = []
    for letter in Word:
        if letter == 'A':
            newWord.append('9')
        elif letter == 'B':
            newWord.append('d')
        elif letter == 'C':
            newWord.append('a')
        elif letter == 'D':
            newWord.append('h')
        elif letter == 'E':
            newWord.append('O')
        elif letter == 'F':
            newWord.append('|')
        elif letter == 'G':
            newWord.append('v')
        elif letter == 'H':
            newWord.append('o')
        elif letter == 'I':
            newWord.append('!')
        elif letter == 'J':
            newWord.append('(')
        elif letter == 'K':
            newWord.append('F')
        elif letter == 'L':
            newWord.append('^')
        elif letter == 'M':
            newWord.append('S')
        elif letter == 'N':
            newWord.append('-')
        elif letter == 'O':
            newWord.append('=')
        elif letter == 'P':
            newWord.append(' ')
        elif letter == 'Q':
            newWord.append('x')
        elif letter == 'R':
            newWord.append('+')
        elif letter == 'S':
            newWord.append('V')
        elif letter == 'T':
            newWord.append('k')
        elif letter == 'U':
            newWord.append('I')
        elif letter == 'V':
            newWord.append('T')
        elif letter == 'W':
            newWord.append('4')
        elif letter == 'X':
            newWord.append('*')
        elif letter == 'Y':
            newWord.append('Q')
        elif letter == 'Z':
            newWord.append('G')
        elif letter == 'a':
            newWord.append('&')
        elif letter == 'b':
            newWord.append('p')
        elif letter == 'c':
            newWord.append('6')
        elif letter == 'd':
            newWord.append('L')
        elif letter == 'e':
            newWord.append('`')
        elif letter == 'f':
            newWord.append('e')
        elif letter == 'g':
            newWord.append('[')
        elif letter == 'h':
            newWord.append('q')
        elif letter == 'i':
            newWord.append('M')
        elif letter == 'j':
            newWord.append('Y')
        elif letter == 'k':
            newWord.append('w')
        elif letter == 'l':
            newWord.append(']')
        elif letter == 'm':
            newWord.append('N')
        elif letter == 'n':
            newWord.append('c')
        elif letter == 'o':
            newWord.append('g')
        elif letter == 'p':
            newWord.append('/')
        elif letter == 'q':
            newWord.append('y')
        elif letter == 'r':
            newWord.append('B')
        elif letter == 's':
            newWord.append(':')
        elif letter == 't':
            newWord.append('b')
        elif letter == 'u':
            newWord.append('1')
        elif letter == 'v':
            newWord.append(',')
        elif letter == 'w':
            newWord.append('$')
        elif letter == 'x':
            newWord.append('7')
        elif letter == 'y':
            newWord.append('s')
        elif letter == 'z':
            newWord.append('{')
        elif letter == '1':
            newWord.append('t')
        elif letter == '2':
            newWord.append('3')
        elif letter == '3':
            newWord.append('H')
        elif letter == '4':
            newWord.append('E')
        elif letter == '5':
            newWord.append('~')
        elif letter == '6':
            newWord.append('A')
        elif letter == '7':
            newWord.append('P')
        elif letter == '8':
            newWord.append('r')
        elif letter == '9':
            newWord.append('U')
        elif letter == '0':
            newWord.append('@')
        elif letter == '!':
            newWord.append(')')
        elif letter == '@':
            newWord.append('j')
        elif letter == '#':
            newWord.append('.')
        elif letter == '$':
            newWord.append('?')
        elif letter == '%':
            newWord.append('}')
        elif letter == '^':
            newWord.append('n')
        elif letter == '&':
            newWord.append('%')
        elif letter == '*':
            newWord.append('f')
        elif letter == '(':
            newWord.append('<')
        elif letter == ')':
            newWord.append('W')
        elif letter == '-':
            newWord.append('>')
        elif letter == '_':
            newWord.append('z')
        elif letter == '+':
            newWord.append('2')
        elif letter == '=':
            newWord.append('8')
        elif letter == '`':
            newWord.append('m')
        elif letter == '~':
            newWord.append('l')
        elif letter == '[':
            newWord.append('C')
        elif letter == ']':
            newWord.append('5')
        elif letter == '{':
            newWord.append('D')
        elif letter == '}':
            newWord.append('R')
        elif letter == '|':
            newWord.append('i')
        elif letter == ':':
            newWord.append('K')
        elif letter == ',':
            newWord.append('_')
        elif letter == '<':
            newWord.append('u')
        elif letter == '.':
            newWord.append('#')
        elif letter == '>':
            newWord.append('Z')
        elif letter == '/':
            newWord.append('0')
        elif letter == '?':
            newWord.append('X')
        elif letter == ' ':
            newWord.append('J')
        elif letter == ";":
            newWord.append(";")
    Word: str = ''
    for x in newWord:
        Word += x
    return Word

def Decode(Word):
    newWord: list = []
    for letter in Word:
        if letter == '9':
            newWord.append('A')
        elif letter == 'd':
            newWord.append('B')
        elif letter == 'a':
            newWord.append('C')
        elif letter == 'h':
            newWord.append('D')
        elif letter == 'O':
            newWord.append('E')
        elif letter == '|':
            newWord.append('F')
        elif letter == 'v':
            newWord.append('G')
        elif letter == 'o':
            newWord.append('H')
        elif letter == '!':
            newWord.append('I')
        elif letter == '(':
            newWord.append('J')
        elif letter == 'F':
            newWord.append('K')
        elif letter == '^':
            newWord.append('L')
        elif letter == 'S':
            newWord.append('M')
        elif letter == '-':
            newWord.append('N')
        elif letter == '=':
            newWord.append('O')
        elif letter == ' ':
            newWord.append('P')
        elif letter == 'x':
            newWord.append('Q')
        elif letter == '+':
            newWord.append('R')
        elif letter == 'V':
            newWord.append('S')
        elif letter == 'k':
            newWord.append('T')
        elif letter == 'I':
            newWord.append('U')
        elif letter == 'T':
            newWord.append('V')
        elif letter == '4':
            newWord.append('W')
        elif letter == '*':
            newWord.append('X')
        elif letter == 'Q':
            newWord.append('Y')
        elif letter == 'G':
            newWord.append('Z')
        elif letter == '&':
            newWord.append('a')
        elif letter == 'p':
            newWord.append('b')
        elif letter == '6':
            newWord.append('c')
        elif letter == 'L':
            newWord.append('d')
        elif letter == '`':
            newWord.append('e')
        elif letter == 'e':
            newWord.append('f')
        elif letter == '[':
            newWord.append('g')
        elif letter == 'q':
            newWord.append('h')
        elif letter == 'M':
            newWord.append('i')
        elif letter == 'Y':
            newWord.append('j')
        elif letter == 'w':
            newWord.append('k')
        elif letter == ']':
            newWord.append('l')
        elif letter == 'N':
            newWord.append('m')
        elif letter == 'c':
            newWord.append('n')
        elif letter == 'g':
            newWord.append('o')
        elif letter == '/':
            newWord.append('p')
        elif letter == 'y':
            newWord.append('q')
        elif letter == 'B':
            newWord.append('r')
        elif letter == ':':
            newWord.append('s')
        elif letter == 'b':
            newWord.append('t')
        elif letter == '1':
            newWord.append('u')
        elif letter == ',':
            newWord.append('v')
        elif letter == '$':
            newWord.append('w')
        elif letter == '7':
            newWord.append('x')
        elif letter == 's':
            newWord.append('y')
        elif letter == '{':
            newWord.append('z')
        elif letter == 't':
            newWord.append('1')
        elif letter == '3':
            newWord.append('2')
        elif letter == 'H':
            newWord.append('3')
        elif letter == 'E':
            newWord.append('4')
        elif letter == '~':
            newWord.append('5')
        elif letter == 'A':
            newWord.append('6')
        elif letter == 'P':
            newWord.append('7')
        elif letter == 'r':
            newWord.append('8')
        elif letter == 'U':
            newWord.append('9')
        elif letter == '@':
            newWord.append('0')
        elif letter == ')':
            newWord.append('!')
        elif letter == 'j':
            newWord.append('@')
        elif letter == '.':
            newWord.append('#')
        elif letter == '?':
            newWord.append('$')
        elif letter == '}':
            newWord.append('%')
        elif letter == 'n':
            newWord.append('^')
        elif letter == '%':
            newWord.append('&')
        elif letter == 'f':
            newWord.append('*')
        elif letter == '<':
            newWord.append('(')
        elif letter == 'W':
            newWord.append(')')
        elif letter == '>':
            newWord.append('-')
        elif letter == 'z':
            newWord.append('_')
        elif letter == '2':
            newWord.append('+')
        elif letter == '8':
            newWord.append('=')
        elif letter == 'm':
            newWord.append('`')
        elif letter == 'l':
            newWord.append('~')
        elif letter == 'C':
            newWord.append('[')
        elif letter == '5':
            newWord.append(']')
        elif letter == 'D':
            newWord.append('{')
        elif letter == 'R':
            newWord.append('}')
        elif letter == 'i':
            newWord.append('|')
        elif letter == 'K':
            newWord.append(':')
        elif letter == '_':
            newWord.append(',')
        elif letter == 'u':
            newWord.append('<')
        elif letter == '#':
            newWord.append('.')
        elif letter == 'Z':
            newWord.append('>')
        elif letter == '0':
            newWord.append('/')
        elif letter == 'X':
            newWord.append('?')
        elif letter == 'J':
            newWord.append(' ')
    Word: str = ''
    for x in newWord:
        Word += x
    return Word

def FullEncode(Word):
    stepOne = Encode(Word)
    stepTwo = Encode(stepOne)
    stepThree = Encode(stepTwo)
    return stepThree

def FullDecode(Word):
    stepOne = Decode(Word)
    stepTwo = Decode(stepOne)
    stepThree = Decode(stepTwo)
    return stepThree

if __name__ == "__main__":
    while True:
        password: str = input()##Quick Brown Fox Jumps Over The Lazy Dog!
        newPassword = FullEncode(password)
        print(newPassword)
        print(FullDecode(newPassword))
        print()