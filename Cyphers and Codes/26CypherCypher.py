#Hello there! I am very pleased to be of your acquaintance.  #original message
#leH oleht!er I ma revp yaeldesot eb fo oy  ruqcaiauatnecn  .#Every three is turned into groups and inverted
#o Hel!thel I reer amay pvsedlebe too of ur  yaiacqentau.  nc#Every five
#t!leH or I lehama reedesvp yot ebelru fo ocaiay  .uatneq  cn   #Every seven

def A_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append(':')
        elif letter == 'B':
            newWord.append('7')
        elif letter == 'C':
            newWord.append('e')
        elif letter == 'D':
            newWord.append('z')
        elif letter == 'E':
            newWord.append('C')
        elif letter == 'F':
            newWord.append('p')
        elif letter == 'G':
            newWord.append(' ')
        elif letter == 'H':
            newWord.append('@')
        elif letter == 'I':
            newWord.append('%')
        elif letter == 'J':
            newWord.append('/')
        elif letter == 'K':
            newWord.append('Q')
        elif letter == 'L':
            newWord.append('w')
        elif letter == 'M':
            newWord.append(')')
        elif letter == 'N':
            newWord.append('s')
        elif letter == 'O':
            newWord.append('Z')
        elif letter == 'P':
            newWord.append('1')
        elif letter == 'Q':
            newWord.append('m')
        elif letter == 'R':
            newWord.append('S')
        elif letter == 'S':
            newWord.append('k')
        elif letter == 'T':
            newWord.append('5')
        elif letter == 'U':
            newWord.append('b')
        elif letter == 'V':
            newWord.append('*')
        elif letter == 'W':
            newWord.append('>')
        elif letter == 'X':
            newWord.append('R')
        elif letter == 'Y':
            newWord.append('W')
        elif letter == 'Z':
            newWord.append('3')
        elif letter == 'a':
            newWord.append('L')
        elif letter == 'b':
            newWord.append('9')
        elif letter == 'c':
            newWord.append('x')
        elif letter == 'd':
            newWord.append('6')
        elif letter == 'e':
            newWord.append('V')
        elif letter == 'f':
            newWord.append('|')
        elif letter == 'g':
            newWord.append('8')
        elif letter == 'h':
            newWord.append('.')
        elif letter == 'i':
            newWord.append('K')
        elif letter == 'j':
            newWord.append('j')
        elif letter == 'k':
            newWord.append('H')
        elif letter == 'l':
            newWord.append('A')
        elif letter == 'm':
            newWord.append('$')
        elif letter == 'n':
            newWord.append(']')
        elif letter == 'o':
            newWord.append('l')
        elif letter == 'p':
            newWord.append('(')
        elif letter == 'q':
            newWord.append('g')
        elif letter == 'r':
            newWord.append('&')
        elif letter == 's':
            newWord.append(',')
        elif letter == 't':
            newWord.append('h')
        elif letter == 'u':
            newWord.append('U')
        elif letter == 'v':
            newWord.append('q')
        elif letter == 'w':
            newWord.append('v')
        elif letter == 'x':
            newWord.append('G')
        elif letter == 'y':
            newWord.append('u')
        elif letter == 'z':
            newWord.append('F')
        elif letter == '1':
            newWord.append('}')
        elif letter == '2':
            newWord.append('B')
        elif letter == '3':
            newWord.append('?')
        elif letter == '4':
            newWord.append('P')
        elif letter == '5':
            newWord.append('-')
        elif letter == '6':
            newWord.append('^')
        elif letter == '7':
            newWord.append('!')
        elif letter == '8':
            newWord.append('O')
        elif letter == '9':
            newWord.append('c')
        elif letter == '0':
            newWord.append('f')
        elif letter == '!':
            newWord.append('y')
        elif letter == '@':
            newWord.append('T')
        elif letter == '#':
            newWord.append('{')
        elif letter == '$':
            newWord.append('t')
        elif letter == '%':
            newWord.append('#')
        elif letter == '^':
            newWord.append('[')
        elif letter == '&':
            newWord.append('_')
        elif letter == '*':
            newWord.append('D')
        elif letter == '(':
            newWord.append('=')
        elif letter == ')':
            newWord.append('2')
        elif letter == '-':
            newWord.append('d')
        elif letter == '_':
            newWord.append('o')
        elif letter == '+':
            newWord.append('4')
        elif letter == '=':
            newWord.append('a')
        elif letter == '`':
            newWord.append('M')
        elif letter == '~':
            newWord.append('E')
        elif letter == '[':
            newWord.append('I')
        elif letter == ']':
            newWord.append('J')
        elif letter == '{':
            newWord.append('N')
        elif letter == '}':
            newWord.append('~')
        elif letter == '|':
            newWord.append('n')
        elif letter == ':':
            newWord.append('r')
        elif letter == ',':
            newWord.append('i')
        elif letter == '<':
            newWord.append('X')
        elif letter == '.':
            newWord.append('Y')
        elif letter == '>':
            newWord.append('+')
        elif letter == '/':
            newWord.append('`')
        elif letter == '?':
            newWord.append('0')
        elif letter == ' ':
            newWord.append('<')
    Switched: str  = ''.join(newWord)
    return Switched

def A_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == ':':
            newWord.append('A')
        elif letter == '7':
            newWord.append('B')
        elif letter == 'e':
            newWord.append('C')
        elif letter == 'z':
            newWord.append('D')
        elif letter == 'C':
            newWord.append('E')
        elif letter == 'p':
            newWord.append('F')
        elif letter == ' ':
            newWord.append('G')
        elif letter == '@':
            newWord.append('H')
        elif letter == '%':
            newWord.append('I')
        elif letter == '/':
            newWord.append('J')
        elif letter == 'Q':
            newWord.append('K')
        elif letter == 'w':
            newWord.append('L')
        elif letter == ')':
            newWord.append('M')
        elif letter == 's':
            newWord.append('N')
        elif letter == 'Z':
            newWord.append('O')
        elif letter == '1':
            newWord.append('P')
        elif letter == 'm':
            newWord.append('Q')
        elif letter == 'S':
            newWord.append('R')
        elif letter == 'k':
            newWord.append('S')
        elif letter == '5':
            newWord.append('T')
        elif letter == 'b':
            newWord.append('U')
        elif letter == '*':
            newWord.append('V')
        elif letter == '>':
            newWord.append('W')
        elif letter == 'R':
            newWord.append('X')
        elif letter == 'W':
            newWord.append('Y')
        elif letter == '3':
            newWord.append('Z')
        elif letter == 'L':
            newWord.append('a')
        elif letter == '9':
            newWord.append('b')
        elif letter == 'x':
            newWord.append('c')
        elif letter == '6':
            newWord.append('d')
        elif letter == 'V':
            newWord.append('e')
        elif letter == '|':
            newWord.append('f')
        elif letter == '8':
            newWord.append('g')
        elif letter == '.':
            newWord.append('h')
        elif letter == 'K':
            newWord.append('i')
        elif letter == 'j':
            newWord.append('j')
        elif letter == 'H':
            newWord.append('k')
        elif letter == 'A':
            newWord.append('l')
        elif letter == '$':
            newWord.append('m')
        elif letter == ']':
            newWord.append('n')
        elif letter == 'l':
            newWord.append('o')
        elif letter == '(':
            newWord.append('p')
        elif letter == 'g':
            newWord.append('q')
        elif letter == '&':
            newWord.append('r')
        elif letter == ',':
            newWord.append('s')
        elif letter == 'h':
            newWord.append('t')
        elif letter == 'U':
            newWord.append('u')
        elif letter == 'q':
            newWord.append('v')
        elif letter == 'v':
            newWord.append('w')
        elif letter == 'G':
            newWord.append('x')
        elif letter == 'u':
            newWord.append('y')
        elif letter == 'F':
            newWord.append('z')
        elif letter == '}':
            newWord.append('1')
        elif letter == 'B':
            newWord.append('2')
        elif letter == '?':
            newWord.append('3')
        elif letter == 'P':
            newWord.append('4')
        elif letter == '-':
            newWord.append('5')
        elif letter == '^':
            newWord.append('6')
        elif letter == '!':
            newWord.append('7')
        elif letter == 'O':
            newWord.append('8')
        elif letter == 'c':
            newWord.append('9')
        elif letter == 'f':
            newWord.append('0')
        elif letter == 'y':
            newWord.append('!')
        elif letter == 'T':
            newWord.append('@')
        elif letter == '{':
            newWord.append('#')
        elif letter == 't':
            newWord.append('$')
        elif letter == '#':
            newWord.append('%')
        elif letter == '[':
            newWord.append('^')
        elif letter == '_':
            newWord.append('&')
        elif letter == 'D':
            newWord.append('*')
        elif letter == '=':
            newWord.append('(')
        elif letter == '2':
            newWord.append(')')
        elif letter == 'd':
            newWord.append('-')
        elif letter == 'o':
            newWord.append('_')
        elif letter == '4':
            newWord.append('+')
        elif letter == 'a':
            newWord.append('=')
        elif letter == 'M':
            newWord.append('`')
        elif letter == 'E':
            newWord.append('~')
        elif letter == 'I':
            newWord.append('[')
        elif letter == 'J':
            newWord.append(']')
        elif letter == 'N':
            newWord.append('{')
        elif letter == '~':
            newWord.append('}')
        elif letter == 'n':
            newWord.append('|')
        elif letter == 'r':
            newWord.append(':')
        elif letter == 'i':
            newWord.append(',')
        elif letter == 'X':
            newWord.append('<')
        elif letter == 'Y':
            newWord.append('.')
        elif letter == '+':
            newWord.append('>')
        elif letter == '`':
            newWord.append('/')
        elif letter == '0':
            newWord.append('?')
        elif letter == '<':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def B_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('O')
        elif letter == 'B':
            newWord.append('E')
        elif letter == 'C':
            newWord.append('~')
        elif letter == 'D':
            newWord.append('^')
        elif letter == 'E':
            newWord.append('h')
        elif letter == 'F':
            newWord.append('j')
        elif letter == 'G':
            newWord.append('S')
        elif letter == 'H':
            newWord.append('M')
        elif letter == 'I':
            newWord.append(' ')
        elif letter == 'J':
            newWord.append('K')
        elif letter == 'K':
            newWord.append('2')
        elif letter == 'L':
            newWord.append('f')
        elif letter == 'M':
            newWord.append('`')
        elif letter == 'N':
            newWord.append('/')
        elif letter == 'O':
            newWord.append('H')
        elif letter == 'P':
            newWord.append('!')
        elif letter == 'Q':
            newWord.append('T')
        elif letter == 'R':
            newWord.append('U')
        elif letter == 'S':
            newWord.append('$')
        elif letter == 'T':
            newWord.append('l')
        elif letter == 'U':
            newWord.append('9')
        elif letter == 'V':
            newWord.append('[')
        elif letter == 'W':
            newWord.append('4')
        elif letter == 'X':
            newWord.append('e')
        elif letter == 'Y':
            newWord.append(':')
        elif letter == 'Z':
            newWord.append('0')
        elif letter == 'a':
            newWord.append('6')
        elif letter == 'b':
            newWord.append('.')
        elif letter == 'c':
            newWord.append('}')
        elif letter == 'd':
            newWord.append('g')
        elif letter == 'e':
            newWord.append('D')
        elif letter == 'f':
            newWord.append('p')
        elif letter == 'g':
            newWord.append('5')
        elif letter == 'h':
            newWord.append('L')
        elif letter == 'i':
            newWord.append(')')
        elif letter == 'j':
            newWord.append('W')
        elif letter == 'k':
            newWord.append('b')
        elif letter == 'l':
            newWord.append('i')
        elif letter == 'm':
            newWord.append('N')
        elif letter == 'n':
            newWord.append('{')
        elif letter == 'o':
            newWord.append('(')
        elif letter == 'p':
            newWord.append('1')
        elif letter == 'q':
            newWord.append('8')
        elif letter == 'r':
            newWord.append('<')
        elif letter == 's':
            newWord.append('v')
        elif letter == 't':
            newWord.append('B')
        elif letter == 'u':
            newWord.append('n')
        elif letter == 'v':
            newWord.append('y')
        elif letter == 'w':
            newWord.append('J')
        elif letter == 'x':
            newWord.append('-')
        elif letter == 'y':
            newWord.append('_')
        elif letter == 'z':
            newWord.append('7')
        elif letter == '1':
            newWord.append(']')
        elif letter == '2':
            newWord.append('k')
        elif letter == '3':
            newWord.append('q')
        elif letter == '4':
            newWord.append('P')
        elif letter == '5':
            newWord.append('Y')
        elif letter == '6':
            newWord.append('F')
        elif letter == '7':
            newWord.append('#')
        elif letter == '8':
            newWord.append('r')
        elif letter == '9':
            newWord.append('>')
        elif letter == '0':
            newWord.append('x')
        elif letter == '!':
            newWord.append('%')
        elif letter == '@':
            newWord.append('R')
        elif letter == '#':
            newWord.append('t')
        elif letter == '$':
            newWord.append('+')
        elif letter == '%':
            newWord.append('X')
        elif letter == '^':
            newWord.append('a')
        elif letter == '&':
            newWord.append('|')
        elif letter == '*':
            newWord.append('u')
        elif letter == '(':
            newWord.append('I')
        elif letter == ')':
            newWord.append('c')
        elif letter == '-':
            newWord.append('w')
        elif letter == '_':
            newWord.append('3')
        elif letter == '+':
            newWord.append('m')
        elif letter == '=':
            newWord.append('*')
        elif letter == '`':
            newWord.append('V')
        elif letter == '~':
            newWord.append('z')
        elif letter == '[':
            newWord.append('@')
        elif letter == ']':
            newWord.append('?')
        elif letter == '{':
            newWord.append('&')
        elif letter == '}':
            newWord.append('G')
        elif letter == '|':
            newWord.append('=')
        elif letter == ':':
            newWord.append('s')
        elif letter == ',':
            newWord.append(',')
        elif letter == '<':
            newWord.append('d')
        elif letter == '.':
            newWord.append('Q')
        elif letter == '>':
            newWord.append('Z')
        elif letter == '/':
            newWord.append('C')
        elif letter == '?':
            newWord.append('A')
        elif letter == ' ':
            newWord.append('o')
    Switched: str  = ''.join(newWord)
    return Switched

def B_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'O':
            newWord.append('A')
        elif letter == 'E':
            newWord.append('B')
        elif letter == '~':
            newWord.append('C')
        elif letter == '^':
            newWord.append('D')
        elif letter == 'h':
            newWord.append('E')
        elif letter == 'j':
            newWord.append('F')
        elif letter == 'S':
            newWord.append('G')
        elif letter == 'M':
            newWord.append('H')
        elif letter == ' ':
            newWord.append('I')
        elif letter == 'K':
            newWord.append('J')
        elif letter == '2':
            newWord.append('K')
        elif letter == 'f':
            newWord.append('L')
        elif letter == '`':
            newWord.append('M')
        elif letter == '/':
            newWord.append('N')
        elif letter == 'H':
            newWord.append('O')
        elif letter == '!':
            newWord.append('P')
        elif letter == 'T':
            newWord.append('Q')
        elif letter == 'U':
            newWord.append('R')
        elif letter == '$':
            newWord.append('S')
        elif letter == 'l':
            newWord.append('T')
        elif letter == '9':
            newWord.append('U')
        elif letter == '[':
            newWord.append('V')
        elif letter == '4':
            newWord.append('W')
        elif letter == 'e':
            newWord.append('X')
        elif letter == ':':
            newWord.append('Y')
        elif letter == '0':
            newWord.append('Z')
        elif letter == '6':
            newWord.append('a')
        elif letter == '.':
            newWord.append('b')
        elif letter == '}':
            newWord.append('c')
        elif letter == 'g':
            newWord.append('d')
        elif letter == 'D':
            newWord.append('e')
        elif letter == 'p':
            newWord.append('f')
        elif letter == '5':
            newWord.append('g')
        elif letter == 'L':
            newWord.append('h')
        elif letter == ')':
            newWord.append('i')
        elif letter == 'W':
            newWord.append('j')
        elif letter == 'b':
            newWord.append('k')
        elif letter == 'i':
            newWord.append('l')
        elif letter == 'N':
            newWord.append('m')
        elif letter == '{':
            newWord.append('n')
        elif letter == '(':
            newWord.append('o')
        elif letter == '1':
            newWord.append('p')
        elif letter == '8':
            newWord.append('q')
        elif letter == '<':
            newWord.append('r')
        elif letter == 'v':
            newWord.append('s')
        elif letter == 'B':
            newWord.append('t')
        elif letter == 'n':
            newWord.append('u')
        elif letter == 'y':
            newWord.append('v')
        elif letter == 'J':
            newWord.append('w')
        elif letter == '-':
            newWord.append('x')
        elif letter == '_':
            newWord.append('y')
        elif letter == '7':
            newWord.append('z')
        elif letter == ']':
            newWord.append('1')
        elif letter == 'k':
            newWord.append('2')
        elif letter == 'q':
            newWord.append('3')
        elif letter == 'P':
            newWord.append('4')
        elif letter == 'Y':
            newWord.append('5')
        elif letter == 'F':
            newWord.append('6')
        elif letter == '#':
            newWord.append('7')
        elif letter == 'r':
            newWord.append('8')
        elif letter == '>':
            newWord.append('9')
        elif letter == 'x':
            newWord.append('0')
        elif letter == '%':
            newWord.append('!')
        elif letter == 'R':
            newWord.append('@')
        elif letter == 't':
            newWord.append('#')
        elif letter == '+':
            newWord.append('$')
        elif letter == 'X':
            newWord.append('%')
        elif letter == 'a':
            newWord.append('^')
        elif letter == '|':
            newWord.append('&')
        elif letter == 'u':
            newWord.append('*')
        elif letter == 'I':
            newWord.append('(')
        elif letter == 'c':
            newWord.append(')')
        elif letter == 'w':
            newWord.append('-')
        elif letter == '3':
            newWord.append('_')
        elif letter == 'm':
            newWord.append('+')
        elif letter == '*':
            newWord.append('=')
        elif letter == 'V':
            newWord.append('`')
        elif letter == 'z':
            newWord.append('~')
        elif letter == '@':
            newWord.append('[')
        elif letter == '?':
            newWord.append(']')
        elif letter == '&':
            newWord.append('{')
        elif letter == 'G':
            newWord.append('}')
        elif letter == '=':
            newWord.append('|')
        elif letter == 's':
            newWord.append(':')
        elif letter == ',':
            newWord.append(',')
        elif letter == 'd':
            newWord.append('<')
        elif letter == 'Q':
            newWord.append('.')
        elif letter == 'Z':
            newWord.append('>')
        elif letter == 'C':
            newWord.append('/')
        elif letter == 'A':
            newWord.append('?')
        elif letter == 'o':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def C_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('A')
        elif letter == 'B':
            newWord.append('t')
        elif letter == 'C':
            newWord.append('@')
        elif letter == 'D':
            newWord.append('4')
        elif letter == 'E':
            newWord.append('|')
        elif letter == 'F':
            newWord.append('r')
        elif letter == 'G':
            newWord.append('p')
        elif letter == 'H':
            newWord.append('Z')
        elif letter == 'I':
            newWord.append(']')
        elif letter == 'J':
            newWord.append('d')
        elif letter == 'K':
            newWord.append('q')
        elif letter == 'L':
            newWord.append('D')
        elif letter == 'M':
            newWord.append('k')
        elif letter == 'N':
            newWord.append('=')
        elif letter == 'O':
            newWord.append('g')
        elif letter == 'P':
            newWord.append('R')
        elif letter == 'Q':
            newWord.append('O')
        elif letter == 'R':
            newWord.append('V')
        elif letter == 'S':
            newWord.append('u')
        elif letter == 'T':
            newWord.append('^')
        elif letter == 'U':
            newWord.append('1')
        elif letter == 'V':
            newWord.append('P')
        elif letter == 'W':
            newWord.append('Y')
        elif letter == 'X':
            newWord.append('0')
        elif letter == 'Y':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append('(')
        elif letter == 'a':
            newWord.append('y')
        elif letter == 'b':
            newWord.append('H')
        elif letter == 'c':
            newWord.append('z')
        elif letter == 'd':
            newWord.append('j')
        elif letter == 'e':
            newWord.append('C')
        elif letter == 'f':
            newWord.append('T')
        elif letter == 'g':
            newWord.append('}')
        elif letter == 'h':
            newWord.append('f')
        elif letter == 'i':
            newWord.append('#')
        elif letter == 'j':
            newWord.append('S')
        elif letter == 'k':
            newWord.append('v')
        elif letter == 'l':
            newWord.append('.')
        elif letter == 'm':
            newWord.append('$')
        elif letter == 'n':
            newWord.append('x')
        elif letter == 'o':
            newWord.append('6')
        elif letter == 'p':
            newWord.append('2')
        elif letter == 'q':
            newWord.append('N')
        elif letter == 'r':
            newWord.append(')')
        elif letter == 's':
            newWord.append('G')
        elif letter == 't':
            newWord.append('+')
        elif letter == 'u':
            newWord.append('I')
        elif letter == 'v':
            newWord.append('%')
        elif letter == 'w':
            newWord.append('L')
        elif letter == 'x':
            newWord.append(',')
        elif letter == 'y':
            newWord.append('5')
        elif letter == 'z':
            newWord.append('e')
        elif letter == '1':
            newWord.append('3')
        elif letter == '2':
            newWord.append('>')
        elif letter == '3':
            newWord.append('X')
        elif letter == '4':
            newWord.append('B')
        elif letter == '5':
            newWord.append('8')
        elif letter == '6':
            newWord.append('W')
        elif letter == '7':
            newWord.append('c')
        elif letter == '8':
            newWord.append('s')
        elif letter == '9':
            newWord.append('/')
        elif letter == '0':
            newWord.append('*')
        elif letter == '!':
            newWord.append('E')
        elif letter == '@':
            newWord.append('-')
        elif letter == '#':
            newWord.append('U')
        elif letter == '$':
            newWord.append('K')
        elif letter == '%':
            newWord.append(':')
        elif letter == '^':
            newWord.append('o')
        elif letter == '&':
            newWord.append('_')
        elif letter == '*':
            newWord.append('i')
        elif letter == '(':
            newWord.append(' ')
        elif letter == ')':
            newWord.append('F')
        elif letter == '-':
            newWord.append('[')
        elif letter == '_':
            newWord.append('7')
        elif letter == '+':
            newWord.append('Q')
        elif letter == '=':
            newWord.append('~')
        elif letter == '`':
            newWord.append('m')
        elif letter == '~':
            newWord.append('9')
        elif letter == '[':
            newWord.append('?')
        elif letter == ']':
            newWord.append('b')
        elif letter == '{':
            newWord.append('h')
        elif letter == '}':
            newWord.append('`')
        elif letter == '|':
            newWord.append('&')
        elif letter == ':':
            newWord.append('{')
        elif letter == ',':
            newWord.append('!')
        elif letter == '<':
            newWord.append('M')
        elif letter == '.':
            newWord.append('<')
        elif letter == '>':
            newWord.append('a')
        elif letter == '/':
            newWord.append('n')
        elif letter == '?':
            newWord.append('J')
        elif letter == ' ':
            newWord.append('l')
    Switched: str  = ''.join(newWord)
    return Switched

def C_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('A')
        elif letter == 't':
            newWord.append('B')
        elif letter == '@':
            newWord.append('C')
        elif letter == '4':
            newWord.append('D')
        elif letter == '|':
            newWord.append('E')
        elif letter == 'r':
            newWord.append('F')
        elif letter == 'p':
            newWord.append('G')
        elif letter == 'Z':
            newWord.append('H')
        elif letter == ']':
            newWord.append('I')
        elif letter == 'd':
            newWord.append('J')
        elif letter == 'q':
            newWord.append('K')
        elif letter == 'D':
            newWord.append('L')
        elif letter == 'k':
            newWord.append('M')
        elif letter == '=':
            newWord.append('N')
        elif letter == 'g':
            newWord.append('O')
        elif letter == 'R':
            newWord.append('P')
        elif letter == 'O':
            newWord.append('Q')
        elif letter == 'V':
            newWord.append('R')
        elif letter == 'u':
            newWord.append('S')
        elif letter == '^':
            newWord.append('T')
        elif letter == '1':
            newWord.append('U')
        elif letter == 'P':
            newWord.append('V')
        elif letter == 'Y':
            newWord.append('W')
        elif letter == '0':
            newWord.append('X')
        elif letter == 'w':
            newWord.append('Y')
        elif letter == '(':
            newWord.append('Z')
        elif letter == 'y':
            newWord.append('a')
        elif letter == 'H':
            newWord.append('b')
        elif letter == 'z':
            newWord.append('c')
        elif letter == 'j':
            newWord.append('d')
        elif letter == 'C':
            newWord.append('e')
        elif letter == 'T':
            newWord.append('f')
        elif letter == '}':
            newWord.append('g')
        elif letter == 'f':
            newWord.append('h')
        elif letter == '#':
            newWord.append('i')
        elif letter == 'S':
            newWord.append('j')
        elif letter == 'v':
            newWord.append('k')
        elif letter == '.':
            newWord.append('l')
        elif letter == '$':
            newWord.append('m')
        elif letter == 'x':
            newWord.append('n')
        elif letter == '6':
            newWord.append('o')
        elif letter == '2':
            newWord.append('p')
        elif letter == 'N':
            newWord.append('q')
        elif letter == ')':
            newWord.append('r')
        elif letter == 'G':
            newWord.append('s')
        elif letter == '+':
            newWord.append('t')
        elif letter == 'I':
            newWord.append('u')
        elif letter == '%':
            newWord.append('v')
        elif letter == 'L':
            newWord.append('w')
        elif letter == ',':
            newWord.append('x')
        elif letter == '5':
            newWord.append('y')
        elif letter == 'e':
            newWord.append('z')
        elif letter == '3':
            newWord.append('1')
        elif letter == '>':
            newWord.append('2')
        elif letter == 'X':
            newWord.append('3')
        elif letter == 'B':
            newWord.append('4')
        elif letter == '8':
            newWord.append('5')
        elif letter == 'W':
            newWord.append('6')
        elif letter == 'c':
            newWord.append('7')
        elif letter == 's':
            newWord.append('8')
        elif letter == '/':
            newWord.append('9')
        elif letter == '*':
            newWord.append('0')
        elif letter == 'E':
            newWord.append('!')
        elif letter == '-':
            newWord.append('@')
        elif letter == 'U':
            newWord.append('#')
        elif letter == 'K':
            newWord.append('$')
        elif letter == ':':
            newWord.append('%')
        elif letter == 'o':
            newWord.append('^')
        elif letter == '_':
            newWord.append('&')
        elif letter == 'i':
            newWord.append('*')
        elif letter == ' ':
            newWord.append('(')
        elif letter == 'F':
            newWord.append(')')
        elif letter == '[':
            newWord.append('-')
        elif letter == '7':
            newWord.append('_')
        elif letter == 'Q':
            newWord.append('+')
        elif letter == '~':
            newWord.append('=')
        elif letter == 'm':
            newWord.append('`')
        elif letter == '9':
            newWord.append('~')
        elif letter == '?':
            newWord.append('[')
        elif letter == 'b':
            newWord.append(']')
        elif letter == 'h':
            newWord.append('{')
        elif letter == '`':
            newWord.append('}')
        elif letter == '&':
            newWord.append('|')
        elif letter == '{':
            newWord.append(':')
        elif letter == '!':
            newWord.append(',')
        elif letter == 'M':
            newWord.append('<')
        elif letter == '<':
            newWord.append('.')
        elif letter == 'a':
            newWord.append('>')
        elif letter == 'n':
            newWord.append('/')
        elif letter == 'J':
            newWord.append('?')
        elif letter == 'l':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def D_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append(']')
        elif letter == 'B':
            newWord.append('w')
        elif letter == 'C':
            newWord.append('l')
        elif letter == 'D':
            newWord.append('*')
        elif letter == 'E':
            newWord.append('S')
        elif letter == 'F':
            newWord.append('y')
        elif letter == 'G':
            newWord.append('N')
        elif letter == 'H':
            newWord.append('/')
        elif letter == 'I':
            newWord.append('a')
        elif letter == 'J':
            newWord.append('%')
        elif letter == 'K':
            newWord.append('0')
        elif letter == 'L':
            newWord.append('r')
        elif letter == 'M':
            newWord.append('X')
        elif letter == 'N':
            newWord.append('}')
        elif letter == 'O':
            newWord.append('G')
        elif letter == 'P':
            newWord.append('m')
        elif letter == 'Q':
            newWord.append('e')
        elif letter == 'R':
            newWord.append('&')
        elif letter == 'S':
            newWord.append('K')
        elif letter == 'T':
            newWord.append('F')
        elif letter == 'U':
            newWord.append('O')
        elif letter == 'V':
            newWord.append('V')
        elif letter == 'W':
            newWord.append('+')
        elif letter == 'X':
            newWord.append('o')
        elif letter == 'Y':
            newWord.append('U')
        elif letter == 'Z':
            newWord.append('E')
        elif letter == 'a':
            newWord.append('$')
        elif letter == 'b':
            newWord.append('Z')
        elif letter == 'c':
            newWord.append('#')
        elif letter == 'd':
            newWord.append('5')
        elif letter == 'e':
            newWord.append('M')
        elif letter == 'f':
            newWord.append('J')
        elif letter == 'g':
            newWord.append('Q')
        elif letter == 'h':
            newWord.append('I')
        elif letter == 'i':
            newWord.append('9')
        elif letter == 'j':
            newWord.append('>')
        elif letter == 'k':
            newWord.append('4')
        elif letter == 'l':
            newWord.append('C')
        elif letter == 'm':
            newWord.append(',')
        elif letter == 'n':
            newWord.append(':')
        elif letter == 'o':
            newWord.append('T')
        elif letter == 'p':
            newWord.append('^')
        elif letter == 'q':
            newWord.append('~')
        elif letter == 'r':
            newWord.append('c')
        elif letter == 's':
            newWord.append('_')
        elif letter == 't':
            newWord.append('f')
        elif letter == 'u':
            newWord.append('6')
        elif letter == 'v':
            newWord.append('u')
        elif letter == 'w':
            newWord.append('d')
        elif letter == 'x':
            newWord.append('-')
        elif letter == 'y':
            newWord.append('D')
        elif letter == 'z':
            newWord.append('g')
        elif letter == '1':
            newWord.append('q')
        elif letter == '2':
            newWord.append('=')
        elif letter == '3':
            newWord.append('(')
        elif letter == '4':
            newWord.append('p')
        elif letter == '5':
            newWord.append('j')
        elif letter == '6':
            newWord.append('t')
        elif letter == '7':
            newWord.append('i')
        elif letter == '8':
            newWord.append('<')
        elif letter == '9':
            newWord.append('h')
        elif letter == '0':
            newWord.append('[')
        elif letter == '!':
            newWord.append('L')
        elif letter == '@':
            newWord.append('Y')
        elif letter == '#':
            newWord.append('!')
        elif letter == '$':
            newWord.append('W')
        elif letter == '%':
            newWord.append('.')
        elif letter == '^':
            newWord.append('n')
        elif letter == '&':
            newWord.append('8')
        elif letter == '*':
            newWord.append('z')
        elif letter == '(':
            newWord.append('?')
        elif letter == ')':
            newWord.append('B')
        elif letter == '-':
            newWord.append('x')
        elif letter == '_':
            newWord.append('{')
        elif letter == '+':
            newWord.append('s')
        elif letter == '=':
            newWord.append('3')
        elif letter == '`':
            newWord.append('|')
        elif letter == '~':
            newWord.append(')')
        elif letter == '[':
            newWord.append('1')
        elif letter == ']':
            newWord.append('P')
        elif letter == '{':
            newWord.append('v')
        elif letter == '}':
            newWord.append('k')
        elif letter == '|':
            newWord.append('H')
        elif letter == ':':
            newWord.append('2')
        elif letter == ',':
            newWord.append('R')
        elif letter == '<':
            newWord.append('7')
        elif letter == '.':
            newWord.append('A')
        elif letter == '>':
            newWord.append('`')
        elif letter == '/':
            newWord.append('@')
        elif letter == '?':
            newWord.append(' ')
        elif letter == ' ':
            newWord.append('b')
    Switched: str  = ''.join(newWord)
    return Switched

def D_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == ']':
            newWord.append('A')
        elif letter == 'w':
            newWord.append('B')
        elif letter == 'l':
            newWord.append('C')
        elif letter == '*':
            newWord.append('D')
        elif letter == 'S':
            newWord.append('E')
        elif letter == 'y':
            newWord.append('F')
        elif letter == 'N':
            newWord.append('G')
        elif letter == '/':
            newWord.append('H')
        elif letter == 'a':
            newWord.append('I')
        elif letter == '%':
            newWord.append('J')
        elif letter == '0':
            newWord.append('K')
        elif letter == 'r':
            newWord.append('L')
        elif letter == 'X':
            newWord.append('M')
        elif letter == '}':
            newWord.append('N')
        elif letter == 'G':
            newWord.append('O')
        elif letter == 'm':
            newWord.append('P')
        elif letter == 'e':
            newWord.append('Q')
        elif letter == '&':
            newWord.append('R')
        elif letter == 'K':
            newWord.append('S')
        elif letter == 'F':
            newWord.append('T')
        elif letter == 'O':
            newWord.append('U')
        elif letter == 'V':
            newWord.append('V')
        elif letter == '+':
            newWord.append('W')
        elif letter == 'o':
            newWord.append('X')
        elif letter == 'U':
            newWord.append('Y')
        elif letter == 'E':
            newWord.append('Z')
        elif letter == '$':
            newWord.append('a')
        elif letter == 'Z':
            newWord.append('b')
        elif letter == '#':
            newWord.append('c')
        elif letter == '5':
            newWord.append('d')
        elif letter == 'M':
            newWord.append('e')
        elif letter == 'J':
            newWord.append('f')
        elif letter == 'Q':
            newWord.append('g')
        elif letter == 'I':
            newWord.append('h')
        elif letter == '9':
            newWord.append('i')
        elif letter == '>':
            newWord.append('j')
        elif letter == '4':
            newWord.append('k')
        elif letter == 'C':
            newWord.append('l')
        elif letter == ',':
            newWord.append('m')
        elif letter == ':':
            newWord.append('n')
        elif letter == 'T':
            newWord.append('o')
        elif letter == '^':
            newWord.append('p')
        elif letter == '~':
            newWord.append('q')
        elif letter == 'c':
            newWord.append('r')
        elif letter == '_':
            newWord.append('s')
        elif letter == 'f':
            newWord.append('t')
        elif letter == '6':
            newWord.append('u')
        elif letter == 'u':
            newWord.append('v')
        elif letter == 'd':
            newWord.append('w')
        elif letter == '-':
            newWord.append('x')
        elif letter == 'D':
            newWord.append('y')
        elif letter == 'g':
            newWord.append('z')
        elif letter == 'q':
            newWord.append('1')
        elif letter == '=':
            newWord.append('2')
        elif letter == '(':
            newWord.append('3')
        elif letter == 'p':
            newWord.append('4')
        elif letter == 'j':
            newWord.append('5')
        elif letter == 't':
            newWord.append('6')
        elif letter == 'i':
            newWord.append('7')
        elif letter == '<':
            newWord.append('8')
        elif letter == 'h':
            newWord.append('9')
        elif letter == '[':
            newWord.append('0')
        elif letter == 'L':
            newWord.append('!')
        elif letter == 'Y':
            newWord.append('@')
        elif letter == '!':
            newWord.append('#')
        elif letter == 'W':
            newWord.append('$')
        elif letter == '.':
            newWord.append('%')
        elif letter == 'n':
            newWord.append('^')
        elif letter == '8':
            newWord.append('&')
        elif letter == 'z':
            newWord.append('*')
        elif letter == '?':
            newWord.append('(')
        elif letter == 'B':
            newWord.append(')')
        elif letter == 'x':
            newWord.append('-')
        elif letter == '{':
            newWord.append('_')
        elif letter == 's':
            newWord.append('+')
        elif letter == '3':
            newWord.append('=')
        elif letter == '|':
            newWord.append('`')
        elif letter == ')':
            newWord.append('~')
        elif letter == '1':
            newWord.append('[')
        elif letter == 'P':
            newWord.append(']')
        elif letter == 'v':
            newWord.append('{')
        elif letter == 'k':
            newWord.append('}')
        elif letter == 'H':
            newWord.append('|')
        elif letter == '2':
            newWord.append(':')
        elif letter == 'R':
            newWord.append(',')
        elif letter == '7':
            newWord.append('<')
        elif letter == 'A':
            newWord.append('.')
        elif letter == '`':
            newWord.append('>')
        elif letter == '@':
            newWord.append('/')
        elif letter == ' ':
            newWord.append('?')
        elif letter == 'b':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def E_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('l')
        elif letter == 'B':
            newWord.append('_')
        elif letter == 'C':
            newWord.append('e')
        elif letter == 'D':
            newWord.append(')')
        elif letter == 'E':
            newWord.append('3')
        elif letter == 'F':
            newWord.append('m')
        elif letter == 'G':
            newWord.append('d')
        elif letter == 'H':
            newWord.append('o')
        elif letter == 'I':
            newWord.append('^')
        elif letter == 'J':
            newWord.append('r')
        elif letter == 'K':
            newWord.append('!')
        elif letter == 'L':
            newWord.append('C')
        elif letter == 'M':
            newWord.append('+')
        elif letter == 'N':
            newWord.append('Y')
        elif letter == 'O':
            newWord.append('K')
        elif letter == 'P':
            newWord.append('b')
        elif letter == 'Q':
            newWord.append('/')
        elif letter == 'R':
            newWord.append('8')
        elif letter == 'S':
            newWord.append('X')
        elif letter == 'T':
            newWord.append('}')
        elif letter == 'U':
            newWord.append('u')
        elif letter == 'V':
            newWord.append('N')
        elif letter == 'W':
            newWord.append('I')
        elif letter == 'X':
            newWord.append('H')
        elif letter == 'Y':
            newWord.append('q')
        elif letter == 'Z':
            newWord.append('a')
        elif letter == 'a':
            newWord.append('J')
        elif letter == 'b':
            newWord.append('>')
        elif letter == 'c':
            newWord.append('W')
        elif letter == 'd':
            newWord.append('<')
        elif letter == 'e':
            newWord.append(' ')
        elif letter == 'f':
            newWord.append('t')
        elif letter == 'g':
            newWord.append('=')
        elif letter == 'h':
            newWord.append('s')
        elif letter == 'i':
            newWord.append('z')
        elif letter == 'j':
            newWord.append('p')
        elif letter == 'k':
            newWord.append('P')
        elif letter == 'l':
            newWord.append('[')
        elif letter == 'm':
            newWord.append('(')
        elif letter == 'n':
            newWord.append('9')
        elif letter == 'o':
            newWord.append(']')
        elif letter == 'p':
            newWord.append('w')
        elif letter == 'q':
            newWord.append('2')
        elif letter == 'r':
            newWord.append('F')
        elif letter == 's':
            newWord.append('-')
        elif letter == 't':
            newWord.append('#')
        elif letter == 'u':
            newWord.append('g')
        elif letter == 'v':
            newWord.append('f')
        elif letter == 'w':
            newWord.append(',')
        elif letter == 'x':
            newWord.append('Z')
        elif letter == 'y':
            newWord.append('n')
        elif letter == 'z':
            newWord.append('7')
        elif letter == '1':
            newWord.append('4')
        elif letter == '2':
            newWord.append('&')
        elif letter == '3':
            newWord.append('`')
        elif letter == '4':
            newWord.append('{')
        elif letter == '5':
            newWord.append('0')
        elif letter == '6':
            newWord.append('5')
        elif letter == '7':
            newWord.append('%')
        elif letter == '8':
            newWord.append('V')
        elif letter == '9':
            newWord.append('i')
        elif letter == '0':
            newWord.append('h')
        elif letter == '!':
            newWord.append('y')
        elif letter == '@':
            newWord.append('M')
        elif letter == '#':
            newWord.append('?')
        elif letter == '$':
            newWord.append('S')
        elif letter == '%':
            newWord.append('1')
        elif letter == '^':
            newWord.append('~')
        elif letter == '&':
            newWord.append('D')
        elif letter == '*':
            newWord.append('T')
        elif letter == '(':
            newWord.append('G')
        elif letter == ')':
            newWord.append('|')
        elif letter == '-':
            newWord.append('Q')
        elif letter == '_':
            newWord.append('.')
        elif letter == '+':
            newWord.append('R')
        elif letter == '=':
            newWord.append('U')
        elif letter == '`':
            newWord.append('*')
        elif letter == '~':
            newWord.append('E')
        elif letter == '[':
            newWord.append('A')
        elif letter == ']':
            newWord.append('x')
        elif letter == '{':
            newWord.append(':')
        elif letter == '}':
            newWord.append('B')
        elif letter == '|':
            newWord.append('6')
        elif letter == ':':
            newWord.append('L')
        elif letter == ',':
            newWord.append('k')
        elif letter == '<':
            newWord.append('j')
        elif letter == '.':
            newWord.append('v')
        elif letter == '>':
            newWord.append('$')
        elif letter == '/':
            newWord.append('@')
        elif letter == '?':
            newWord.append('c')
        elif letter == ' ':
            newWord.append('O')
    Switched: str  = ''.join(newWord)
    return Switched

def E_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'l':
            newWord.append('A')
        elif letter == '_':
            newWord.append('B')
        elif letter == 'e':
            newWord.append('C')
        elif letter == ')':
            newWord.append('D')
        elif letter == '3':
            newWord.append('E')
        elif letter == 'm':
            newWord.append('F')
        elif letter == 'd':
            newWord.append('G')
        elif letter == 'o':
            newWord.append('H')
        elif letter == '^':
            newWord.append('I')
        elif letter == 'r':
            newWord.append('J')
        elif letter == '!':
            newWord.append('K')
        elif letter == 'C':
            newWord.append('L')
        elif letter == '+':
            newWord.append('M')
        elif letter == 'Y':
            newWord.append('N')
        elif letter == 'K':
            newWord.append('O')
        elif letter == 'b':
            newWord.append('P')
        elif letter == '/':
            newWord.append('Q')
        elif letter == '8':
            newWord.append('R')
        elif letter == 'X':
            newWord.append('S')
        elif letter == '}':
            newWord.append('T')
        elif letter == 'u':
            newWord.append('U')
        elif letter == 'N':
            newWord.append('V')
        elif letter == 'I':
            newWord.append('W')
        elif letter == 'H':
            newWord.append('X')
        elif letter == 'q':
            newWord.append('Y')
        elif letter == 'a':
            newWord.append('Z')
        elif letter == 'J':
            newWord.append('a')
        elif letter == '>':
            newWord.append('b')
        elif letter == 'W':
            newWord.append('c')
        elif letter == '<':
            newWord.append('d')
        elif letter == ' ':
            newWord.append('e')
        elif letter == 't':
            newWord.append('f')
        elif letter == '=':
            newWord.append('g')
        elif letter == 's':
            newWord.append('h')
        elif letter == 'z':
            newWord.append('i')
        elif letter == 'p':
            newWord.append('j')
        elif letter == 'P':
            newWord.append('k')
        elif letter == '[':
            newWord.append('l')
        elif letter == '(':
            newWord.append('m')
        elif letter == '9':
            newWord.append('n')
        elif letter == ']':
            newWord.append('o')
        elif letter == 'w':
            newWord.append('p')
        elif letter == '2':
            newWord.append('q')
        elif letter == 'F':
            newWord.append('r')
        elif letter == '-':
            newWord.append('s')
        elif letter == '#':
            newWord.append('t')
        elif letter == 'g':
            newWord.append('u')
        elif letter == 'f':
            newWord.append('v')
        elif letter == ',':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append('x')
        elif letter == 'n':
            newWord.append('y')
        elif letter == '7':
            newWord.append('z')
        elif letter == '4':
            newWord.append('1')
        elif letter == '&':
            newWord.append('2')
        elif letter == '`':
            newWord.append('3')
        elif letter == '{':
            newWord.append('4')
        elif letter == '0':
            newWord.append('5')
        elif letter == '5':
            newWord.append('6')
        elif letter == '%':
            newWord.append('7')
        elif letter == 'V':
            newWord.append('8')
        elif letter == 'i':
            newWord.append('9')
        elif letter == 'h':
            newWord.append('0')
        elif letter == 'y':
            newWord.append('!')
        elif letter == 'M':
            newWord.append('@')
        elif letter == '?':
            newWord.append('#')
        elif letter == 'S':
            newWord.append('$')
        elif letter == '1':
            newWord.append('%')
        elif letter == '~':
            newWord.append('^')
        elif letter == 'D':
            newWord.append('&')
        elif letter == 'T':
            newWord.append('*')
        elif letter == 'G':
            newWord.append('(')
        elif letter == '|':
            newWord.append(')')
        elif letter == 'Q':
            newWord.append('-')
        elif letter == '.':
            newWord.append('_')
        elif letter == 'R':
            newWord.append('+')
        elif letter == 'U':
            newWord.append('=')
        elif letter == '*':
            newWord.append('`')
        elif letter == 'E':
            newWord.append('~')
        elif letter == 'A':
            newWord.append('[')
        elif letter == 'x':
            newWord.append(']')
        elif letter == ':':
            newWord.append('{')
        elif letter == 'B':
            newWord.append('}')
        elif letter == '6':
            newWord.append('|')
        elif letter == 'L':
            newWord.append(':')
        elif letter == 'k':
            newWord.append(',')
        elif letter == 'j':
            newWord.append('<')
        elif letter == 'v':
            newWord.append('.')
        elif letter == '$':
            newWord.append('>')
        elif letter == '@':
            newWord.append('/')
        elif letter == 'c':
            newWord.append('?')
        elif letter == 'O':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def F_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('?')
        elif letter == 'B':
            newWord.append('M')
        elif letter == 'C':
            newWord.append('c')
        elif letter == 'D':
            newWord.append('[')
        elif letter == 'E':
            newWord.append('3')
        elif letter == 'F':
            newWord.append('v')
        elif letter == 'G':
            newWord.append('S')
        elif letter == 'H':
            newWord.append('>')
        elif letter == 'I':
            newWord.append('K')
        elif letter == 'J':
            newWord.append('z')
        elif letter == 'K':
            newWord.append('2')
        elif letter == 'L':
            newWord.append('q')
        elif letter == 'M':
            newWord.append('`')
        elif letter == 'N':
            newWord.append('$')
        elif letter == 'O':
            newWord.append('R')
        elif letter == 'P':
            newWord.append('F')
        elif letter == 'Q':
            newWord.append('e')
        elif letter == 'R':
            newWord.append('U')
        elif letter == 'S':
            newWord.append('%')
        elif letter == 'T':
            newWord.append('H')
        elif letter == 'U':
            newWord.append('#')
        elif letter == 'V':
            newWord.append('t')
        elif letter == 'W':
            newWord.append(']')
        elif letter == 'X':
            newWord.append('+')
        elif letter == 'Y':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append('b')
        elif letter == 'a':
            newWord.append('f')
        elif letter == 'b':
            newWord.append(')')
        elif letter == 'c':
            newWord.append('l')
        elif letter == 'd':
            newWord.append('!')
        elif letter == 'e':
            newWord.append('i')
        elif letter == 'f':
            newWord.append('L')
        elif letter == 'g':
            newWord.append('T')
        elif letter == 'h':
            newWord.append('n')
        elif letter == 'i':
            newWord.append('A')
        elif letter == 'j':
            newWord.append('r')
        elif letter == 'k':
            newWord.append('4')
        elif letter == 'l':
            newWord.append('(')
        elif letter == 'm':
            newWord.append('X')
        elif letter == 'n':
            newWord.append('*')
        elif letter == 'o':
            newWord.append('o')
        elif letter == 'p':
            newWord.append('.')
        elif letter == 'q':
            newWord.append('J')
        elif letter == 'r':
            newWord.append('D')
        elif letter == 's':
            newWord.append('_')
        elif letter == 't':
            newWord.append('j')
        elif letter == 'u':
            newWord.append('O')
        elif letter == 'v':
            newWord.append(':')
        elif letter == 'w':
            newWord.append('&')
        elif letter == 'x':
            newWord.append('x')
        elif letter == 'y':
            newWord.append('^')
        elif letter == 'z':
            newWord.append('/')
        elif letter == '1':
            newWord.append('W')
        elif letter == '2':
            newWord.append('<')
        elif letter == '3':
            newWord.append('=')
        elif letter == '4':
            newWord.append('1')
        elif letter == '5':
            newWord.append('Q')
        elif letter == '6':
            newWord.append('m')
        elif letter == '7':
            newWord.append('8')
        elif letter == '8':
            newWord.append('6')
        elif letter == '9':
            newWord.append('7')
        elif letter == '0':
            newWord.append('V')
        elif letter == '!':
            newWord.append('0')
        elif letter == '@':
            newWord.append('p')
        elif letter == '#':
            newWord.append('k')
        elif letter == '$':
            newWord.append('y')
        elif letter == '%':
            newWord.append('@')
        elif letter == '^':
            newWord.append('d')
        elif letter == '&':
            newWord.append('~')
        elif letter == '*':
            newWord.append(',')
        elif letter == '(':
            newWord.append('G')
        elif letter == ')':
            newWord.append('h')
        elif letter == '-':
            newWord.append('{')
        elif letter == '_':
            newWord.append(' ')
        elif letter == '+':
            newWord.append('Y')
        elif letter == '=':
            newWord.append('a')
        elif letter == '`':
            newWord.append('B')
        elif letter == '~':
            newWord.append('Z')
        elif letter == '[':
            newWord.append('9')
        elif letter == ']':
            newWord.append('u')
        elif letter == '{':
            newWord.append('C')
        elif letter == '}':
            newWord.append('5')
        elif letter == '|':
            newWord.append('s')
        elif letter == ':':
            newWord.append('g')
        elif letter == ',':
            newWord.append('N')
        elif letter == '<':
            newWord.append('|')
        elif letter == '.':
            newWord.append('}')
        elif letter == '>':
            newWord.append('-')
        elif letter == '/':
            newWord.append('E')
        elif letter == '?':
            newWord.append('I')
        elif letter == ' ':
            newWord.append('P')
    Switched: str  = ''.join(newWord)
    return Switched

def F_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '?':
            newWord.append('A')
        elif letter == 'M':
            newWord.append('B')
        elif letter == 'c':
            newWord.append('C')
        elif letter == '[':
            newWord.append('D')
        elif letter == '3':
            newWord.append('E')
        elif letter == 'v':
            newWord.append('F')
        elif letter == 'S':
            newWord.append('G')
        elif letter == '>':
            newWord.append('H')
        elif letter == 'K':
            newWord.append('I')
        elif letter == 'z':
            newWord.append('J')
        elif letter == '2':
            newWord.append('K')
        elif letter == 'q':
            newWord.append('L')
        elif letter == '`':
            newWord.append('M')
        elif letter == '$':
            newWord.append('N')
        elif letter == 'R':
            newWord.append('O')
        elif letter == 'F':
            newWord.append('P')
        elif letter == 'e':
            newWord.append('Q')
        elif letter == 'U':
            newWord.append('R')
        elif letter == '%':
            newWord.append('S')
        elif letter == 'H':
            newWord.append('T')
        elif letter == '#':
            newWord.append('U')
        elif letter == 't':
            newWord.append('V')
        elif letter == ']':
            newWord.append('W')
        elif letter == '+':
            newWord.append('X')
        elif letter == 'w':
            newWord.append('Y')
        elif letter == 'b':
            newWord.append('Z')
        elif letter == 'f':
            newWord.append('a')
        elif letter == ')':
            newWord.append('b')
        elif letter == 'l':
            newWord.append('c')
        elif letter == '!':
            newWord.append('d')
        elif letter == 'i':
            newWord.append('e')
        elif letter == 'L':
            newWord.append('f')
        elif letter == 'T':
            newWord.append('g')
        elif letter == 'n':
            newWord.append('h')
        elif letter == 'A':
            newWord.append('i')
        elif letter == 'r':
            newWord.append('j')
        elif letter == '4':
            newWord.append('k')
        elif letter == '(':
            newWord.append('l')
        elif letter == 'X':
            newWord.append('m')
        elif letter == '*':
            newWord.append('n')
        elif letter == 'o':
            newWord.append('o')
        elif letter == '.':
            newWord.append('p')
        elif letter == 'J':
            newWord.append('q')
        elif letter == 'D':
            newWord.append('r')
        elif letter == '_':
            newWord.append('s')
        elif letter == 'j':
            newWord.append('t')
        elif letter == 'O':
            newWord.append('u')
        elif letter == ':':
            newWord.append('v')
        elif letter == '&':
            newWord.append('w')
        elif letter == 'x':
            newWord.append('x')
        elif letter == '^':
            newWord.append('y')
        elif letter == '/':
            newWord.append('z')
        elif letter == 'W':
            newWord.append('1')
        elif letter == '<':
            newWord.append('2')
        elif letter == '=':
            newWord.append('3')
        elif letter == '1':
            newWord.append('4')
        elif letter == 'Q':
            newWord.append('5')
        elif letter == 'm':
            newWord.append('6')
        elif letter == '8':
            newWord.append('7')
        elif letter == '6':
            newWord.append('8')
        elif letter == '7':
            newWord.append('9')
        elif letter == 'V':
            newWord.append('0')
        elif letter == '0':
            newWord.append('!')
        elif letter == 'p':
            newWord.append('@')
        elif letter == 'k':
            newWord.append('#')
        elif letter == 'y':
            newWord.append('$')
        elif letter == '@':
            newWord.append('%')
        elif letter == 'd':
            newWord.append('^')
        elif letter == '~':
            newWord.append('&')
        elif letter == ',':
            newWord.append('*')
        elif letter == 'G':
            newWord.append('(')
        elif letter == 'h':
            newWord.append(')')
        elif letter == '{':
            newWord.append('-')
        elif letter == ' ':
            newWord.append('_')
        elif letter == 'Y':
            newWord.append('+')
        elif letter == 'a':
            newWord.append('=')
        elif letter == 'B':
            newWord.append('`')
        elif letter == 'Z':
            newWord.append('~')
        elif letter == '9':
            newWord.append('[')
        elif letter == 'u':
            newWord.append(']')
        elif letter == 'C':
            newWord.append('{')
        elif letter == '5':
            newWord.append('}')
        elif letter == 's':
            newWord.append('|')
        elif letter == 'g':
            newWord.append(':')
        elif letter == 'N':
            newWord.append(',')
        elif letter == '|':
            newWord.append('<')
        elif letter == '}':
            newWord.append('.')
        elif letter == '-':
            newWord.append('>')
        elif letter == 'E':
            newWord.append('/')
        elif letter == 'I':
            newWord.append('?')
        elif letter == 'P':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def G_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('`')
        elif letter == 'B':
            newWord.append('M')
        elif letter == 'C':
            newWord.append('<')
        elif letter == 'D':
            newWord.append('T')
        elif letter == 'E':
            newWord.append('%')
        elif letter == 'F':
            newWord.append('*')
        elif letter == 'G':
            newWord.append('O')
        elif letter == 'H':
            newWord.append('S')
        elif letter == 'I':
            newWord.append('e')
        elif letter == 'J':
            newWord.append('X')
        elif letter == 'K':
            newWord.append('n')
        elif letter == 'L':
            newWord.append('E')
        elif letter == 'M':
            newWord.append('H')
        elif letter == 'N':
            newWord.append('7')
        elif letter == 'O':
            newWord.append('}')
        elif letter == 'P':
            newWord.append('Q')
        elif letter == 'Q':
            newWord.append(']')
        elif letter == 'R':
            newWord.append('K')
        elif letter == 'S':
            newWord.append('0')
        elif letter == 'T':
            newWord.append('[')
        elif letter == 'U':
            newWord.append(')')
        elif letter == 'V':
            newWord.append('J')
        elif letter == 'W':
            newWord.append('6')
        elif letter == 'X':
            newWord.append('@')
        elif letter == 'Y':
            newWord.append('F')
        elif letter == 'Z':
            newWord.append('z')
        elif letter == 'a':
            newWord.append(':')
        elif letter == 'b':
            newWord.append('j')
        elif letter == 'c':
            newWord.append('A')
        elif letter == 'd':
            newWord.append('w')
        elif letter == 'e':
            newWord.append('Z')
        elif letter == 'f':
            newWord.append('8')
        elif letter == 'g':
            newWord.append('u')
        elif letter == 'h':
            newWord.append('$')
        elif letter == 'i':
            newWord.append('Y')
        elif letter == 'j':
            newWord.append('R')
        elif letter == 'k':
            newWord.append('.')
        elif letter == 'l':
            newWord.append('m')
        elif letter == 'm':
            newWord.append('D')
        elif letter == 'n':
            newWord.append('s')
        elif letter == 'o':
            newWord.append('l')
        elif letter == 'p':
            newWord.append('V')
        elif letter == 'q':
            newWord.append('|')
        elif letter == 'r':
            newWord.append('5')
        elif letter == 's':
            newWord.append('3')
        elif letter == 't':
            newWord.append('P')
        elif letter == 'u':
            newWord.append('q')
        elif letter == 'v':
            newWord.append('C')
        elif letter == 'w':
            newWord.append('/')
        elif letter == 'x':
            newWord.append('c')
        elif letter == 'y':
            newWord.append('N')
        elif letter == 'z':
            newWord.append('d')
        elif letter == '1':
            newWord.append('h')
        elif letter == '2':
            newWord.append('x')
        elif letter == '3':
            newWord.append('1')
        elif letter == '4':
            newWord.append('L')
        elif letter == '5':
            newWord.append('2')
        elif letter == '6':
            newWord.append('W')
        elif letter == '7':
            newWord.append(' ')
        elif letter == '8':
            newWord.append('=')
        elif letter == '9':
            newWord.append('#')
        elif letter == '0':
            newWord.append('?')
        elif letter == '!':
            newWord.append('_')
        elif letter == '@':
            newWord.append('G')
        elif letter == '#':
            newWord.append('a')
        elif letter == '$':
            newWord.append('9')
        elif letter == '%':
            newWord.append('g')
        elif letter == '^':
            newWord.append('i')
        elif letter == '&':
            newWord.append('~')
        elif letter == '*':
            newWord.append('U')
        elif letter == '(':
            newWord.append('o')
        elif letter == ')':
            newWord.append('4')
        elif letter == '-':
            newWord.append('r')
        elif letter == '_':
            newWord.append('b')
        elif letter == '+':
            newWord.append('I')
        elif letter == '=':
            newWord.append('y')
        elif letter == '`':
            newWord.append('^')
        elif letter == '~':
            newWord.append('+')
        elif letter == '[':
            newWord.append('>')
        elif letter == ']':
            newWord.append('k')
        elif letter == '{':
            newWord.append('B')
        elif letter == '}':
            newWord.append('f')
        elif letter == '|':
            newWord.append('p')
        elif letter == ':':
            newWord.append(',')
        elif letter == ',':
            newWord.append('v')
        elif letter == '<':
            newWord.append('&')
        elif letter == '.':
            newWord.append('{')
        elif letter == '>':
            newWord.append('t')
        elif letter == '/':
            newWord.append('(')
        elif letter == '?':
            newWord.append('!')
        elif letter == ' ':
            newWord.append('-')
    Switched: str  = ''.join(newWord)
    return Switched

def G_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '`':
            newWord.append('A')
        elif letter == 'M':
            newWord.append('B')
        elif letter == '<':
            newWord.append('C')
        elif letter == 'T':
            newWord.append('D')
        elif letter == '%':
            newWord.append('E')
        elif letter == '*':
            newWord.append('F')
        elif letter == 'O':
            newWord.append('G')
        elif letter == 'S':
            newWord.append('H')
        elif letter == 'e':
            newWord.append('I')
        elif letter == 'X':
            newWord.append('J')
        elif letter == 'n':
            newWord.append('K')
        elif letter == 'E':
            newWord.append('L')
        elif letter == 'H':
            newWord.append('M')
        elif letter == '7':
            newWord.append('N')
        elif letter == '}':
            newWord.append('O')
        elif letter == 'Q':
            newWord.append('P')
        elif letter == ']':
            newWord.append('Q')
        elif letter == 'K':
            newWord.append('R')
        elif letter == '0':
            newWord.append('S')
        elif letter == '[':
            newWord.append('T')
        elif letter == ')':
            newWord.append('U')
        elif letter == 'J':
            newWord.append('V')
        elif letter == '6':
            newWord.append('W')
        elif letter == '@':
            newWord.append('X')
        elif letter == 'F':
            newWord.append('Y')
        elif letter == 'z':
            newWord.append('Z')
        elif letter == ':':
            newWord.append('a')
        elif letter == 'j':
            newWord.append('b')
        elif letter == 'A':
            newWord.append('c')
        elif letter == 'w':
            newWord.append('d')
        elif letter == 'Z':
            newWord.append('e')
        elif letter == '8':
            newWord.append('f')
        elif letter == 'u':
            newWord.append('g')
        elif letter == '$':
            newWord.append('h')
        elif letter == 'Y':
            newWord.append('i')
        elif letter == 'R':
            newWord.append('j')
        elif letter == '.':
            newWord.append('k')
        elif letter == 'm':
            newWord.append('l')
        elif letter == 'D':
            newWord.append('m')
        elif letter == 's':
            newWord.append('n')
        elif letter == 'l':
            newWord.append('o')
        elif letter == 'V':
            newWord.append('p')
        elif letter == '|':
            newWord.append('q')
        elif letter == '5':
            newWord.append('r')
        elif letter == '3':
            newWord.append('s')
        elif letter == 'P':
            newWord.append('t')
        elif letter == 'q':
            newWord.append('u')
        elif letter == 'C':
            newWord.append('v')
        elif letter == '/':
            newWord.append('w')
        elif letter == 'c':
            newWord.append('x')
        elif letter == 'N':
            newWord.append('y')
        elif letter == 'd':
            newWord.append('z')
        elif letter == 'h':
            newWord.append('1')
        elif letter == 'x':
            newWord.append('2')
        elif letter == '1':
            newWord.append('3')
        elif letter == 'L':
            newWord.append('4')
        elif letter == '2':
            newWord.append('5')
        elif letter == 'W':
            newWord.append('6')
        elif letter == ' ':
            newWord.append('7')
        elif letter == '=':
            newWord.append('8')
        elif letter == '#':
            newWord.append('9')
        elif letter == '?':
            newWord.append('0')
        elif letter == '_':
            newWord.append('!')
        elif letter == 'G':
            newWord.append('@')
        elif letter == 'a':
            newWord.append('#')
        elif letter == '9':
            newWord.append('$')
        elif letter == 'g':
            newWord.append('%')
        elif letter == 'i':
            newWord.append('^')
        elif letter == '~':
            newWord.append('&')
        elif letter == 'U':
            newWord.append('*')
        elif letter == 'o':
            newWord.append('(')
        elif letter == '4':
            newWord.append(')')
        elif letter == 'r':
            newWord.append('-')
        elif letter == 'b':
            newWord.append('_')
        elif letter == 'I':
            newWord.append('+')
        elif letter == 'y':
            newWord.append('=')
        elif letter == '^':
            newWord.append('`')
        elif letter == '+':
            newWord.append('~')
        elif letter == '>':
            newWord.append('[')
        elif letter == 'k':
            newWord.append(']')
        elif letter == 'B':
            newWord.append('{')
        elif letter == 'f':
            newWord.append('}')
        elif letter == 'p':
            newWord.append('|')
        elif letter == ',':
            newWord.append(':')
        elif letter == 'v':
            newWord.append(',')
        elif letter == '&':
            newWord.append('<')
        elif letter == '{':
            newWord.append('.')
        elif letter == 't':
            newWord.append('>')
        elif letter == '(':
            newWord.append('/')
        elif letter == '!':
            newWord.append('?')
        elif letter == '-':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def H_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('T')
        elif letter == 'B':
            newWord.append('y')
        elif letter == 'C':
            newWord.append('3')
        elif letter == 'D':
            newWord.append('C')
        elif letter == 'E':
            newWord.append('M')
        elif letter == 'F':
            newWord.append('2')
        elif letter == 'G':
            newWord.append('=')
        elif letter == 'H':
            newWord.append('#')
        elif letter == 'I':
            newWord.append('6')
        elif letter == 'J':
            newWord.append('q')
        elif letter == 'K':
            newWord.append(']')
        elif letter == 'L':
            newWord.append('_')
        elif letter == 'M':
            newWord.append('d')
        elif letter == 'N':
            newWord.append('0')
        elif letter == 'O':
            newWord.append('m')
        elif letter == 'P':
            newWord.append('Q')
        elif letter == 'Q':
            newWord.append('z')
        elif letter == 'R':
            newWord.append('+')
        elif letter == 'S':
            newWord.append('.')
        elif letter == 'T':
            newWord.append('P')
        elif letter == 'U':
            newWord.append('/')
        elif letter == 'V':
            newWord.append('7')
        elif letter == 'W':
            newWord.append('K')
        elif letter == 'X':
            newWord.append('p')
        elif letter == 'Y':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append('1')
        elif letter == 'a':
            newWord.append('H')
        elif letter == 'b':
            newWord.append('%')
        elif letter == 'c':
            newWord.append('~')
        elif letter == 'd':
            newWord.append('k')
        elif letter == 'e':
            newWord.append('x')
        elif letter == 'f':
            newWord.append('$')
        elif letter == 'g':
            newWord.append('g')
        elif letter == 'h':
            newWord.append('B')
        elif letter == 'i':
            newWord.append('-')
        elif letter == 'j':
            newWord.append(':')
        elif letter == 'k':
            newWord.append('*')
        elif letter == 'l':
            newWord.append('o')
        elif letter == 'm':
            newWord.append('U')
        elif letter == 'n':
            newWord.append('i')
        elif letter == 'o':
            newWord.append('b')
        elif letter == 'p':
            newWord.append('t')
        elif letter == 'q':
            newWord.append('R')
        elif letter == 'r':
            newWord.append('@')
        elif letter == 's':
            newWord.append('V')
        elif letter == 't':
            newWord.append('E')
        elif letter == 'u':
            newWord.append('F')
        elif letter == 'v':
            newWord.append('v')
        elif letter == 'w':
            newWord.append('f')
        elif letter == 'x':
            newWord.append('9')
        elif letter == 'y':
            newWord.append('n')
        elif letter == 'z':
            newWord.append('?')
        elif letter == '1':
            newWord.append('I')
        elif letter == '2':
            newWord.append(' ')
        elif letter == '3':
            newWord.append('&')
        elif letter == '4':
            newWord.append('N')
        elif letter == '5':
            newWord.append('Z')
        elif letter == '6':
            newWord.append('{')
        elif letter == '7':
            newWord.append('8')
        elif letter == '8':
            newWord.append('S')
        elif letter == '9':
            newWord.append('|')
        elif letter == '0':
            newWord.append('j')
        elif letter == '!':
            newWord.append('O')
        elif letter == '@':
            newWord.append('s')
        elif letter == '#':
            newWord.append('W')
        elif letter == '$':
            newWord.append('h')
        elif letter == '%':
            newWord.append('G')
        elif letter == '^':
            newWord.append(')')
        elif letter == '&':
            newWord.append('}')
        elif letter == '*':
            newWord.append('<')
        elif letter == '(':
            newWord.append('l')
        elif letter == ')':
            newWord.append('5')
        elif letter == '-':
            newWord.append('r')
        elif letter == '_':
            newWord.append('4')
        elif letter == '+':
            newWord.append('e')
        elif letter == '=':
            newWord.append('a')
        elif letter == '`':
            newWord.append('J')
        elif letter == '~':
            newWord.append('A')
        elif letter == '[':
            newWord.append('^')
        elif letter == ']':
            newWord.append('(')
        elif letter == '{':
            newWord.append('L')
        elif letter == '}':
            newWord.append('c')
        elif letter == '|':
            newWord.append(',')
        elif letter == ':':
            newWord.append('u')
        elif letter == ',':
            newWord.append('Y')
        elif letter == '<':
            newWord.append('D')
        elif letter == '.':
            newWord.append('X')
        elif letter == '>':
            newWord.append('[')
        elif letter == '/':
            newWord.append('>')
        elif letter == '?':
            newWord.append('!')
        elif letter == ' ':
            newWord.append('`')
    Switched: str  = ''.join(newWord)
    return Switched

def H_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'T':
            newWord.append('A')
        elif letter == 'y':
            newWord.append('B')
        elif letter == '3':
            newWord.append('C')
        elif letter == 'C':
            newWord.append('D')
        elif letter == 'M':
            newWord.append('E')
        elif letter == '2':
            newWord.append('F')
        elif letter == '=':
            newWord.append('G')
        elif letter == '#':
            newWord.append('H')
        elif letter == '6':
            newWord.append('I')
        elif letter == 'q':
            newWord.append('J')
        elif letter == ']':
            newWord.append('K')
        elif letter == '_':
            newWord.append('L')
        elif letter == 'd':
            newWord.append('M')
        elif letter == '0':
            newWord.append('N')
        elif letter == 'm':
            newWord.append('O')
        elif letter == 'Q':
            newWord.append('P')
        elif letter == 'z':
            newWord.append('Q')
        elif letter == '+':
            newWord.append('R')
        elif letter == '.':
            newWord.append('S')
        elif letter == 'P':
            newWord.append('T')
        elif letter == '/':
            newWord.append('U')
        elif letter == '7':
            newWord.append('V')
        elif letter == 'K':
            newWord.append('W')
        elif letter == 'p':
            newWord.append('X')
        elif letter == 'w':
            newWord.append('Y')
        elif letter == '1':
            newWord.append('Z')
        elif letter == 'H':
            newWord.append('a')
        elif letter == '%':
            newWord.append('b')
        elif letter == '~':
            newWord.append('c')
        elif letter == 'k':
            newWord.append('d')
        elif letter == 'x':
            newWord.append('e')
        elif letter == '$':
            newWord.append('f')
        elif letter == 'g':
            newWord.append('g')
        elif letter == 'B':
            newWord.append('h')
        elif letter == '-':
            newWord.append('i')
        elif letter == ':':
            newWord.append('j')
        elif letter == '*':
            newWord.append('k')
        elif letter == 'o':
            newWord.append('l')
        elif letter == 'U':
            newWord.append('m')
        elif letter == 'i':
            newWord.append('n')
        elif letter == 'b':
            newWord.append('o')
        elif letter == 't':
            newWord.append('p')
        elif letter == 'R':
            newWord.append('q')
        elif letter == '@':
            newWord.append('r')
        elif letter == 'V':
            newWord.append('s')
        elif letter == 'E':
            newWord.append('t')
        elif letter == 'F':
            newWord.append('u')
        elif letter == 'v':
            newWord.append('v')
        elif letter == 'f':
            newWord.append('w')
        elif letter == '9':
            newWord.append('x')
        elif letter == 'n':
            newWord.append('y')
        elif letter == '?':
            newWord.append('z')
        elif letter == 'I':
            newWord.append('1')
        elif letter == ' ':
            newWord.append('2')
        elif letter == '&':
            newWord.append('3')
        elif letter == 'N':
            newWord.append('4')
        elif letter == 'Z':
            newWord.append('5')
        elif letter == '{':
            newWord.append('6')
        elif letter == '8':
            newWord.append('7')
        elif letter == 'S':
            newWord.append('8')
        elif letter == '|':
            newWord.append('9')
        elif letter == 'j':
            newWord.append('0')
        elif letter == 'O':
            newWord.append('!')
        elif letter == 's':
            newWord.append('@')
        elif letter == 'W':
            newWord.append('#')
        elif letter == 'h':
            newWord.append('$')
        elif letter == 'G':
            newWord.append('%')
        elif letter == ')':
            newWord.append('^')
        elif letter == '}':
            newWord.append('&')
        elif letter == '<':
            newWord.append('*')
        elif letter == 'l':
            newWord.append('(')
        elif letter == '5':
            newWord.append(')')
        elif letter == 'r':
            newWord.append('-')
        elif letter == '4':
            newWord.append('_')
        elif letter == 'e':
            newWord.append('+')
        elif letter == 'a':
            newWord.append('=')
        elif letter == 'J':
            newWord.append('`')
        elif letter == 'A':
            newWord.append('~')
        elif letter == '^':
            newWord.append('[')
        elif letter == '(':
            newWord.append(']')
        elif letter == 'L':
            newWord.append('{')
        elif letter == 'c':
            newWord.append('}')
        elif letter == ',':
            newWord.append('|')
        elif letter == 'u':
            newWord.append(':')
        elif letter == 'Y':
            newWord.append(',')
        elif letter == 'D':
            newWord.append('<')
        elif letter == 'X':
            newWord.append('.')
        elif letter == '[':
            newWord.append('>')
        elif letter == '>':
            newWord.append('/')
        elif letter == '!':
            newWord.append('?')
        elif letter == '`':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def I_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append(')')
        elif letter == 'B':
            newWord.append('l')
        elif letter == 'C':
            newWord.append('u')
        elif letter == 'D':
            newWord.append('C')
        elif letter == 'E':
            newWord.append('@')
        elif letter == 'F':
            newWord.append('s')
        elif letter == 'G':
            newWord.append('z')
        elif letter == 'H':
            newWord.append('h')
        elif letter == 'I':
            newWord.append('(')
        elif letter == 'J':
            newWord.append('*')
        elif letter == 'K':
            newWord.append('x')
        elif letter == 'L':
            newWord.append('7')
        elif letter == 'M':
            newWord.append('W')
        elif letter == 'N':
            newWord.append('r')
        elif letter == 'O':
            newWord.append('!')
        elif letter == 'P':
            newWord.append('Z')
        elif letter == 'Q':
            newWord.append('1')
        elif letter == 'R':
            newWord.append('M')
        elif letter == 'S':
            newWord.append('a')
        elif letter == 'T':
            newWord.append('Q')
        elif letter == 'U':
            newWord.append('[')
        elif letter == 'V':
            newWord.append('N')
        elif letter == 'W':
            newWord.append('R')
        elif letter == 'X':
            newWord.append('-')
        elif letter == 'Y':
            newWord.append('d')
        elif letter == 'Z':
            newWord.append('E')
        elif letter == 'a':
            newWord.append('y')
        elif letter == 'b':
            newWord.append('j')
        elif letter == 'c':
            newWord.append('P')
        elif letter == 'd':
            newWord.append('g')
        elif letter == 'e':
            newWord.append('q')
        elif letter == 'f':
            newWord.append('|')
        elif letter == 'g':
            newWord.append('%')
        elif letter == 'h':
            newWord.append('O')
        elif letter == 'i':
            newWord.append('G')
        elif letter == 'j':
            newWord.append('4')
        elif letter == 'k':
            newWord.append('b')
        elif letter == 'l':
            newWord.append('$')
        elif letter == 'm':
            newWord.append('}')
        elif letter == 'n':
            newWord.append('/')
        elif letter == 'o':
            newWord.append(':')
        elif letter == 'p':
            newWord.append('2')
        elif letter == 'q':
            newWord.append('T')
        elif letter == 'r':
            newWord.append('X')
        elif letter == 's':
            newWord.append('<')
        elif letter == 't':
            newWord.append('&')
        elif letter == 'u':
            newWord.append('o')
        elif letter == 'v':
            newWord.append('_')
        elif letter == 'w':
            newWord.append('c')
        elif letter == 'x':
            newWord.append('D')
        elif letter == 'y':
            newWord.append('m')
        elif letter == 'z':
            newWord.append('K')
        elif letter == '1':
            newWord.append('`')
        elif letter == '2':
            newWord.append('^')
        elif letter == '3':
            newWord.append('5')
        elif letter == '4':
            newWord.append(',')
        elif letter == '5':
            newWord.append('V')
        elif letter == '6':
            newWord.append('=')
        elif letter == '7':
            newWord.append('k')
        elif letter == '8':
            newWord.append('?')
        elif letter == '9':
            newWord.append('L')
        elif letter == '0':
            newWord.append('U')
        elif letter == '!':
            newWord.append('H')
        elif letter == '@':
            newWord.append('{')
        elif letter == '#':
            newWord.append('F')
        elif letter == '$':
            newWord.append('A')
        elif letter == '%':
            newWord.append('#')
        elif letter == '^':
            newWord.append('3')
        elif letter == '&':
            newWord.append('p')
        elif letter == '*':
            newWord.append('Y')
        elif letter == '(':
            newWord.append('v')
        elif letter == ')':
            newWord.append('.')
        elif letter == '-':
            newWord.append('9')
        elif letter == '_':
            newWord.append('f')
        elif letter == '+':
            newWord.append('J')
        elif letter == '=':
            newWord.append('i')
        elif letter == '`':
            newWord.append('>')
        elif letter == '~':
            newWord.append('S')
        elif letter == '[':
            newWord.append(']')
        elif letter == ']':
            newWord.append('~')
        elif letter == '{':
            newWord.append('e')
        elif letter == '}':
            newWord.append('I')
        elif letter == '|':
            newWord.append(' ')
        elif letter == ':':
            newWord.append('B')
        elif letter == ',':
            newWord.append('t')
        elif letter == '<':
            newWord.append('6')
        elif letter == '.':
            newWord.append('0')
        elif letter == '>':
            newWord.append('+')
        elif letter == '/':
            newWord.append('n')
        elif letter == '?':
            newWord.append('8')
        elif letter == ' ':
            newWord.append('w')
    Switched: str  = ''.join(newWord)
    return Switched

def I_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == ')':
            newWord.append('A')
        elif letter == 'l':
            newWord.append('B')
        elif letter == 'u':
            newWord.append('C')
        elif letter == 'C':
            newWord.append('D')
        elif letter == '@':
            newWord.append('E')
        elif letter == 's':
            newWord.append('F')
        elif letter == 'z':
            newWord.append('G')
        elif letter == 'h':
            newWord.append('H')
        elif letter == '(':
            newWord.append('I')
        elif letter == '*':
            newWord.append('J')
        elif letter == 'x':
            newWord.append('K')
        elif letter == '7':
            newWord.append('L')
        elif letter == 'W':
            newWord.append('M')
        elif letter == 'r':
            newWord.append('N')
        elif letter == '!':
            newWord.append('O')
        elif letter == 'Z':
            newWord.append('P')
        elif letter == '1':
            newWord.append('Q')
        elif letter == 'M':
            newWord.append('R')
        elif letter == 'a':
            newWord.append('S')
        elif letter == 'Q':
            newWord.append('T')
        elif letter == '[':
            newWord.append('U')
        elif letter == 'N':
            newWord.append('V')
        elif letter == 'R':
            newWord.append('W')
        elif letter == '-':
            newWord.append('X')
        elif letter == 'd':
            newWord.append('Y')
        elif letter == 'E':
            newWord.append('Z')
        elif letter == 'y':
            newWord.append('a')
        elif letter == 'j':
            newWord.append('b')
        elif letter == 'P':
            newWord.append('c')
        elif letter == 'g':
            newWord.append('d')
        elif letter == 'q':
            newWord.append('e')
        elif letter == '|':
            newWord.append('f')
        elif letter == '%':
            newWord.append('g')
        elif letter == 'O':
            newWord.append('h')
        elif letter == 'G':
            newWord.append('i')
        elif letter == '4':
            newWord.append('j')
        elif letter == 'b':
            newWord.append('k')
        elif letter == '$':
            newWord.append('l')
        elif letter == '}':
            newWord.append('m')
        elif letter == '/':
            newWord.append('n')
        elif letter == ':':
            newWord.append('o')
        elif letter == '2':
            newWord.append('p')
        elif letter == 'T':
            newWord.append('q')
        elif letter == 'X':
            newWord.append('r')
        elif letter == '<':
            newWord.append('s')
        elif letter == '&':
            newWord.append('t')
        elif letter == 'o':
            newWord.append('u')
        elif letter == '_':
            newWord.append('v')
        elif letter == 'c':
            newWord.append('w')
        elif letter == 'D':
            newWord.append('x')
        elif letter == 'm':
            newWord.append('y')
        elif letter == 'K':
            newWord.append('z')
        elif letter == '`':
            newWord.append('1')
        elif letter == '^':
            newWord.append('2')
        elif letter == '5':
            newWord.append('3')
        elif letter == ',':
            newWord.append('4')
        elif letter == 'V':
            newWord.append('5')
        elif letter == '=':
            newWord.append('6')
        elif letter == 'k':
            newWord.append('7')
        elif letter == '?':
            newWord.append('8')
        elif letter == 'L':
            newWord.append('9')
        elif letter == 'U':
            newWord.append('0')
        elif letter == 'H':
            newWord.append('!')
        elif letter == '{':
            newWord.append('@')
        elif letter == 'F':
            newWord.append('#')
        elif letter == 'A':
            newWord.append('$')
        elif letter == '#':
            newWord.append('%')
        elif letter == '3':
            newWord.append('^')
        elif letter == 'p':
            newWord.append('&')
        elif letter == 'Y':
            newWord.append('*')
        elif letter == 'v':
            newWord.append('(')
        elif letter == '.':
            newWord.append(')')
        elif letter == '9':
            newWord.append('-')
        elif letter == 'f':
            newWord.append('_')
        elif letter == 'J':
            newWord.append('+')
        elif letter == 'i':
            newWord.append('=')
        elif letter == '>':
            newWord.append('`')
        elif letter == 'S':
            newWord.append('~')
        elif letter == ']':
            newWord.append('[')
        elif letter == '~':
            newWord.append(']')
        elif letter == 'e':
            newWord.append('{')
        elif letter == 'I':
            newWord.append('}')
        elif letter == ' ':
            newWord.append('|')
        elif letter == 'B':
            newWord.append(':')
        elif letter == 't':
            newWord.append(',')
        elif letter == '6':
            newWord.append('<')
        elif letter == '0':
            newWord.append('.')
        elif letter == '+':
            newWord.append('>')
        elif letter == 'n':
            newWord.append('/')
        elif letter == '8':
            newWord.append('?')
        elif letter == 'w':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def J_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('l')
        elif letter == 'B':
            newWord.append(']')
        elif letter == 'C':
            newWord.append('Z')
        elif letter == 'D':
            newWord.append('V')
        elif letter == 'E':
            newWord.append('9')
        elif letter == 'F':
            newWord.append('%')
        elif letter == 'G':
            newWord.append('R')
        elif letter == 'H':
            newWord.append('B')
        elif letter == 'I':
            newWord.append('P')
        elif letter == 'J':
            newWord.append('u')
        elif letter == 'K':
            newWord.append('t')
        elif letter == 'L':
            newWord.append('6')
        elif letter == 'M':
            newWord.append('N')
        elif letter == 'N':
            newWord.append('X')
        elif letter == 'O':
            newWord.append('M')
        elif letter == 'P':
            newWord.append(',')
        elif letter == 'Q':
            newWord.append(' ')
        elif letter == 'R':
            newWord.append('s')
        elif letter == 'S':
            newWord.append('7')
        elif letter == 'T':
            newWord.append('g')
        elif letter == 'U':
            newWord.append('d')
        elif letter == 'V':
            newWord.append('e')
        elif letter == 'W':
            newWord.append('v')
        elif letter == 'X':
            newWord.append('T')
        elif letter == 'Y':
            newWord.append(':')
        elif letter == 'Z':
            newWord.append('r')
        elif letter == 'a':
            newWord.append('2')
        elif letter == 'b':
            newWord.append('D')
        elif letter == 'c':
            newWord.append('}')
        elif letter == 'd':
            newWord.append('x')
        elif letter == 'e':
            newWord.append('@')
        elif letter == 'f':
            newWord.append('|')
        elif letter == 'g':
            newWord.append('Y')
        elif letter == 'h':
            newWord.append('~')
        elif letter == 'i':
            newWord.append('m')
        elif letter == 'j':
            newWord.append('O')
        elif letter == 'k':
            newWord.append('w')
        elif letter == 'l':
            newWord.append('I')
        elif letter == 'm':
            newWord.append('c')
        elif letter == 'n':
            newWord.append('U')
        elif letter == 'o':
            newWord.append('.')
        elif letter == 'p':
            newWord.append('8')
        elif letter == 'q':
            newWord.append('f')
        elif letter == 'r':
            newWord.append('^')
        elif letter == 's':
            newWord.append('(')
        elif letter == 't':
            newWord.append('*')
        elif letter == 'u':
            newWord.append('0')
        elif letter == 'v':
            newWord.append('<')
        elif letter == 'w':
            newWord.append('L')
        elif letter == 'x':
            newWord.append('$')
        elif letter == 'y':
            newWord.append('q')
        elif letter == 'z':
            newWord.append('>')
        elif letter == '1':
            newWord.append('G')
        elif letter == '2':
            newWord.append('/')
        elif letter == '3':
            newWord.append('3')
        elif letter == '4':
            newWord.append('o')
        elif letter == '5':
            newWord.append('=')
        elif letter == '6':
            newWord.append('S')
        elif letter == '7':
            newWord.append('C')
        elif letter == '8':
            newWord.append('[')
        elif letter == '9':
            newWord.append('k')
        elif letter == '0':
            newWord.append('H')
        elif letter == '!':
            newWord.append('j')
        elif letter == '@':
            newWord.append('Q')
        elif letter == '#':
            newWord.append('{')
        elif letter == '$':
            newWord.append(')')
        elif letter == '%':
            newWord.append('_')
        elif letter == '^':
            newWord.append('J')
        elif letter == '&':
            newWord.append('h')
        elif letter == '*':
            newWord.append('`')
        elif letter == '(':
            newWord.append('z')
        elif letter == ')':
            newWord.append('y')
        elif letter == '-':
            newWord.append('5')
        elif letter == '_':
            newWord.append('!')
        elif letter == '+':
            newWord.append('W')
        elif letter == '=':
            newWord.append('i')
        elif letter == '`':
            newWord.append('E')
        elif letter == '~':
            newWord.append('b')
        elif letter == '[':
            newWord.append('-')
        elif letter == ']':
            newWord.append('p')
        elif letter == '{':
            newWord.append('A')
        elif letter == '}':
            newWord.append('n')
        elif letter == '|':
            newWord.append('F')
        elif letter == ':':
            newWord.append('#')
        elif letter == ',':
            newWord.append('4')
        elif letter == '<':
            newWord.append('K')
        elif letter == '.':
            newWord.append('&')
        elif letter == '>':
            newWord.append('+')
        elif letter == '/':
            newWord.append('1')
        elif letter == '?':
            newWord.append('?')
        elif letter == ' ':
            newWord.append('a')
    Switched: str  = ''.join(newWord)
    return Switched

def J_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'l':
            newWord.append('A')
        elif letter == ']':
            newWord.append('B')
        elif letter == 'Z':
            newWord.append('C')
        elif letter == 'V':
            newWord.append('D')
        elif letter == '9':
            newWord.append('E')
        elif letter == '%':
            newWord.append('F')
        elif letter == 'R':
            newWord.append('G')
        elif letter == 'B':
            newWord.append('H')
        elif letter == 'P':
            newWord.append('I')
        elif letter == 'u':
            newWord.append('J')
        elif letter == 't':
            newWord.append('K')
        elif letter == '6':
            newWord.append('L')
        elif letter == 'N':
            newWord.append('M')
        elif letter == 'X':
            newWord.append('N')
        elif letter == 'M':
            newWord.append('O')
        elif letter == ',':
            newWord.append('P')
        elif letter == ' ':
            newWord.append('Q')
        elif letter == 's':
            newWord.append('R')
        elif letter == '7':
            newWord.append('S')
        elif letter == 'g':
            newWord.append('T')
        elif letter == 'd':
            newWord.append('U')
        elif letter == 'e':
            newWord.append('V')
        elif letter == 'v':
            newWord.append('W')
        elif letter == 'T':
            newWord.append('X')
        elif letter == ':':
            newWord.append('Y')
        elif letter == 'r':
            newWord.append('Z')
        elif letter == '2':
            newWord.append('a')
        elif letter == 'D':
            newWord.append('b')
        elif letter == '}':
            newWord.append('c')
        elif letter == 'x':
            newWord.append('d')
        elif letter == '@':
            newWord.append('e')
        elif letter == '|':
            newWord.append('f')
        elif letter == 'Y':
            newWord.append('g')
        elif letter == '~':
            newWord.append('h')
        elif letter == 'm':
            newWord.append('i')
        elif letter == 'O':
            newWord.append('j')
        elif letter == 'w':
            newWord.append('k')
        elif letter == 'I':
            newWord.append('l')
        elif letter == 'c':
            newWord.append('m')
        elif letter == 'U':
            newWord.append('n')
        elif letter == '.':
            newWord.append('o')
        elif letter == '8':
            newWord.append('p')
        elif letter == 'f':
            newWord.append('q')
        elif letter == '^':
            newWord.append('r')
        elif letter == '(':
            newWord.append('s')
        elif letter == '*':
            newWord.append('t')
        elif letter == '0':
            newWord.append('u')
        elif letter == '<':
            newWord.append('v')
        elif letter == 'L':
            newWord.append('w')
        elif letter == '$':
            newWord.append('x')
        elif letter == 'q':
            newWord.append('y')
        elif letter == '>':
            newWord.append('z')
        elif letter == 'G':
            newWord.append('1')
        elif letter == '/':
            newWord.append('2')
        elif letter == '3':
            newWord.append('3')
        elif letter == 'o':
            newWord.append('4')
        elif letter == '=':
            newWord.append('5')
        elif letter == 'S':
            newWord.append('6')
        elif letter == 'C':
            newWord.append('7')
        elif letter == '[':
            newWord.append('8')
        elif letter == 'k':
            newWord.append('9')
        elif letter == 'H':
            newWord.append('0')
        elif letter == 'j':
            newWord.append('!')
        elif letter == 'Q':
            newWord.append('@')
        elif letter == '{':
            newWord.append('#')
        elif letter == ')':
            newWord.append('$')
        elif letter == '_':
            newWord.append('%')
        elif letter == 'J':
            newWord.append('^')
        elif letter == 'h':
            newWord.append('&')
        elif letter == '`':
            newWord.append('*')
        elif letter == 'z':
            newWord.append('(')
        elif letter == 'y':
            newWord.append(')')
        elif letter == '5':
            newWord.append('-')
        elif letter == '!':
            newWord.append('_')
        elif letter == 'W':
            newWord.append('+')
        elif letter == 'i':
            newWord.append('=')
        elif letter == 'E':
            newWord.append('`')
        elif letter == 'b':
            newWord.append('~')
        elif letter == '-':
            newWord.append('[')
        elif letter == 'p':
            newWord.append(']')
        elif letter == 'A':
            newWord.append('{')
        elif letter == 'n':
            newWord.append('}')
        elif letter == 'F':
            newWord.append('|')
        elif letter == '#':
            newWord.append(':')
        elif letter == '4':
            newWord.append(',')
        elif letter == 'K':
            newWord.append('<')
        elif letter == '&':
            newWord.append('.')
        elif letter == '+':
            newWord.append('>')
        elif letter == '1':
            newWord.append('/')
        elif letter == '?':
            newWord.append('?')
        elif letter == 'a':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def K_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('8')
        elif letter == 'B':
            newWord.append('9')
        elif letter == 'C':
            newWord.append('o')
        elif letter == 'D':
            newWord.append('p')
        elif letter == 'E':
            newWord.append('g')
        elif letter == 'F':
            newWord.append('6')
        elif letter == 'G':
            newWord.append('A')
        elif letter == 'H':
            newWord.append('I')
        elif letter == 'I':
            newWord.append('Q')
        elif letter == 'J':
            newWord.append('0')
        elif letter == 'K':
            newWord.append('%')
        elif letter == 'L':
            newWord.append('3')
        elif letter == 'M':
            newWord.append('d')
        elif letter == 'N':
            newWord.append('U')
        elif letter == 'O':
            newWord.append('x')
        elif letter == 'P':
            newWord.append('c')
        elif letter == 'Q':
            newWord.append('E')
        elif letter == 'R':
            newWord.append('/')
        elif letter == 'S':
            newWord.append('&')
        elif letter == 'T':
            newWord.append('B')
        elif letter == 'U':
            newWord.append('a')
        elif letter == 'V':
            newWord.append('2')
        elif letter == 'W':
            newWord.append('$')
        elif letter == 'X':
            newWord.append('r')
        elif letter == 'Y':
            newWord.append('J')
        elif letter == 'Z':
            newWord.append(' ')
        elif letter == 'a':
            newWord.append('*')
        elif letter == 'b':
            newWord.append('W')
        elif letter == 'c':
            newWord.append('i')
        elif letter == 'd':
            newWord.append(']')
        elif letter == 'e':
            newWord.append('G')
        elif letter == 'f':
            newWord.append('X')
        elif letter == 'g':
            newWord.append('q')
        elif letter == 'h':
            newWord.append('z')
        elif letter == 'i':
            newWord.append('V')
        elif letter == 'j':
            newWord.append(',')
        elif letter == 'k':
            newWord.append('-')
        elif letter == 'l':
            newWord.append('7')
        elif letter == 'm':
            newWord.append('K')
        elif letter == 'n':
            newWord.append(')')
        elif letter == 'o':
            newWord.append('^')
        elif letter == 'p':
            newWord.append('4')
        elif letter == 'q':
            newWord.append(':')
        elif letter == 'r':
            newWord.append('H')
        elif letter == 's':
            newWord.append('h')
        elif letter == 't':
            newWord.append('e')
        elif letter == 'u':
            newWord.append('1')
        elif letter == 'v':
            newWord.append('+')
        elif letter == 'w':
            newWord.append('_')
        elif letter == 'x':
            newWord.append('M')
        elif letter == 'y':
            newWord.append('<')
        elif letter == 'z':
            newWord.append('F')
        elif letter == '1':
            newWord.append('#')
        elif letter == '2':
            newWord.append('}')
        elif letter == '3':
            newWord.append('N')
        elif letter == '4':
            newWord.append('v')
        elif letter == '5':
            newWord.append('>')
        elif letter == '6':
            newWord.append('t')
        elif letter == '7':
            newWord.append('{')
        elif letter == '8':
            newWord.append('S')
        elif letter == '9':
            newWord.append('f')
        elif letter == '0':
            newWord.append('y')
        elif letter == '!':
            newWord.append('(')
        elif letter == '@':
            newWord.append('~')
        elif letter == '#':
            newWord.append('5')
        elif letter == '$':
            newWord.append('D')
        elif letter == '%':
            newWord.append('@')
        elif letter == '^':
            newWord.append('`')
        elif letter == '&':
            newWord.append('w')
        elif letter == '*':
            newWord.append('O')
        elif letter == '(':
            newWord.append('s')
        elif letter == ')':
            newWord.append('n')
        elif letter == '-':
            newWord.append('=')
        elif letter == '_':
            newWord.append('?')
        elif letter == '+':
            newWord.append('[')
        elif letter == '=':
            newWord.append('Z')
        elif letter == '`':
            newWord.append('!')
        elif letter == '~':
            newWord.append('C')
        elif letter == '[':
            newWord.append('R')
        elif letter == ']':
            newWord.append('m')
        elif letter == '{':
            newWord.append('Y')
        elif letter == '}':
            newWord.append('b')
        elif letter == '|':
            newWord.append('|')
        elif letter == ':':
            newWord.append('l')
        elif letter == ',':
            newWord.append('j')
        elif letter == '<':
            newWord.append('.')
        elif letter == '.':
            newWord.append('k')
        elif letter == '>':
            newWord.append('T')
        elif letter == '/':
            newWord.append('u')
        elif letter == '?':
            newWord.append('P')
        elif letter == ' ':
            newWord.append('L')
    Switched: str  = ''.join(newWord)
    return Switched

def K_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '8':
            newWord.append('A')
        elif letter == '9':
            newWord.append('B')
        elif letter == 'o':
            newWord.append('C')
        elif letter == 'p':
            newWord.append('D')
        elif letter == 'g':
            newWord.append('E')
        elif letter == '6':
            newWord.append('F')
        elif letter == 'A':
            newWord.append('G')
        elif letter == 'I':
            newWord.append('H')
        elif letter == 'Q':
            newWord.append('I')
        elif letter == '0':
            newWord.append('J')
        elif letter == '%':
            newWord.append('K')
        elif letter == '3':
            newWord.append('L')
        elif letter == 'd':
            newWord.append('M')
        elif letter == 'U':
            newWord.append('N')
        elif letter == 'x':
            newWord.append('O')
        elif letter == 'c':
            newWord.append('P')
        elif letter == 'E':
            newWord.append('Q')
        elif letter == '/':
            newWord.append('R')
        elif letter == '&':
            newWord.append('S')
        elif letter == 'B':
            newWord.append('T')
        elif letter == 'a':
            newWord.append('U')
        elif letter == '2':
            newWord.append('V')
        elif letter == '$':
            newWord.append('W')
        elif letter == 'r':
            newWord.append('X')
        elif letter == 'J':
            newWord.append('Y')
        elif letter == ' ':
            newWord.append('Z')
        elif letter == '*':
            newWord.append('a')
        elif letter == 'W':
            newWord.append('b')
        elif letter == 'i':
            newWord.append('c')
        elif letter == ']':
            newWord.append('d')
        elif letter == 'G':
            newWord.append('e')
        elif letter == 'X':
            newWord.append('f')
        elif letter == 'q':
            newWord.append('g')
        elif letter == 'z':
            newWord.append('h')
        elif letter == 'V':
            newWord.append('i')
        elif letter == ',':
            newWord.append('j')
        elif letter == '-':
            newWord.append('k')
        elif letter == '7':
            newWord.append('l')
        elif letter == 'K':
            newWord.append('m')
        elif letter == ')':
            newWord.append('n')
        elif letter == '^':
            newWord.append('o')
        elif letter == '4':
            newWord.append('p')
        elif letter == ':':
            newWord.append('q')
        elif letter == 'H':
            newWord.append('r')
        elif letter == 'h':
            newWord.append('s')
        elif letter == 'e':
            newWord.append('t')
        elif letter == '1':
            newWord.append('u')
        elif letter == '+':
            newWord.append('v')
        elif letter == '_':
            newWord.append('w')
        elif letter == 'M':
            newWord.append('x')
        elif letter == '<':
            newWord.append('y')
        elif letter == 'F':
            newWord.append('z')
        elif letter == '#':
            newWord.append('1')
        elif letter == '}':
            newWord.append('2')
        elif letter == 'N':
            newWord.append('3')
        elif letter == 'v':
            newWord.append('4')
        elif letter == '>':
            newWord.append('5')
        elif letter == 't':
            newWord.append('6')
        elif letter == '{':
            newWord.append('7')
        elif letter == 'S':
            newWord.append('8')
        elif letter == 'f':
            newWord.append('9')
        elif letter == 'y':
            newWord.append('0')
        elif letter == '(':
            newWord.append('!')
        elif letter == '~':
            newWord.append('@')
        elif letter == '5':
            newWord.append('#')
        elif letter == 'D':
            newWord.append('$')
        elif letter == '@':
            newWord.append('%')
        elif letter == '`':
            newWord.append('^')
        elif letter == 'w':
            newWord.append('&')
        elif letter == 'O':
            newWord.append('*')
        elif letter == 's':
            newWord.append('(')
        elif letter == 'n':
            newWord.append(')')
        elif letter == '=':
            newWord.append('-')
        elif letter == '?':
            newWord.append('_')
        elif letter == '[':
            newWord.append('+')
        elif letter == 'Z':
            newWord.append('=')
        elif letter == '!':
            newWord.append('`')
        elif letter == 'C':
            newWord.append('~')
        elif letter == 'R':
            newWord.append('[')
        elif letter == 'm':
            newWord.append(']')
        elif letter == 'Y':
            newWord.append('{')
        elif letter == 'b':
            newWord.append('}')
        elif letter == '|':
            newWord.append('|')
        elif letter == 'l':
            newWord.append(':')
        elif letter == 'j':
            newWord.append(',')
        elif letter == '.':
            newWord.append('<')
        elif letter == 'k':
            newWord.append('.')
        elif letter == 'T':
            newWord.append('>')
        elif letter == 'u':
            newWord.append('/')
        elif letter == 'P':
            newWord.append('?')
        elif letter == 'L':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def L_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('P')
        elif letter == 'B':
            newWord.append('p')
        elif letter == 'C':
            newWord.append('Z')
        elif letter == 'D':
            newWord.append('v')
        elif letter == 'E':
            newWord.append('Y')
        elif letter == 'F':
            newWord.append('x')
        elif letter == 'G':
            newWord.append('L')
        elif letter == 'H':
            newWord.append('0')
        elif letter == 'I':
            newWord.append('=')
        elif letter == 'J':
            newWord.append(')')
        elif letter == 'K':
            newWord.append('j')
        elif letter == 'L':
            newWord.append('S')
        elif letter == 'M':
            newWord.append('<')
        elif letter == 'N':
            newWord.append('(')
        elif letter == 'O':
            newWord.append('c')
        elif letter == 'P':
            newWord.append('V')
        elif letter == 'Q':
            newWord.append('7')
        elif letter == 'R':
            newWord.append('-')
        elif letter == 'S':
            newWord.append('u')
        elif letter == 'T':
            newWord.append('K')
        elif letter == 'U':
            newWord.append('D')
        elif letter == 'V':
            newWord.append('1')
        elif letter == 'W':
            newWord.append('f')
        elif letter == 'X':
            newWord.append('n')
        elif letter == 'Y':
            newWord.append('.')
        elif letter == 'Z':
            newWord.append('h')
        elif letter == 'a':
            newWord.append('q')
        elif letter == 'b':
            newWord.append('H')
        elif letter == 'c':
            newWord.append('~')
        elif letter == 'd':
            newWord.append('?')
        elif letter == 'e':
            newWord.append('!')
        elif letter == 'f':
            newWord.append('C')
        elif letter == 'g':
            newWord.append('J')
        elif letter == 'h':
            newWord.append('M')
        elif letter == 'i':
            newWord.append('G')
        elif letter == 'j':
            newWord.append('`')
        elif letter == 'k':
            newWord.append('/')
        elif letter == 'l':
            newWord.append('w')
        elif letter == 'm':
            newWord.append('y')
        elif letter == 'n':
            newWord.append('N')
        elif letter == 'o':
            newWord.append('_')
        elif letter == 'p':
            newWord.append('l')
        elif letter == 'q':
            newWord.append('|')
        elif letter == 'r':
            newWord.append('W')
        elif letter == 's':
            newWord.append(' ')
        elif letter == 't':
            newWord.append('4')
        elif letter == 'u':
            newWord.append('#')
        elif letter == 'v':
            newWord.append('6')
        elif letter == 'w':
            newWord.append('X')
        elif letter == 'x':
            newWord.append('&')
        elif letter == 'y':
            newWord.append(',')
        elif letter == 'z':
            newWord.append('i')
        elif letter == '1':
            newWord.append('>')
        elif letter == '2':
            newWord.append('^')
        elif letter == '3':
            newWord.append('*')
        elif letter == '4':
            newWord.append('B')
        elif letter == '5':
            newWord.append('9')
        elif letter == '6':
            newWord.append('b')
        elif letter == '7':
            newWord.append('g')
        elif letter == '8':
            newWord.append('%')
        elif letter == '9':
            newWord.append(']')
        elif letter == '0':
            newWord.append('d')
        elif letter == '!':
            newWord.append('F')
        elif letter == '@':
            newWord.append('+')
        elif letter == '#':
            newWord.append('R')
        elif letter == '$':
            newWord.append('[')
        elif letter == '%':
            newWord.append(':')
        elif letter == '^':
            newWord.append('r')
        elif letter == '&':
            newWord.append('$')
        elif letter == '*':
            newWord.append('}')
        elif letter == '(':
            newWord.append('{')
        elif letter == ')':
            newWord.append('I')
        elif letter == '-':
            newWord.append('8')
        elif letter == '_':
            newWord.append('A')
        elif letter == '+':
            newWord.append('5')
        elif letter == '=':
            newWord.append('U')
        elif letter == '`':
            newWord.append('t')
        elif letter == '~':
            newWord.append('2')
        elif letter == '[':
            newWord.append('a')
        elif letter == ']':
            newWord.append('3')
        elif letter == '{':
            newWord.append('@')
        elif letter == '}':
            newWord.append('o')
        elif letter == '|':
            newWord.append('s')
        elif letter == ':':
            newWord.append('O')
        elif letter == ',':
            newWord.append('m')
        elif letter == '<':
            newWord.append('k')
        elif letter == '.':
            newWord.append('T')
        elif letter == '>':
            newWord.append('E')
        elif letter == '/':
            newWord.append('Q')
        elif letter == '?':
            newWord.append('z')
        elif letter == ' ':
            newWord.append('e')
    Switched: str  = ''.join(newWord)
    return Switched

def L_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'P':
            newWord.append('A')
        elif letter == 'p':
            newWord.append('B')
        elif letter == 'Z':
            newWord.append('C')
        elif letter == 'v':
            newWord.append('D')
        elif letter == 'Y':
            newWord.append('E')
        elif letter == 'x':
            newWord.append('F')
        elif letter == 'L':
            newWord.append('G')
        elif letter == '0':
            newWord.append('H')
        elif letter == '=':
            newWord.append('I')
        elif letter == ')':
            newWord.append('J')
        elif letter == 'j':
            newWord.append('K')
        elif letter == 'S':
            newWord.append('L')
        elif letter == '<':
            newWord.append('M')
        elif letter == '(':
            newWord.append('N')
        elif letter == 'c':
            newWord.append('O')
        elif letter == 'V':
            newWord.append('P')
        elif letter == '7':
            newWord.append('Q')
        elif letter == '-':
            newWord.append('R')
        elif letter == 'u':
            newWord.append('S')
        elif letter == 'K':
            newWord.append('T')
        elif letter == 'D':
            newWord.append('U')
        elif letter == '1':
            newWord.append('V')
        elif letter == 'f':
            newWord.append('W')
        elif letter == 'n':
            newWord.append('X')
        elif letter == '.':
            newWord.append('Y')
        elif letter == 'h':
            newWord.append('Z')
        elif letter == 'q':
            newWord.append('a')
        elif letter == 'H':
            newWord.append('b')
        elif letter == '~':
            newWord.append('c')
        elif letter == '?':
            newWord.append('d')
        elif letter == '!':
            newWord.append('e')
        elif letter == 'C':
            newWord.append('f')
        elif letter == 'J':
            newWord.append('g')
        elif letter == 'M':
            newWord.append('h')
        elif letter == 'G':
            newWord.append('i')
        elif letter == '`':
            newWord.append('j')
        elif letter == '/':
            newWord.append('k')
        elif letter == 'w':
            newWord.append('l')
        elif letter == 'y':
            newWord.append('m')
        elif letter == 'N':
            newWord.append('n')
        elif letter == '_':
            newWord.append('o')
        elif letter == 'l':
            newWord.append('p')
        elif letter == '|':
            newWord.append('q')
        elif letter == 'W':
            newWord.append('r')
        elif letter == ' ':
            newWord.append('s')
        elif letter == '4':
            newWord.append('t')
        elif letter == '#':
            newWord.append('u')
        elif letter == '6':
            newWord.append('v')
        elif letter == 'X':
            newWord.append('w')
        elif letter == '&':
            newWord.append('x')
        elif letter == ',':
            newWord.append('y')
        elif letter == 'i':
            newWord.append('z')
        elif letter == '>':
            newWord.append('1')
        elif letter == '^':
            newWord.append('2')
        elif letter == '*':
            newWord.append('3')
        elif letter == 'B':
            newWord.append('4')
        elif letter == '9':
            newWord.append('5')
        elif letter == 'b':
            newWord.append('6')
        elif letter == 'g':
            newWord.append('7')
        elif letter == '%':
            newWord.append('8')
        elif letter == ']':
            newWord.append('9')
        elif letter == 'd':
            newWord.append('0')
        elif letter == 'F':
            newWord.append('!')
        elif letter == '+':
            newWord.append('@')
        elif letter == 'R':
            newWord.append('#')
        elif letter == '[':
            newWord.append('$')
        elif letter == ':':
            newWord.append('%')
        elif letter == 'r':
            newWord.append('^')
        elif letter == '$':
            newWord.append('&')
        elif letter == '}':
            newWord.append('*')
        elif letter == '{':
            newWord.append('(')
        elif letter == 'I':
            newWord.append(')')
        elif letter == '8':
            newWord.append('-')
        elif letter == 'A':
            newWord.append('_')
        elif letter == '5':
            newWord.append('+')
        elif letter == 'U':
            newWord.append('=')
        elif letter == 't':
            newWord.append('`')
        elif letter == '2':
            newWord.append('~')
        elif letter == 'a':
            newWord.append('[')
        elif letter == '3':
            newWord.append(']')
        elif letter == '@':
            newWord.append('{')
        elif letter == 'o':
            newWord.append('}')
        elif letter == 's':
            newWord.append('|')
        elif letter == 'O':
            newWord.append(':')
        elif letter == 'm':
            newWord.append(',')
        elif letter == 'k':
            newWord.append('<')
        elif letter == 'T':
            newWord.append('.')
        elif letter == 'E':
            newWord.append('>')
        elif letter == 'Q':
            newWord.append('/')
        elif letter == 'z':
            newWord.append('?')
        elif letter == 'e':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def M_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('z')
        elif letter == 'B':
            newWord.append('=')
        elif letter == 'C':
            newWord.append('q')
        elif letter == 'D':
            newWord.append('G')
        elif letter == 'E':
            newWord.append('X')
        elif letter == 'F':
            newWord.append('Z')
        elif letter == 'G':
            newWord.append('%')
        elif letter == 'H':
            newWord.append('l')
        elif letter == 'I':
            newWord.append('O')
        elif letter == 'J':
            newWord.append('V')
        elif letter == 'K':
            newWord.append('e')
        elif letter == 'L':
            newWord.append('D')
        elif letter == 'M':
            newWord.append('i')
        elif letter == 'N':
            newWord.append('7')
        elif letter == 'O':
            newWord.append('>')
        elif letter == 'P':
            newWord.append('{')
        elif letter == 'Q':
            newWord.append('(')
        elif letter == 'R':
            newWord.append('9')
        elif letter == 'S':
            newWord.append('H')
        elif letter == 'T':
            newWord.append(',')
        elif letter == 'U':
            newWord.append('s')
        elif letter == 'V':
            newWord.append('o')
        elif letter == 'W':
            newWord.append(')')
        elif letter == 'X':
            newWord.append(' ')
        elif letter == 'Y':
            newWord.append('~')
        elif letter == 'Z':
            newWord.append('A')
        elif letter == 'a':
            newWord.append('$')
        elif letter == 'b':
            newWord.append('/')
        elif letter == 'c':
            newWord.append('p')
        elif letter == 'd':
            newWord.append('E')
        elif letter == 'e':
            newWord.append('P')
        elif letter == 'f':
            newWord.append('_')
        elif letter == 'g':
            newWord.append('k')
        elif letter == 'h':
            newWord.append('r')
        elif letter == 'i':
            newWord.append('K')
        elif letter == 'j':
            newWord.append('`')
        elif letter == 'k':
            newWord.append('.')
        elif letter == 'l':
            newWord.append('2')
        elif letter == 'm':
            newWord.append('*')
        elif letter == 'n':
            newWord.append('[')
        elif letter == 'o':
            newWord.append('}')
        elif letter == 'p':
            newWord.append('#')
        elif letter == 'q':
            newWord.append('t')
        elif letter == 'r':
            newWord.append('L')
        elif letter == 's':
            newWord.append('?')
        elif letter == 't':
            newWord.append('1')
        elif letter == 'u':
            newWord.append('@')
        elif letter == 'v':
            newWord.append('0')
        elif letter == 'w':
            newWord.append('b')
        elif letter == 'x':
            newWord.append('j')
        elif letter == 'y':
            newWord.append('n')
        elif letter == 'z':
            newWord.append('y')
        elif letter == '1':
            newWord.append('g')
        elif letter == '2':
            newWord.append('6')
        elif letter == '3':
            newWord.append('|')
        elif letter == '4':
            newWord.append('3')
        elif letter == '5':
            newWord.append('a')
        elif letter == '6':
            newWord.append('x')
        elif letter == '7':
            newWord.append('F')
        elif letter == '8':
            newWord.append('4')
        elif letter == '9':
            newWord.append('R')
        elif letter == '0':
            newWord.append('8')
        elif letter == '!':
            newWord.append('U')
        elif letter == '@':
            newWord.append('<')
        elif letter == '#':
            newWord.append('N')
        elif letter == '$':
            newWord.append(':')
        elif letter == '%':
            newWord.append('m')
        elif letter == '^':
            newWord.append('+')
        elif letter == '&':
            newWord.append('C')
        elif letter == '*':
            newWord.append('h')
        elif letter == '(':
            newWord.append('Q')
        elif letter == ')':
            newWord.append('I')
        elif letter == '-':
            newWord.append('f')
        elif letter == '_':
            newWord.append('w')
        elif letter == '+':
            newWord.append('c')
        elif letter == '=':
            newWord.append('B')
        elif letter == '`':
            newWord.append(']')
        elif letter == '~':
            newWord.append('T')
        elif letter == '[':
            newWord.append('W')
        elif letter == ']':
            newWord.append('J')
        elif letter == '{':
            newWord.append('M')
        elif letter == '}':
            newWord.append('Y')
        elif letter == '|':
            newWord.append('S')
        elif letter == ':':
            newWord.append('5')
        elif letter == ',':
            newWord.append('v')
        elif letter == '<':
            newWord.append('^')
        elif letter == '.':
            newWord.append('d')
        elif letter == '>':
            newWord.append('!')
        elif letter == '/':
            newWord.append('-')
        elif letter == '?':
            newWord.append('&')
        elif letter == ' ':
            newWord.append('u')
    Switched: str  = ''.join(newWord)
    return Switched

def M_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'z':
            newWord.append('A')
        elif letter == '=':
            newWord.append('B')
        elif letter == 'q':
            newWord.append('C')
        elif letter == 'G':
            newWord.append('D')
        elif letter == 'X':
            newWord.append('E')
        elif letter == 'Z':
            newWord.append('F')
        elif letter == '%':
            newWord.append('G')
        elif letter == 'l':
            newWord.append('H')
        elif letter == 'O':
            newWord.append('I')
        elif letter == 'V':
            newWord.append('J')
        elif letter == 'e':
            newWord.append('K')
        elif letter == 'D':
            newWord.append('L')
        elif letter == 'i':
            newWord.append('M')
        elif letter == '7':
            newWord.append('N')
        elif letter == '>':
            newWord.append('O')
        elif letter == '{':
            newWord.append('P')
        elif letter == '(':
            newWord.append('Q')
        elif letter == '9':
            newWord.append('R')
        elif letter == 'H':
            newWord.append('S')
        elif letter == ',':
            newWord.append('T')
        elif letter == 's':
            newWord.append('U')
        elif letter == 'o':
            newWord.append('V')
        elif letter == ')':
            newWord.append('W')
        elif letter == ' ':
            newWord.append('X')
        elif letter == '~':
            newWord.append('Y')
        elif letter == 'A':
            newWord.append('Z')
        elif letter == '$':
            newWord.append('a')
        elif letter == '/':
            newWord.append('b')
        elif letter == 'p':
            newWord.append('c')
        elif letter == 'E':
            newWord.append('d')
        elif letter == 'P':
            newWord.append('e')
        elif letter == '_':
            newWord.append('f')
        elif letter == 'k':
            newWord.append('g')
        elif letter == 'r':
            newWord.append('h')
        elif letter == 'K':
            newWord.append('i')
        elif letter == '`':
            newWord.append('j')
        elif letter == '.':
            newWord.append('k')
        elif letter == '2':
            newWord.append('l')
        elif letter == '*':
            newWord.append('m')
        elif letter == '[':
            newWord.append('n')
        elif letter == '}':
            newWord.append('o')
        elif letter == '#':
            newWord.append('p')
        elif letter == 't':
            newWord.append('q')
        elif letter == 'L':
            newWord.append('r')
        elif letter == '?':
            newWord.append('s')
        elif letter == '1':
            newWord.append('t')
        elif letter == '@':
            newWord.append('u')
        elif letter == '0':
            newWord.append('v')
        elif letter == 'b':
            newWord.append('w')
        elif letter == 'j':
            newWord.append('x')
        elif letter == 'n':
            newWord.append('y')
        elif letter == 'y':
            newWord.append('z')
        elif letter == 'g':
            newWord.append('1')
        elif letter == '6':
            newWord.append('2')
        elif letter == '|':
            newWord.append('3')
        elif letter == '3':
            newWord.append('4')
        elif letter == 'a':
            newWord.append('5')
        elif letter == 'x':
            newWord.append('6')
        elif letter == 'F':
            newWord.append('7')
        elif letter == '4':
            newWord.append('8')
        elif letter == 'R':
            newWord.append('9')
        elif letter == '8':
            newWord.append('0')
        elif letter == 'U':
            newWord.append('!')
        elif letter == '<':
            newWord.append('@')
        elif letter == 'N':
            newWord.append('#')
        elif letter == ':':
            newWord.append('$')
        elif letter == 'm':
            newWord.append('%')
        elif letter == '+':
            newWord.append('^')
        elif letter == 'C':
            newWord.append('&')
        elif letter == 'h':
            newWord.append('*')
        elif letter == 'Q':
            newWord.append('(')
        elif letter == 'I':
            newWord.append(')')
        elif letter == 'f':
            newWord.append('-')
        elif letter == 'w':
            newWord.append('_')
        elif letter == 'c':
            newWord.append('+')
        elif letter == 'B':
            newWord.append('=')
        elif letter == ']':
            newWord.append('`')
        elif letter == 'T':
            newWord.append('~')
        elif letter == 'W':
            newWord.append('[')
        elif letter == 'J':
            newWord.append(']')
        elif letter == 'M':
            newWord.append('{')
        elif letter == 'Y':
            newWord.append('}')
        elif letter == 'S':
            newWord.append('|')
        elif letter == '5':
            newWord.append(':')
        elif letter == 'v':
            newWord.append(',')
        elif letter == '^':
            newWord.append('<')
        elif letter == 'd':
            newWord.append('.')
        elif letter == '!':
            newWord.append('>')
        elif letter == '-':
            newWord.append('/')
        elif letter == '&':
            newWord.append('?')
        elif letter == 'u':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def N_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('7')
        elif letter == 'B':
            newWord.append('R')
        elif letter == 'C':
            newWord.append('f')
        elif letter == 'D':
            newWord.append('.')
        elif letter == 'E':
            newWord.append('*')
        elif letter == 'F':
            newWord.append(' ')
        elif letter == 'G':
            newWord.append('e')
        elif letter == 'H':
            newWord.append('_')
        elif letter == 'I':
            newWord.append('z')
        elif letter == 'J':
            newWord.append('Z')
        elif letter == 'K':
            newWord.append('4')
        elif letter == 'L':
            newWord.append('I')
        elif letter == 'M':
            newWord.append('1')
        elif letter == 'N':
            newWord.append(')')
        elif letter == 'O':
            newWord.append('2')
        elif letter == 'P':
            newWord.append('$')
        elif letter == 'Q':
            newWord.append('3')
        elif letter == 'R':
            newWord.append('}')
        elif letter == 'S':
            newWord.append('`')
        elif letter == 'T':
            newWord.append('i')
        elif letter == 'U':
            newWord.append('0')
        elif letter == 'V':
            newWord.append('n')
        elif letter == 'W':
            newWord.append('H')
        elif letter == 'X':
            newWord.append('w')
        elif letter == 'Y':
            newWord.append('G')
        elif letter == 'Z':
            newWord.append('6')
        elif letter == 'a':
            newWord.append('=')
        elif letter == 'b':
            newWord.append('Y')
        elif letter == 'c':
            newWord.append('9')
        elif letter == 'd':
            newWord.append('p')
        elif letter == 'e':
            newWord.append('8')
        elif letter == 'f':
            newWord.append('A')
        elif letter == 'g':
            newWord.append(':')
        elif letter == 'h':
            newWord.append('a')
        elif letter == 'i':
            newWord.append('K')
        elif letter == 'j':
            newWord.append('{')
        elif letter == 'k':
            newWord.append('h')
        elif letter == 'l':
            newWord.append('-')
        elif letter == 'm':
            newWord.append('b')
        elif letter == 'n':
            newWord.append('[')
        elif letter == 'o':
            newWord.append('M')
        elif letter == 'p':
            newWord.append('+')
        elif letter == 'q':
            newWord.append('c')
        elif letter == 'r':
            newWord.append('B')
        elif letter == 's':
            newWord.append('d')
        elif letter == 't':
            newWord.append('N')
        elif letter == 'u':
            newWord.append('/')
        elif letter == 'v':
            newWord.append('#')
        elif letter == 'w':
            newWord.append('S')
        elif letter == 'x':
            newWord.append('J')
        elif letter == 'y':
            newWord.append('D')
        elif letter == 'z':
            newWord.append('v')
        elif letter == '1':
            newWord.append('^')
        elif letter == '2':
            newWord.append('T')
        elif letter == '3':
            newWord.append('5')
        elif letter == '4':
            newWord.append('C')
        elif letter == '5':
            newWord.append('u')
        elif letter == '6':
            newWord.append('&')
        elif letter == '7':
            newWord.append('q')
        elif letter == '8':
            newWord.append('<')
        elif letter == '9':
            newWord.append('V')
        elif letter == '0':
            newWord.append('s')
        elif letter == '!':
            newWord.append('!')
        elif letter == '@':
            newWord.append('l')
        elif letter == '#':
            newWord.append('j')
        elif letter == '$':
            newWord.append('U')
        elif letter == '%':
            newWord.append('?')
        elif letter == '^':
            newWord.append('X')
        elif letter == '&':
            newWord.append('g')
        elif letter == '*':
            newWord.append(',')
        elif letter == '(':
            newWord.append('Q')
        elif letter == ')':
            newWord.append('r')
        elif letter == '-':
            newWord.append('y')
        elif letter == '_':
            newWord.append('|')
        elif letter == '+':
            newWord.append('E')
        elif letter == '=':
            newWord.append('@')
        elif letter == '`':
            newWord.append('x')
        elif letter == '~':
            newWord.append('O')
        elif letter == '[':
            newWord.append('%')
        elif letter == ']':
            newWord.append('W')
        elif letter == '{':
            newWord.append('m')
        elif letter == '}':
            newWord.append('~')
        elif letter == '|':
            newWord.append('(')
        elif letter == ':':
            newWord.append('k')
        elif letter == ',':
            newWord.append('o')
        elif letter == '<':
            newWord.append('P')
        elif letter == '.':
            newWord.append('L')
        elif letter == '>':
            newWord.append('t')
        elif letter == '/':
            newWord.append('F')
        elif letter == '?':
            newWord.append(']')
        elif letter == ' ':
            newWord.append('>')
    Switched: str  = ''.join(newWord)
    return Switched

def N_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '7':
            newWord.append('A')
        elif letter == 'R':
            newWord.append('B')
        elif letter == 'f':
            newWord.append('C')
        elif letter == '.':
            newWord.append('D')
        elif letter == '*':
            newWord.append('E')
        elif letter == ' ':
            newWord.append('F')
        elif letter == 'e':
            newWord.append('G')
        elif letter == '_':
            newWord.append('H')
        elif letter == 'z':
            newWord.append('I')
        elif letter == 'Z':
            newWord.append('J')
        elif letter == '4':
            newWord.append('K')
        elif letter == 'I':
            newWord.append('L')
        elif letter == '1':
            newWord.append('M')
        elif letter == ')':
            newWord.append('N')
        elif letter == '2':
            newWord.append('O')
        elif letter == '$':
            newWord.append('P')
        elif letter == '3':
            newWord.append('Q')
        elif letter == '}':
            newWord.append('R')
        elif letter == '`':
            newWord.append('S')
        elif letter == 'i':
            newWord.append('T')
        elif letter == '0':
            newWord.append('U')
        elif letter == 'n':
            newWord.append('V')
        elif letter == 'H':
            newWord.append('W')
        elif letter == 'w':
            newWord.append('X')
        elif letter == 'G':
            newWord.append('Y')
        elif letter == '6':
            newWord.append('Z')
        elif letter == '=':
            newWord.append('a')
        elif letter == 'Y':
            newWord.append('b')
        elif letter == '9':
            newWord.append('c')
        elif letter == 'p':
            newWord.append('d')
        elif letter == '8':
            newWord.append('e')
        elif letter == 'A':
            newWord.append('f')
        elif letter == ':':
            newWord.append('g')
        elif letter == 'a':
            newWord.append('h')
        elif letter == 'K':
            newWord.append('i')
        elif letter == '{':
            newWord.append('j')
        elif letter == 'h':
            newWord.append('k')
        elif letter == '-':
            newWord.append('l')
        elif letter == 'b':
            newWord.append('m')
        elif letter == '[':
            newWord.append('n')
        elif letter == 'M':
            newWord.append('o')
        elif letter == '+':
            newWord.append('p')
        elif letter == 'c':
            newWord.append('q')
        elif letter == 'B':
            newWord.append('r')
        elif letter == 'd':
            newWord.append('s')
        elif letter == 'N':
            newWord.append('t')
        elif letter == '/':
            newWord.append('u')
        elif letter == '#':
            newWord.append('v')
        elif letter == 'S':
            newWord.append('w')
        elif letter == 'J':
            newWord.append('x')
        elif letter == 'D':
            newWord.append('y')
        elif letter == 'v':
            newWord.append('z')
        elif letter == '^':
            newWord.append('1')
        elif letter == 'T':
            newWord.append('2')
        elif letter == '5':
            newWord.append('3')
        elif letter == 'C':
            newWord.append('4')
        elif letter == 'u':
            newWord.append('5')
        elif letter == '&':
            newWord.append('6')
        elif letter == 'q':
            newWord.append('7')
        elif letter == '<':
            newWord.append('8')
        elif letter == 'V':
            newWord.append('9')
        elif letter == 's':
            newWord.append('0')
        elif letter == '!':
            newWord.append('!')
        elif letter == 'l':
            newWord.append('@')
        elif letter == 'j':
            newWord.append('#')
        elif letter == 'U':
            newWord.append('$')
        elif letter == '?':
            newWord.append('%')
        elif letter == 'X':
            newWord.append('^')
        elif letter == 'g':
            newWord.append('&')
        elif letter == ',':
            newWord.append('*')
        elif letter == 'Q':
            newWord.append('(')
        elif letter == 'r':
            newWord.append(')')
        elif letter == 'y':
            newWord.append('-')
        elif letter == '|':
            newWord.append('_')
        elif letter == 'E':
            newWord.append('+')
        elif letter == '@':
            newWord.append('=')
        elif letter == 'x':
            newWord.append('`')
        elif letter == 'O':
            newWord.append('~')
        elif letter == '%':
            newWord.append('[')
        elif letter == 'W':
            newWord.append(']')
        elif letter == 'm':
            newWord.append('{')
        elif letter == '~':
            newWord.append('}')
        elif letter == '(':
            newWord.append('|')
        elif letter == 'k':
            newWord.append(':')
        elif letter == 'o':
            newWord.append(',')
        elif letter == 'P':
            newWord.append('<')
        elif letter == 'L':
            newWord.append('.')
        elif letter == 't':
            newWord.append('>')
        elif letter == 'F':
            newWord.append('/')
        elif letter == ']':
            newWord.append('?')
        elif letter == '>':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def O_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('*')
        elif letter == 'B':
            newWord.append('T')
        elif letter == 'C':
            newWord.append('#')
        elif letter == 'D':
            newWord.append('V')
        elif letter == 'E':
            newWord.append(',')
        elif letter == 'F':
            newWord.append('l')
        elif letter == 'G':
            newWord.append('U')
        elif letter == 'H':
            newWord.append('h')
        elif letter == 'I':
            newWord.append('w')
        elif letter == 'J':
            newWord.append('R')
        elif letter == 'K':
            newWord.append('<')
        elif letter == 'L':
            newWord.append('.')
        elif letter == 'M':
            newWord.append('H')
        elif letter == 'N':
            newWord.append('Y')
        elif letter == 'O':
            newWord.append('K')
        elif letter == 'P':
            newWord.append('[')
        elif letter == 'Q':
            newWord.append('5')
        elif letter == 'R':
            newWord.append('6')
        elif letter == 'S':
            newWord.append('i')
        elif letter == 'T':
            newWord.append('1')
        elif letter == 'U':
            newWord.append('M')
        elif letter == 'V':
            newWord.append('%')
        elif letter == 'W':
            newWord.append('j')
        elif letter == 'X':
            newWord.append('_')
        elif letter == 'Y':
            newWord.append('v')
        elif letter == 'Z':
            newWord.append('m')
        elif letter == 'a':
            newWord.append('W')
        elif letter == 'b':
            newWord.append('}')
        elif letter == 'c':
            newWord.append('~')
        elif letter == 'd':
            newWord.append('O')
        elif letter == 'e':
            newWord.append('x')
        elif letter == 'f':
            newWord.append('I')
        elif letter == 'g':
            newWord.append('4')
        elif letter == 'h':
            newWord.append('(')
        elif letter == 'i':
            newWord.append('^')
        elif letter == 'j':
            newWord.append('8')
        elif letter == 'k':
            newWord.append('L')
        elif letter == 'l':
            newWord.append('d')
        elif letter == 'm':
            newWord.append('r')
        elif letter == 'n':
            newWord.append('J')
        elif letter == 'o':
            newWord.append('$')
        elif letter == 'p':
            newWord.append('>')
        elif letter == 'q':
            newWord.append('`')
        elif letter == 'r':
            newWord.append('+')
        elif letter == 's':
            newWord.append('G')
        elif letter == 't':
            newWord.append('q')
        elif letter == 'u':
            newWord.append('z')
        elif letter == 'v':
            newWord.append('{')
        elif letter == 'w':
            newWord.append('e')
        elif letter == 'x':
            newWord.append('!')
        elif letter == 'y':
            newWord.append(']')
        elif letter == 'z':
            newWord.append(' ')
        elif letter == '1':
            newWord.append('Q')
        elif letter == '2':
            newWord.append('@')
        elif letter == '3':
            newWord.append('=')
        elif letter == '4':
            newWord.append('p')
        elif letter == '5':
            newWord.append('P')
        elif letter == '6':
            newWord.append('g')
        elif letter == '7':
            newWord.append('N')
        elif letter == '8':
            newWord.append('C')
        elif letter == '9':
            newWord.append('2')
        elif letter == '0':
            newWord.append('b')
        elif letter == '!':
            newWord.append('7')
        elif letter == '@':
            newWord.append('s')
        elif letter == '#':
            newWord.append(':')
        elif letter == '$':
            newWord.append('0')
        elif letter == '%':
            newWord.append('n')
        elif letter == '^':
            newWord.append('c')
        elif letter == '&':
            newWord.append('t')
        elif letter == '*':
            newWord.append('3')
        elif letter == '(':
            newWord.append('y')
        elif letter == ')':
            newWord.append('/')
        elif letter == '-':
            newWord.append('k')
        elif letter == '_':
            newWord.append(')')
        elif letter == '+':
            newWord.append('B')
        elif letter == '=':
            newWord.append('F')
        elif letter == '`':
            newWord.append('E')
        elif letter == '~':
            newWord.append('-')
        elif letter == '[':
            newWord.append('f')
        elif letter == ']':
            newWord.append('|')
        elif letter == '{':
            newWord.append('X')
        elif letter == '}':
            newWord.append('?')
        elif letter == '|':
            newWord.append('9')
        elif letter == ':':
            newWord.append('D')
        elif letter == ',':
            newWord.append('A')
        elif letter == '<':
            newWord.append('u')
        elif letter == '.':
            newWord.append('&')
        elif letter == '>':
            newWord.append('S')
        elif letter == '/':
            newWord.append('a')
        elif letter == '?':
            newWord.append('o')
        elif letter == ' ':
            newWord.append('Z')
    Switched: str  = ''.join(newWord)
    return Switched

def O_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '*':
            newWord.append('A')
        elif letter == 'T':
            newWord.append('B')
        elif letter == '#':
            newWord.append('C')
        elif letter == 'V':
            newWord.append('D')
        elif letter == ',':
            newWord.append('E')
        elif letter == 'l':
            newWord.append('F')
        elif letter == 'U':
            newWord.append('G')
        elif letter == 'h':
            newWord.append('H')
        elif letter == 'w':
            newWord.append('I')
        elif letter == 'R':
            newWord.append('J')
        elif letter == '<':
            newWord.append('K')
        elif letter == '.':
            newWord.append('L')
        elif letter == 'H':
            newWord.append('M')
        elif letter == 'Y':
            newWord.append('N')
        elif letter == 'K':
            newWord.append('O')
        elif letter == '[':
            newWord.append('P')
        elif letter == '5':
            newWord.append('Q')
        elif letter == '6':
            newWord.append('R')
        elif letter == 'i':
            newWord.append('S')
        elif letter == '1':
            newWord.append('T')
        elif letter == 'M':
            newWord.append('U')
        elif letter == '%':
            newWord.append('V')
        elif letter == 'j':
            newWord.append('W')
        elif letter == '_':
            newWord.append('X')
        elif letter == 'v':
            newWord.append('Y')
        elif letter == 'm':
            newWord.append('Z')
        elif letter == 'W':
            newWord.append('a')
        elif letter == '}':
            newWord.append('b')
        elif letter == '~':
            newWord.append('c')
        elif letter == 'O':
            newWord.append('d')
        elif letter == 'x':
            newWord.append('e')
        elif letter == 'I':
            newWord.append('f')
        elif letter == '4':
            newWord.append('g')
        elif letter == '(':
            newWord.append('h')
        elif letter == '^':
            newWord.append('i')
        elif letter == '8':
            newWord.append('j')
        elif letter == 'L':
            newWord.append('k')
        elif letter == 'd':
            newWord.append('l')
        elif letter == 'r':
            newWord.append('m')
        elif letter == 'J':
            newWord.append('n')
        elif letter == '$':
            newWord.append('o')
        elif letter == '>':
            newWord.append('p')
        elif letter == '`':
            newWord.append('q')
        elif letter == '+':
            newWord.append('r')
        elif letter == 'G':
            newWord.append('s')
        elif letter == 'q':
            newWord.append('t')
        elif letter == 'z':
            newWord.append('u')
        elif letter == '{':
            newWord.append('v')
        elif letter == 'e':
            newWord.append('w')
        elif letter == '!':
            newWord.append('x')
        elif letter == ']':
            newWord.append('y')
        elif letter == ' ':
            newWord.append('z')
        elif letter == 'Q':
            newWord.append('1')
        elif letter == '@':
            newWord.append('2')
        elif letter == '=':
            newWord.append('3')
        elif letter == 'p':
            newWord.append('4')
        elif letter == 'P':
            newWord.append('5')
        elif letter == 'g':
            newWord.append('6')
        elif letter == 'N':
            newWord.append('7')
        elif letter == 'C':
            newWord.append('8')
        elif letter == '2':
            newWord.append('9')
        elif letter == 'b':
            newWord.append('0')
        elif letter == '7':
            newWord.append('!')
        elif letter == 's':
            newWord.append('@')
        elif letter == ':':
            newWord.append('#')
        elif letter == '0':
            newWord.append('$')
        elif letter == 'n':
            newWord.append('%')
        elif letter == 'c':
            newWord.append('^')
        elif letter == 't':
            newWord.append('&')
        elif letter == '3':
            newWord.append('*')
        elif letter == 'y':
            newWord.append('(')
        elif letter == '/':
            newWord.append(')')
        elif letter == 'k':
            newWord.append('-')
        elif letter == ')':
            newWord.append('_')
        elif letter == 'B':
            newWord.append('+')
        elif letter == 'F':
            newWord.append('=')
        elif letter == 'E':
            newWord.append('`')
        elif letter == '-':
            newWord.append('~')
        elif letter == 'f':
            newWord.append('[')
        elif letter == '|':
            newWord.append(']')
        elif letter == 'X':
            newWord.append('{')
        elif letter == '?':
            newWord.append('}')
        elif letter == '9':
            newWord.append('|')
        elif letter == 'D':
            newWord.append(':')
        elif letter == 'A':
            newWord.append(',')
        elif letter == 'u':
            newWord.append('<')
        elif letter == '&':
            newWord.append('.')
        elif letter == 'S':
            newWord.append('>')
        elif letter == 'a':
            newWord.append('/')
        elif letter == 'o':
            newWord.append('?')
        elif letter == 'Z':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def P_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('R')
        elif letter == 'B':
            newWord.append('z')
        elif letter == 'C':
            newWord.append('^')
        elif letter == 'D':
            newWord.append('Z')
        elif letter == 'E':
            newWord.append('%')
        elif letter == 'F':
            newWord.append('H')
        elif letter == 'G':
            newWord.append('k')
        elif letter == 'H':
            newWord.append('t')
        elif letter == 'I':
            newWord.append('j')
        elif letter == 'J':
            newWord.append('h')
        elif letter == 'K':
            newWord.append('8')
        elif letter == 'L':
            newWord.append('p')
        elif letter == 'M':
            newWord.append('~')
        elif letter == 'N':
            newWord.append('{')
        elif letter == 'O':
            newWord.append('u')
        elif letter == 'P':
            newWord.append('1')
        elif letter == 'Q':
            newWord.append('!')
        elif letter == 'R':
            newWord.append('<')
        elif letter == 'S':
            newWord.append('+')
        elif letter == 'T':
            newWord.append('d')
        elif letter == 'U':
            newWord.append('#')
        elif letter == 'V':
            newWord.append('V')
        elif letter == 'W':
            newWord.append('*')
        elif letter == 'X':
            newWord.append('4')
        elif letter == 'Y':
            newWord.append('x')
        elif letter == 'Z':
            newWord.append('Y')
        elif letter == 'a':
            newWord.append('D')
        elif letter == 'b':
            newWord.append('}')
        elif letter == 'c':
            newWord.append('E')
        elif letter == 'd':
            newWord.append('I')
        elif letter == 'e':
            newWord.append('P')
        elif letter == 'f':
            newWord.append('y')
        elif letter == 'g':
            newWord.append('J')
        elif letter == 'h':
            newWord.append(')')
        elif letter == 'i':
            newWord.append('f')
        elif letter == 'j':
            newWord.append('S')
        elif letter == 'k':
            newWord.append('F')
        elif letter == 'l':
            newWord.append('w')
        elif letter == 'm':
            newWord.append('s')
        elif letter == 'n':
            newWord.append('M')
        elif letter == 'o':
            newWord.append('9')
        elif letter == 'p':
            newWord.append('o')
        elif letter == 'q':
            newWord.append('v')
        elif letter == 'r':
            newWord.append('5')
        elif letter == 's':
            newWord.append('&')
        elif letter == 't':
            newWord.append('B')
        elif letter == 'u':
            newWord.append('`')
        elif letter == 'v':
            newWord.append('A')
        elif letter == 'w':
            newWord.append('U')
        elif letter == 'x':
            newWord.append('T')
        elif letter == 'y':
            newWord.append('e')
        elif letter == 'z':
            newWord.append('6')
        elif letter == '1':
            newWord.append('3')
        elif letter == '2':
            newWord.append('=')
        elif letter == '3':
            newWord.append('7')
        elif letter == '4':
            newWord.append('K')
        elif letter == '5':
            newWord.append('[')
        elif letter == '6':
            newWord.append('r')
        elif letter == '7':
            newWord.append('c')
        elif letter == '8':
            newWord.append('G')
        elif letter == '9':
            newWord.append('>')
        elif letter == '0':
            newWord.append('X')
        elif letter == '!':
            newWord.append('?')
        elif letter == '@':
            newWord.append('W')
        elif letter == '#':
            newWord.append('g')
        elif letter == '$':
            newWord.append('a')
        elif letter == '%':
            newWord.append('C')
        elif letter == '^':
            newWord.append(']')
        elif letter == '&':
            newWord.append('/')
        elif letter == '*':
            newWord.append('0')
        elif letter == '(':
            newWord.append('n')
        elif letter == ')':
            newWord.append(',')
        elif letter == '-':
            newWord.append('i')
        elif letter == '_':
            newWord.append('2')
        elif letter == '+':
            newWord.append('b')
        elif letter == '=':
            newWord.append(' ')
        elif letter == '`':
            newWord.append(':')
        elif letter == '~':
            newWord.append('l')
        elif letter == '[':
            newWord.append('-')
        elif letter == ']':
            newWord.append('N')
        elif letter == '{':
            newWord.append('q')
        elif letter == '}':
            newWord.append('.')
        elif letter == '|':
            newWord.append('$')
        elif letter == ':':
            newWord.append('Q')
        elif letter == ',':
            newWord.append('_')
        elif letter == '<':
            newWord.append('(')
        elif letter == '.':
            newWord.append('|')
        elif letter == '>':
            newWord.append('m')
        elif letter == '/':
            newWord.append('O')
        elif letter == '?':
            newWord.append('@')
        elif letter == ' ':
            newWord.append('L')
    Switched: str  = ''.join(newWord)
    return Switched

def P_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'R':
            newWord.append('A')
        elif letter == 'z':
            newWord.append('B')
        elif letter == '^':
            newWord.append('C')
        elif letter == 'Z':
            newWord.append('D')
        elif letter == '%':
            newWord.append('E')
        elif letter == 'H':
            newWord.append('F')
        elif letter == 'k':
            newWord.append('G')
        elif letter == 't':
            newWord.append('H')
        elif letter == 'j':
            newWord.append('I')
        elif letter == 'h':
            newWord.append('J')
        elif letter == '8':
            newWord.append('K')
        elif letter == 'p':
            newWord.append('L')
        elif letter == '~':
            newWord.append('M')
        elif letter == '{':
            newWord.append('N')
        elif letter == 'u':
            newWord.append('O')
        elif letter == '1':
            newWord.append('P')
        elif letter == '!':
            newWord.append('Q')
        elif letter == '<':
            newWord.append('R')
        elif letter == '+':
            newWord.append('S')
        elif letter == 'd':
            newWord.append('T')
        elif letter == '#':
            newWord.append('U')
        elif letter == 'V':
            newWord.append('V')
        elif letter == '*':
            newWord.append('W')
        elif letter == '4':
            newWord.append('X')
        elif letter == 'x':
            newWord.append('Y')
        elif letter == 'Y':
            newWord.append('Z')
        elif letter == 'D':
            newWord.append('a')
        elif letter == '}':
            newWord.append('b')
        elif letter == 'E':
            newWord.append('c')
        elif letter == 'I':
            newWord.append('d')
        elif letter == 'P':
            newWord.append('e')
        elif letter == 'y':
            newWord.append('f')
        elif letter == 'J':
            newWord.append('g')
        elif letter == ')':
            newWord.append('h')
        elif letter == 'f':
            newWord.append('i')
        elif letter == 'S':
            newWord.append('j')
        elif letter == 'F':
            newWord.append('k')
        elif letter == 'w':
            newWord.append('l')
        elif letter == 's':
            newWord.append('m')
        elif letter == 'M':
            newWord.append('n')
        elif letter == '9':
            newWord.append('o')
        elif letter == 'o':
            newWord.append('p')
        elif letter == 'v':
            newWord.append('q')
        elif letter == '5':
            newWord.append('r')
        elif letter == '&':
            newWord.append('s')
        elif letter == 'B':
            newWord.append('t')
        elif letter == '`':
            newWord.append('u')
        elif letter == 'A':
            newWord.append('v')
        elif letter == 'U':
            newWord.append('w')
        elif letter == 'T':
            newWord.append('x')
        elif letter == 'e':
            newWord.append('y')
        elif letter == '6':
            newWord.append('z')
        elif letter == '3':
            newWord.append('1')
        elif letter == '=':
            newWord.append('2')
        elif letter == '7':
            newWord.append('3')
        elif letter == 'K':
            newWord.append('4')
        elif letter == '[':
            newWord.append('5')
        elif letter == 'r':
            newWord.append('6')
        elif letter == 'c':
            newWord.append('7')
        elif letter == 'G':
            newWord.append('8')
        elif letter == '>':
            newWord.append('9')
        elif letter == 'X':
            newWord.append('0')
        elif letter == '?':
            newWord.append('!')
        elif letter == 'W':
            newWord.append('@')
        elif letter == 'g':
            newWord.append('#')
        elif letter == 'a':
            newWord.append('$')
        elif letter == 'C':
            newWord.append('%')
        elif letter == ']':
            newWord.append('^')
        elif letter == '/':
            newWord.append('&')
        elif letter == '0':
            newWord.append('*')
        elif letter == 'n':
            newWord.append('(')
        elif letter == ',':
            newWord.append(')')
        elif letter == 'i':
            newWord.append('-')
        elif letter == '2':
            newWord.append('_')
        elif letter == 'b':
            newWord.append('+')
        elif letter == ' ':
            newWord.append('=')
        elif letter == ':':
            newWord.append('`')
        elif letter == 'l':
            newWord.append('~')
        elif letter == '-':
            newWord.append('[')
        elif letter == 'N':
            newWord.append(']')
        elif letter == 'q':
            newWord.append('{')
        elif letter == '.':
            newWord.append('}')
        elif letter == '$':
            newWord.append('|')
        elif letter == 'Q':
            newWord.append(':')
        elif letter == '_':
            newWord.append(',')
        elif letter == '(':
            newWord.append('<')
        elif letter == '|':
            newWord.append('.')
        elif letter == 'm':
            newWord.append('>')
        elif letter == 'O':
            newWord.append('/')
        elif letter == '@':
            newWord.append('?')
        elif letter == 'L':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def Q_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('H')
        elif letter == 'B':
            newWord.append('(')
        elif letter == 'C':
            newWord.append('e')
        elif letter == 'D':
            newWord.append('i')
        elif letter == 'E':
            newWord.append('V')
        elif letter == 'F':
            newWord.append('n')
        elif letter == 'G':
            newWord.append('{')
        elif letter == 'H':
            newWord.append('6')
        elif letter == 'I':
            newWord.append('O')
        elif letter == 'J':
            newWord.append('1')
        elif letter == 'K':
            newWord.append('L')
        elif letter == 'L':
            newWord.append('x')
        elif letter == 'M':
            newWord.append('J')
        elif letter == 'N':
            newWord.append('8')
        elif letter == 'O':
            newWord.append('7')
        elif letter == 'P':
            newWord.append('@')
        elif letter == 'Q':
            newWord.append('!')
        elif letter == 'R':
            newWord.append('A')
        elif letter == 'S':
            newWord.append('<')
        elif letter == 'T':
            newWord.append('b')
        elif letter == 'U':
            newWord.append('.')
        elif letter == 'V':
            newWord.append('%')
        elif letter == 'W':
            newWord.append('`')
        elif letter == 'X':
            newWord.append('I')
        elif letter == 'Y':
            newWord.append('Q')
        elif letter == 'Z':
            newWord.append('u')
        elif letter == 'a':
            newWord.append('S')
        elif letter == 'b':
            newWord.append('P')
        elif letter == 'c':
            newWord.append('j')
        elif letter == 'd':
            newWord.append('N')
        elif letter == 'e':
            newWord.append('/')
        elif letter == 'f':
            newWord.append('Z')
        elif letter == 'g':
            newWord.append('l')
        elif letter == 'h':
            newWord.append('M')
        elif letter == 'i':
            newWord.append('$')
        elif letter == 'j':
            newWord.append('a')
        elif letter == 'k':
            newWord.append(')')
        elif letter == 'l':
            newWord.append('#')
        elif letter == 'm':
            newWord.append('g')
        elif letter == 'n':
            newWord.append('4')
        elif letter == 'o':
            newWord.append('C')
        elif letter == 'p':
            newWord.append('W')
        elif letter == 'q':
            newWord.append('}')
        elif letter == 'r':
            newWord.append('k')
        elif letter == 's':
            newWord.append('F')
        elif letter == 't':
            newWord.append('z')
        elif letter == 'u':
            newWord.append('-')
        elif letter == 'v':
            newWord.append('=')
        elif letter == 'w':
            newWord.append('E')
        elif letter == 'x':
            newWord.append('>')
        elif letter == 'y':
            newWord.append('2')
        elif letter == 'z':
            newWord.append('B')
        elif letter == '1':
            newWord.append('*')
        elif letter == '2':
            newWord.append('r')
        elif letter == '3':
            newWord.append('~')
        elif letter == '4':
            newWord.append('9')
        elif letter == '5':
            newWord.append('D')
        elif letter == '6':
            newWord.append('0')
        elif letter == '7':
            newWord.append('K')
        elif letter == '8':
            newWord.append('p')
        elif letter == '9':
            newWord.append('o')
        elif letter == '0':
            newWord.append('^')
        elif letter == '!':
            newWord.append('d')
        elif letter == '@':
            newWord.append(',')
        elif letter == '#':
            newWord.append(':')
        elif letter == '$':
            newWord.append('X')
        elif letter == '%':
            newWord.append('t')
        elif letter == '^':
            newWord.append('q')
        elif letter == '&':
            newWord.append(' ')
        elif letter == '*':
            newWord.append('w')
        elif letter == '(':
            newWord.append('Y')
        elif letter == ')':
            newWord.append('m')
        elif letter == '-':
            newWord.append('U')
        elif letter == '_':
            newWord.append('f')
        elif letter == '+':
            newWord.append('c')
        elif letter == '=':
            newWord.append('y')
        elif letter == '`':
            newWord.append('v')
        elif letter == '~':
            newWord.append('_')
        elif letter == '[':
            newWord.append(']')
        elif letter == ']':
            newWord.append('[')
        elif letter == '{':
            newWord.append('+')
        elif letter == '}':
            newWord.append('h')
        elif letter == '|':
            newWord.append('3')
        elif letter == ':':
            newWord.append('T')
        elif letter == ',':
            newWord.append('?')
        elif letter == '<':
            newWord.append('|')
        elif letter == '.':
            newWord.append('s')
        elif letter == '>':
            newWord.append('G')
        elif letter == '/':
            newWord.append('&')
        elif letter == '?':
            newWord.append('R')
        elif letter == ' ':
            newWord.append('5')
    Switched: str  = ''.join(newWord)
    return Switched

def Q_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'H':
            newWord.append('A')
        elif letter == '(':
            newWord.append('B')
        elif letter == 'e':
            newWord.append('C')
        elif letter == 'i':
            newWord.append('D')
        elif letter == 'V':
            newWord.append('E')
        elif letter == 'n':
            newWord.append('F')
        elif letter == '{':
            newWord.append('G')
        elif letter == '6':
            newWord.append('H')
        elif letter == 'O':
            newWord.append('I')
        elif letter == '1':
            newWord.append('J')
        elif letter == 'L':
            newWord.append('K')
        elif letter == 'x':
            newWord.append('L')
        elif letter == 'J':
            newWord.append('M')
        elif letter == '8':
            newWord.append('N')
        elif letter == '7':
            newWord.append('O')
        elif letter == '@':
            newWord.append('P')
        elif letter == '!':
            newWord.append('Q')
        elif letter == 'A':
            newWord.append('R')
        elif letter == '<':
            newWord.append('S')
        elif letter == 'b':
            newWord.append('T')
        elif letter == '.':
            newWord.append('U')
        elif letter == '%':
            newWord.append('V')
        elif letter == '`':
            newWord.append('W')
        elif letter == 'I':
            newWord.append('X')
        elif letter == 'Q':
            newWord.append('Y')
        elif letter == 'u':
            newWord.append('Z')
        elif letter == 'S':
            newWord.append('a')
        elif letter == 'P':
            newWord.append('b')
        elif letter == 'j':
            newWord.append('c')
        elif letter == 'N':
            newWord.append('d')
        elif letter == '/':
            newWord.append('e')
        elif letter == 'Z':
            newWord.append('f')
        elif letter == 'l':
            newWord.append('g')
        elif letter == 'M':
            newWord.append('h')
        elif letter == '$':
            newWord.append('i')
        elif letter == 'a':
            newWord.append('j')
        elif letter == ')':
            newWord.append('k')
        elif letter == '#':
            newWord.append('l')
        elif letter == 'g':
            newWord.append('m')
        elif letter == '4':
            newWord.append('n')
        elif letter == 'C':
            newWord.append('o')
        elif letter == 'W':
            newWord.append('p')
        elif letter == '}':
            newWord.append('q')
        elif letter == 'k':
            newWord.append('r')
        elif letter == 'F':
            newWord.append('s')
        elif letter == 'z':
            newWord.append('t')
        elif letter == '-':
            newWord.append('u')
        elif letter == '=':
            newWord.append('v')
        elif letter == 'E':
            newWord.append('w')
        elif letter == '>':
            newWord.append('x')
        elif letter == '2':
            newWord.append('y')
        elif letter == 'B':
            newWord.append('z')
        elif letter == '*':
            newWord.append('1')
        elif letter == 'r':
            newWord.append('2')
        elif letter == '~':
            newWord.append('3')
        elif letter == '9':
            newWord.append('4')
        elif letter == 'D':
            newWord.append('5')
        elif letter == '0':
            newWord.append('6')
        elif letter == 'K':
            newWord.append('7')
        elif letter == 'p':
            newWord.append('8')
        elif letter == 'o':
            newWord.append('9')
        elif letter == '^':
            newWord.append('0')
        elif letter == 'd':
            newWord.append('!')
        elif letter == ',':
            newWord.append('@')
        elif letter == ':':
            newWord.append('#')
        elif letter == 'X':
            newWord.append('$')
        elif letter == 't':
            newWord.append('%')
        elif letter == 'q':
            newWord.append('^')
        elif letter == ' ':
            newWord.append('&')
        elif letter == 'w':
            newWord.append('*')
        elif letter == 'Y':
            newWord.append('(')
        elif letter == 'm':
            newWord.append(')')
        elif letter == 'U':
            newWord.append('-')
        elif letter == 'f':
            newWord.append('_')
        elif letter == 'c':
            newWord.append('+')
        elif letter == 'y':
            newWord.append('=')
        elif letter == 'v':
            newWord.append('`')
        elif letter == '_':
            newWord.append('~')
        elif letter == ']':
            newWord.append('[')
        elif letter == '[':
            newWord.append(']')
        elif letter == '+':
            newWord.append('{')
        elif letter == 'h':
            newWord.append('}')
        elif letter == '3':
            newWord.append('|')
        elif letter == 'T':
            newWord.append(':')
        elif letter == '?':
            newWord.append(',')
        elif letter == '|':
            newWord.append('<')
        elif letter == 's':
            newWord.append('.')
        elif letter == 'G':
            newWord.append('>')
        elif letter == '&':
            newWord.append('/')
        elif letter == 'R':
            newWord.append('?')
        elif letter == '5':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def R_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('|')
        elif letter == 'B':
            newWord.append('X')
        elif letter == 'C':
            newWord.append(' ')
        elif letter == 'D':
            newWord.append('w')
        elif letter == 'E':
            newWord.append('g')
        elif letter == 'F':
            newWord.append('B')
        elif letter == 'G':
            newWord.append('1')
        elif letter == 'H':
            newWord.append('o')
        elif letter == 'I':
            newWord.append('^')
        elif letter == 'J':
            newWord.append('~')
        elif letter == 'K':
            newWord.append('r')
        elif letter == 'L':
            newWord.append(',')
        elif letter == 'M':
            newWord.append('G')
        elif letter == 'N':
            newWord.append('u')
        elif letter == 'O':
            newWord.append('h')
        elif letter == 'P':
            newWord.append('2')
        elif letter == 'Q':
            newWord.append('m')
        elif letter == 'R':
            newWord.append('>')
        elif letter == 'S':
            newWord.append('c')
        elif letter == 'T':
            newWord.append('&')
        elif letter == 'U':
            newWord.append('i')
        elif letter == 'V':
            newWord.append(')')
        elif letter == 'W':
            newWord.append('<')
        elif letter == 'X':
            newWord.append('D')
        elif letter == 'Y':
            newWord.append('N')
        elif letter == 'Z':
            newWord.append('$')
        elif letter == 'a':
            newWord.append('y')
        elif letter == 'b':
            newWord.append('5')
        elif letter == 'c':
            newWord.append('f')
        elif letter == 'd':
            newWord.append('l')
        elif letter == 'e':
            newWord.append(']')
        elif letter == 'f':
            newWord.append('z')
        elif letter == 'g':
            newWord.append('O')
        elif letter == 'h':
            newWord.append('}')
        elif letter == 'i':
            newWord.append('!')
        elif letter == 'j':
            newWord.append('`')
        elif letter == 'k':
            newWord.append('T')
        elif letter == 'l':
            newWord.append('Y')
        elif letter == 'm':
            newWord.append('C')
        elif letter == 'n':
            newWord.append('I')
        elif letter == 'o':
            newWord.append('*')
        elif letter == 'p':
            newWord.append('4')
        elif letter == 'q':
            newWord.append('.')
        elif letter == 'r':
            newWord.append('J')
        elif letter == 's':
            newWord.append('s')
        elif letter == 't':
            newWord.append(':')
        elif letter == 'u':
            newWord.append('/')
        elif letter == 'v':
            newWord.append('v')
        elif letter == 'w':
            newWord.append('Q')
        elif letter == 'x':
            newWord.append('x')
        elif letter == 'y':
            newWord.append('E')
        elif letter == 'z':
            newWord.append('p')
        elif letter == '1':
            newWord.append('H')
        elif letter == '2':
            newWord.append('n')
        elif letter == '3':
            newWord.append('t')
        elif letter == '4':
            newWord.append('j')
        elif letter == '5':
            newWord.append('?')
        elif letter == '6':
            newWord.append('L')
        elif letter == '7':
            newWord.append('P')
        elif letter == '8':
            newWord.append('U')
        elif letter == '9':
            newWord.append('F')
        elif letter == '0':
            newWord.append('V')
        elif letter == '!':
            newWord.append('7')
        elif letter == '@':
            newWord.append('Z')
        elif letter == '#':
            newWord.append('b')
        elif letter == '$':
            newWord.append('=')
        elif letter == '%':
            newWord.append('3')
        elif letter == '^':
            newWord.append('%')
        elif letter == '&':
            newWord.append('M')
        elif letter == '*':
            newWord.append('8')
        elif letter == '(':
            newWord.append('q')
        elif letter == ')':
            newWord.append('d')
        elif letter == '-':
            newWord.append('(')
        elif letter == '_':
            newWord.append('k')
        elif letter == '+':
            newWord.append('A')
        elif letter == '=':
            newWord.append('S')
        elif letter == '`':
            newWord.append('0')
        elif letter == '~':
            newWord.append('W')
        elif letter == '[':
            newWord.append('_')
        elif letter == ']':
            newWord.append('{')
        elif letter == '{':
            newWord.append('e')
        elif letter == '}':
            newWord.append('a')
        elif letter == '|':
            newWord.append('-')
        elif letter == ':':
            newWord.append('@')
        elif letter == ',':
            newWord.append('9')
        elif letter == '<':
            newWord.append('K')
        elif letter == '.':
            newWord.append('R')
        elif letter == '>':
            newWord.append('#')
        elif letter == '/':
            newWord.append('+')
        elif letter == '?':
            newWord.append('[')
        elif letter == ' ':
            newWord.append('6')
    Switched: str  = ''.join(newWord)
    return Switched

def R_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '|':
            newWord.append('A')
        elif letter == 'X':
            newWord.append('B')
        elif letter == ' ':
            newWord.append('C')
        elif letter == 'w':
            newWord.append('D')
        elif letter == 'g':
            newWord.append('E')
        elif letter == 'B':
            newWord.append('F')
        elif letter == '1':
            newWord.append('G')
        elif letter == 'o':
            newWord.append('H')
        elif letter == '^':
            newWord.append('I')
        elif letter == '~':
            newWord.append('J')
        elif letter == 'r':
            newWord.append('K')
        elif letter == ',':
            newWord.append('L')
        elif letter == 'G':
            newWord.append('M')
        elif letter == 'u':
            newWord.append('N')
        elif letter == 'h':
            newWord.append('O')
        elif letter == '2':
            newWord.append('P')
        elif letter == 'm':
            newWord.append('Q')
        elif letter == '>':
            newWord.append('R')
        elif letter == 'c':
            newWord.append('S')
        elif letter == '&':
            newWord.append('T')
        elif letter == 'i':
            newWord.append('U')
        elif letter == ')':
            newWord.append('V')
        elif letter == '<':
            newWord.append('W')
        elif letter == 'D':
            newWord.append('X')
        elif letter == 'N':
            newWord.append('Y')
        elif letter == '$':
            newWord.append('Z')
        elif letter == 'y':
            newWord.append('a')
        elif letter == '5':
            newWord.append('b')
        elif letter == 'f':
            newWord.append('c')
        elif letter == 'l':
            newWord.append('d')
        elif letter == ']':
            newWord.append('e')
        elif letter == 'z':
            newWord.append('f')
        elif letter == 'O':
            newWord.append('g')
        elif letter == '}':
            newWord.append('h')
        elif letter == '!':
            newWord.append('i')
        elif letter == '`':
            newWord.append('j')
        elif letter == 'T':
            newWord.append('k')
        elif letter == 'Y':
            newWord.append('l')
        elif letter == 'C':
            newWord.append('m')
        elif letter == 'I':
            newWord.append('n')
        elif letter == '*':
            newWord.append('o')
        elif letter == '4':
            newWord.append('p')
        elif letter == '.':
            newWord.append('q')
        elif letter == 'J':
            newWord.append('r')
        elif letter == 's':
            newWord.append('s')
        elif letter == ':':
            newWord.append('t')
        elif letter == '/':
            newWord.append('u')
        elif letter == 'v':
            newWord.append('v')
        elif letter == 'Q':
            newWord.append('w')
        elif letter == 'x':
            newWord.append('x')
        elif letter == 'E':
            newWord.append('y')
        elif letter == 'p':
            newWord.append('z')
        elif letter == 'H':
            newWord.append('1')
        elif letter == 'n':
            newWord.append('2')
        elif letter == 't':
            newWord.append('3')
        elif letter == 'j':
            newWord.append('4')
        elif letter == '?':
            newWord.append('5')
        elif letter == 'L':
            newWord.append('6')
        elif letter == 'P':
            newWord.append('7')
        elif letter == 'U':
            newWord.append('8')
        elif letter == 'F':
            newWord.append('9')
        elif letter == 'V':
            newWord.append('0')
        elif letter == '7':
            newWord.append('!')
        elif letter == 'Z':
            newWord.append('@')
        elif letter == 'b':
            newWord.append('#')
        elif letter == '=':
            newWord.append('$')
        elif letter == '3':
            newWord.append('%')
        elif letter == '%':
            newWord.append('^')
        elif letter == 'M':
            newWord.append('&')
        elif letter == '8':
            newWord.append('*')
        elif letter == 'q':
            newWord.append('(')
        elif letter == 'd':
            newWord.append(')')
        elif letter == '(':
            newWord.append('-')
        elif letter == 'k':
            newWord.append('_')
        elif letter == 'A':
            newWord.append('+')
        elif letter == 'S':
            newWord.append('=')
        elif letter == '0':
            newWord.append('`')
        elif letter == 'W':
            newWord.append('~')
        elif letter == '_':
            newWord.append('[')
        elif letter == '{':
            newWord.append(']')
        elif letter == 'e':
            newWord.append('{')
        elif letter == 'a':
            newWord.append('}')
        elif letter == '-':
            newWord.append('|')
        elif letter == '@':
            newWord.append(':')
        elif letter == '9':
            newWord.append(',')
        elif letter == 'K':
            newWord.append('<')
        elif letter == 'R':
            newWord.append('.')
        elif letter == '#':
            newWord.append('>')
        elif letter == '+':
            newWord.append('/')
        elif letter == '[':
            newWord.append('?')
        elif letter == '6':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def S_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('9')
        elif letter == 'B':
            newWord.append('2')
        elif letter == 'C':
            newWord.append('q')
        elif letter == 'D':
            newWord.append('Q')
        elif letter == 'E':
            newWord.append('I')
        elif letter == 'F':
            newWord.append(',')
        elif letter == 'G':
            newWord.append('&')
        elif letter == 'H':
            newWord.append('C')
        elif letter == 'I':
            newWord.append('X')
        elif letter == 'J':
            newWord.append('|')
        elif letter == 'K':
            newWord.append('%')
        elif letter == 'L':
            newWord.append(')')
        elif letter == 'M':
            newWord.append('s')
        elif letter == 'N':
            newWord.append('S')
        elif letter == 'O':
            newWord.append('f')
        elif letter == 'P':
            newWord.append('=')
        elif letter == 'Q':
            newWord.append('#')
        elif letter == 'R':
            newWord.append('m')
        elif letter == 'S':
            newWord.append('<')
        elif letter == 'T':
            newWord.append('n')
        elif letter == 'U':
            newWord.append('E')
        elif letter == 'V':
            newWord.append('a')
        elif letter == 'W':
            newWord.append('/')
        elif letter == 'X':
            newWord.append('O')
        elif letter == 'Y':
            newWord.append('x')
        elif letter == 'Z':
            newWord.append('{')
        elif letter == 'a':
            newWord.append('r')
        elif letter == 'b':
            newWord.append('B')
        elif letter == 'c':
            newWord.append('>')
        elif letter == 'd':
            newWord.append(']')
        elif letter == 'e':
            newWord.append('!')
        elif letter == 'f':
            newWord.append('8')
        elif letter == 'g':
            newWord.append('P')
        elif letter == 'h':
            newWord.append('_')
        elif letter == 'i':
            newWord.append('o')
        elif letter == 'j':
            newWord.append('j')
        elif letter == 'k':
            newWord.append('g')
        elif letter == 'l':
            newWord.append('$')
        elif letter == 'm':
            newWord.append('}')
        elif letter == 'n':
            newWord.append('A')
        elif letter == 'o':
            newWord.append('T')
        elif letter == 'p':
            newWord.append('K')
        elif letter == 'q':
            newWord.append('v')
        elif letter == 'r':
            newWord.append('H')
        elif letter == 's':
            newWord.append('w')
        elif letter == 't':
            newWord.append('?')
        elif letter == 'u':
            newWord.append('[')
        elif letter == 'v':
            newWord.append('h')
        elif letter == 'w':
            newWord.append('R')
        elif letter == 'x':
            newWord.append('^')
        elif letter == 'y':
            newWord.append('e')
        elif letter == 'z':
            newWord.append('5')
        elif letter == '1':
            newWord.append('-')
        elif letter == '2':
            newWord.append('.')
        elif letter == '3':
            newWord.append('Z')
        elif letter == '4':
            newWord.append('U')
        elif letter == '5':
            newWord.append('3')
        elif letter == '6':
            newWord.append('7')
        elif letter == '7':
            newWord.append('c')
        elif letter == '8':
            newWord.append('N')
        elif letter == '9':
            newWord.append(' ')
        elif letter == '0':
            newWord.append('M')
        elif letter == '!':
            newWord.append('d')
        elif letter == '@':
            newWord.append('+')
        elif letter == '#':
            newWord.append('b')
        elif letter == '$':
            newWord.append('@')
        elif letter == '%':
            newWord.append('`')
        elif letter == '^':
            newWord.append('(')
        elif letter == '&':
            newWord.append('~')
        elif letter == '*':
            newWord.append('0')
        elif letter == '(':
            newWord.append('W')
        elif letter == ')':
            newWord.append(':')
        elif letter == '-':
            newWord.append('p')
        elif letter == '_':
            newWord.append('k')
        elif letter == '+':
            newWord.append('1')
        elif letter == '=':
            newWord.append('y')
        elif letter == '`':
            newWord.append('6')
        elif letter == '~':
            newWord.append('G')
        elif letter == '[':
            newWord.append('L')
        elif letter == ']':
            newWord.append('4')
        elif letter == '{':
            newWord.append('*')
        elif letter == '}':
            newWord.append('J')
        elif letter == '|':
            newWord.append('t')
        elif letter == ':':
            newWord.append('D')
        elif letter == ',':
            newWord.append('Y')
        elif letter == '<':
            newWord.append('V')
        elif letter == '.':
            newWord.append('F')
        elif letter == '>':
            newWord.append('l')
        elif letter == '/':
            newWord.append('z')
        elif letter == '?':
            newWord.append('i')
        elif letter == ' ':
            newWord.append('u')
    Switched: str  = ''.join(newWord)
    return Switched

def S_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '9':
            newWord.append('A')
        elif letter == '2':
            newWord.append('B')
        elif letter == 'q':
            newWord.append('C')
        elif letter == 'Q':
            newWord.append('D')
        elif letter == 'I':
            newWord.append('E')
        elif letter == ',':
            newWord.append('F')
        elif letter == '&':
            newWord.append('G')
        elif letter == 'C':
            newWord.append('H')
        elif letter == 'X':
            newWord.append('I')
        elif letter == '|':
            newWord.append('J')
        elif letter == '%':
            newWord.append('K')
        elif letter == ')':
            newWord.append('L')
        elif letter == 's':
            newWord.append('M')
        elif letter == 'S':
            newWord.append('N')
        elif letter == 'f':
            newWord.append('O')
        elif letter == '=':
            newWord.append('P')
        elif letter == '#':
            newWord.append('Q')
        elif letter == 'm':
            newWord.append('R')
        elif letter == '<':
            newWord.append('S')
        elif letter == 'n':
            newWord.append('T')
        elif letter == 'E':
            newWord.append('U')
        elif letter == 'a':
            newWord.append('V')
        elif letter == '/':
            newWord.append('W')
        elif letter == 'O':
            newWord.append('X')
        elif letter == 'x':
            newWord.append('Y')
        elif letter == '{':
            newWord.append('Z')
        elif letter == 'r':
            newWord.append('a')
        elif letter == 'B':
            newWord.append('b')
        elif letter == '>':
            newWord.append('c')
        elif letter == ']':
            newWord.append('d')
        elif letter == '!':
            newWord.append('e')
        elif letter == '8':
            newWord.append('f')
        elif letter == 'P':
            newWord.append('g')
        elif letter == '_':
            newWord.append('h')
        elif letter == 'o':
            newWord.append('i')
        elif letter == 'j':
            newWord.append('j')
        elif letter == 'g':
            newWord.append('k')
        elif letter == '$':
            newWord.append('l')
        elif letter == '}':
            newWord.append('m')
        elif letter == 'A':
            newWord.append('n')
        elif letter == 'T':
            newWord.append('o')
        elif letter == 'K':
            newWord.append('p')
        elif letter == 'v':
            newWord.append('q')
        elif letter == 'H':
            newWord.append('r')
        elif letter == 'w':
            newWord.append('s')
        elif letter == '?':
            newWord.append('t')
        elif letter == '[':
            newWord.append('u')
        elif letter == 'h':
            newWord.append('v')
        elif letter == 'R':
            newWord.append('w')
        elif letter == '^':
            newWord.append('x')
        elif letter == 'e':
            newWord.append('y')
        elif letter == '5':
            newWord.append('z')
        elif letter == '-':
            newWord.append('1')
        elif letter == '.':
            newWord.append('2')
        elif letter == 'Z':
            newWord.append('3')
        elif letter == 'U':
            newWord.append('4')
        elif letter == '3':
            newWord.append('5')
        elif letter == '7':
            newWord.append('6')
        elif letter == 'c':
            newWord.append('7')
        elif letter == 'N':
            newWord.append('8')
        elif letter == ' ':
            newWord.append('9')
        elif letter == 'M':
            newWord.append('0')
        elif letter == 'd':
            newWord.append('!')
        elif letter == '+':
            newWord.append('@')
        elif letter == 'b':
            newWord.append('#')
        elif letter == '@':
            newWord.append('$')
        elif letter == '`':
            newWord.append('%')
        elif letter == '(':
            newWord.append('^')
        elif letter == '~':
            newWord.append('&')
        elif letter == '0':
            newWord.append('*')
        elif letter == 'W':
            newWord.append('(')
        elif letter == ':':
            newWord.append(')')
        elif letter == 'p':
            newWord.append('-')
        elif letter == 'k':
            newWord.append('_')
        elif letter == '1':
            newWord.append('+')
        elif letter == 'y':
            newWord.append('=')
        elif letter == '6':
            newWord.append('`')
        elif letter == 'G':
            newWord.append('~')
        elif letter == 'L':
            newWord.append('[')
        elif letter == '4':
            newWord.append(']')
        elif letter == '*':
            newWord.append('{')
        elif letter == 'J':
            newWord.append('}')
        elif letter == 't':
            newWord.append('|')
        elif letter == 'D':
            newWord.append(':')
        elif letter == 'Y':
            newWord.append(',')
        elif letter == 'V':
            newWord.append('<')
        elif letter == 'F':
            newWord.append('.')
        elif letter == 'l':
            newWord.append('>')
        elif letter == 'z':
            newWord.append('/')
        elif letter == 'i':
            newWord.append('?')
        elif letter == 'u':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def T_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('[')
        elif letter == 'B':
            newWord.append(',')
        elif letter == 'C':
            newWord.append('b')
        elif letter == 'D':
            newWord.append('+')
        elif letter == 'E':
            newWord.append('2')
        elif letter == 'F':
            newWord.append('|')
        elif letter == 'G':
            newWord.append('4')
        elif letter == 'H':
            newWord.append('S')
        elif letter == 'I':
            newWord.append('d')
        elif letter == 'J':
            newWord.append('I')
        elif letter == 'K':
            newWord.append('G')
        elif letter == 'L':
            newWord.append('D')
        elif letter == 'M':
            newWord.append('E')
        elif letter == 'N':
            newWord.append('W')
        elif letter == 'O':
            newWord.append('9')
        elif letter == 'P':
            newWord.append('6')
        elif letter == 'Q':
            newWord.append('J')
        elif letter == 'R':
            newWord.append('}')
        elif letter == 'S':
            newWord.append('.')
        elif letter == 'T':
            newWord.append('%')
        elif letter == 'U':
            newWord.append('L')
        elif letter == 'V':
            newWord.append('8')
        elif letter == 'W':
            newWord.append('w')
        elif letter == 'X':
            newWord.append('!')
        elif letter == 'Y':
            newWord.append('(')
        elif letter == 'Z':
            newWord.append(':')
        elif letter == 'a':
            newWord.append('1')
        elif letter == 'b':
            newWord.append('N')
        elif letter == 'c':
            newWord.append('q')
        elif letter == 'd':
            newWord.append('Q')
        elif letter == 'e':
            newWord.append('B')
        elif letter == 'f':
            newWord.append('o')
        elif letter == 'g':
            newWord.append('O')
        elif letter == 'h':
            newWord.append('~')
        elif letter == 'i':
            newWord.append(']')
        elif letter == 'j':
            newWord.append('=')
        elif letter == 'k':
            newWord.append('$')
        elif letter == 'l':
            newWord.append('#')
        elif letter == 'm':
            newWord.append('@')
        elif letter == 'n':
            newWord.append('<')
        elif letter == 'o':
            newWord.append('i')
        elif letter == 'p':
            newWord.append('C')
        elif letter == 'q':
            newWord.append(' ')
        elif letter == 'r':
            newWord.append('n')
        elif letter == 's':
            newWord.append('p')
        elif letter == 't':
            newWord.append(')')
        elif letter == 'u':
            newWord.append('t')
        elif letter == 'v':
            newWord.append('a')
        elif letter == 'w':
            newWord.append('x')
        elif letter == 'x':
            newWord.append('&')
        elif letter == 'y':
            newWord.append('{')
        elif letter == 'z':
            newWord.append('_')
        elif letter == '1':
            newWord.append('h')
        elif letter == '2':
            newWord.append('V')
        elif letter == '3':
            newWord.append('g')
        elif letter == '4':
            newWord.append('Y')
        elif letter == '5':
            newWord.append('M')
        elif letter == '6':
            newWord.append('m')
        elif letter == '7':
            newWord.append('5')
        elif letter == '8':
            newWord.append('7')
        elif letter == '9':
            newWord.append('?')
        elif letter == '0':
            newWord.append('y')
        elif letter == '!':
            newWord.append('e')
        elif letter == '@':
            newWord.append('Z')
        elif letter == '#':
            newWord.append('H')
        elif letter == '$':
            newWord.append('u')
        elif letter == '%':
            newWord.append('^')
        elif letter == '^':
            newWord.append('/')
        elif letter == '&':
            newWord.append('A')
        elif letter == '*':
            newWord.append('T')
        elif letter == '(':
            newWord.append('X')
        elif letter == ')':
            newWord.append('R')
        elif letter == '-':
            newWord.append('0')
        elif letter == '_':
            newWord.append('U')
        elif letter == '+':
            newWord.append('>')
        elif letter == '=':
            newWord.append('P')
        elif letter == '`':
            newWord.append('j')
        elif letter == '~':
            newWord.append('F')
        elif letter == '[':
            newWord.append('l')
        elif letter == ']':
            newWord.append('K')
        elif letter == '{':
            newWord.append('-')
        elif letter == '}':
            newWord.append('v')
        elif letter == '|':
            newWord.append('*')
        elif letter == ':':
            newWord.append('`')
        elif letter == ',':
            newWord.append('r')
        elif letter == '<':
            newWord.append('z')
        elif letter == '.':
            newWord.append('c')
        elif letter == '>':
            newWord.append('f')
        elif letter == '/':
            newWord.append('s')
        elif letter == '?':
            newWord.append('3')
        elif letter == ' ':
            newWord.append('k')
    Switched: str  = ''.join(newWord)
    return Switched

def T_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '[':
            newWord.append('A')
        elif letter == ',':
            newWord.append('B')
        elif letter == 'b':
            newWord.append('C')
        elif letter == '+':
            newWord.append('D')
        elif letter == '2':
            newWord.append('E')
        elif letter == '|':
            newWord.append('F')
        elif letter == '4':
            newWord.append('G')
        elif letter == 'S':
            newWord.append('H')
        elif letter == 'd':
            newWord.append('I')
        elif letter == 'I':
            newWord.append('J')
        elif letter == 'G':
            newWord.append('K')
        elif letter == 'D':
            newWord.append('L')
        elif letter == 'E':
            newWord.append('M')
        elif letter == 'W':
            newWord.append('N')
        elif letter == '9':
            newWord.append('O')
        elif letter == '6':
            newWord.append('P')
        elif letter == 'J':
            newWord.append('Q')
        elif letter == '}':
            newWord.append('R')
        elif letter == '.':
            newWord.append('S')
        elif letter == '%':
            newWord.append('T')
        elif letter == 'L':
            newWord.append('U')
        elif letter == '8':
            newWord.append('V')
        elif letter == 'w':
            newWord.append('W')
        elif letter == '!':
            newWord.append('X')
        elif letter == '(':
            newWord.append('Y')
        elif letter == ':':
            newWord.append('Z')
        elif letter == '1':
            newWord.append('a')
        elif letter == 'N':
            newWord.append('b')
        elif letter == 'q':
            newWord.append('c')
        elif letter == 'Q':
            newWord.append('d')
        elif letter == 'B':
            newWord.append('e')
        elif letter == 'o':
            newWord.append('f')
        elif letter == 'O':
            newWord.append('g')
        elif letter == '~':
            newWord.append('h')
        elif letter == ']':
            newWord.append('i')
        elif letter == '=':
            newWord.append('j')
        elif letter == '$':
            newWord.append('k')
        elif letter == '#':
            newWord.append('l')
        elif letter == '@':
            newWord.append('m')
        elif letter == '<':
            newWord.append('n')
        elif letter == 'i':
            newWord.append('o')
        elif letter == 'C':
            newWord.append('p')
        elif letter == ' ':
            newWord.append('q')
        elif letter == 'n':
            newWord.append('r')
        elif letter == 'p':
            newWord.append('s')
        elif letter == ')':
            newWord.append('t')
        elif letter == 't':
            newWord.append('u')
        elif letter == 'a':
            newWord.append('v')
        elif letter == 'x':
            newWord.append('w')
        elif letter == '&':
            newWord.append('x')
        elif letter == '{':
            newWord.append('y')
        elif letter == '_':
            newWord.append('z')
        elif letter == 'h':
            newWord.append('1')
        elif letter == 'V':
            newWord.append('2')
        elif letter == 'g':
            newWord.append('3')
        elif letter == 'Y':
            newWord.append('4')
        elif letter == 'M':
            newWord.append('5')
        elif letter == 'm':
            newWord.append('6')
        elif letter == '5':
            newWord.append('7')
        elif letter == '7':
            newWord.append('8')
        elif letter == '?':
            newWord.append('9')
        elif letter == 'y':
            newWord.append('0')
        elif letter == 'e':
            newWord.append('!')
        elif letter == 'Z':
            newWord.append('@')
        elif letter == 'H':
            newWord.append('#')
        elif letter == 'u':
            newWord.append('$')
        elif letter == '^':
            newWord.append('%')
        elif letter == '/':
            newWord.append('^')
        elif letter == 'A':
            newWord.append('&')
        elif letter == 'T':
            newWord.append('*')
        elif letter == 'X':
            newWord.append('(')
        elif letter == 'R':
            newWord.append(')')
        elif letter == '0':
            newWord.append('-')
        elif letter == 'U':
            newWord.append('_')
        elif letter == '>':
            newWord.append('+')
        elif letter == 'P':
            newWord.append('=')
        elif letter == 'j':
            newWord.append('`')
        elif letter == 'F':
            newWord.append('~')
        elif letter == 'l':
            newWord.append('[')
        elif letter == 'K':
            newWord.append(']')
        elif letter == '-':
            newWord.append('{')
        elif letter == 'v':
            newWord.append('}')
        elif letter == '*':
            newWord.append('|')
        elif letter == '`':
            newWord.append(':')
        elif letter == 'r':
            newWord.append(',')
        elif letter == 'z':
            newWord.append('<')
        elif letter == 'c':
            newWord.append('.')
        elif letter == 'f':
            newWord.append('>')
        elif letter == 's':
            newWord.append('/')
        elif letter == '3':
            newWord.append('?')
        elif letter == 'k':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def U_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('A')
        elif letter == 'B':
            newWord.append('.')
        elif letter == 'C':
            newWord.append('2')
        elif letter == 'D':
            newWord.append('}')
        elif letter == 'E':
            newWord.append('v')
        elif letter == 'F':
            newWord.append('G')
        elif letter == 'G':
            newWord.append('e')
        elif letter == 'H':
            newWord.append('6')
        elif letter == 'I':
            newWord.append('0')
        elif letter == 'J':
            newWord.append('u')
        elif letter == 'K':
            newWord.append('/')
        elif letter == 'L':
            newWord.append('l')
        elif letter == 'M':
            newWord.append('=')
        elif letter == 'N':
            newWord.append('@')
        elif letter == 'O':
            newWord.append('(')
        elif letter == 'P':
            newWord.append('g')
        elif letter == 'Q':
            newWord.append(')')
        elif letter == 'R':
            newWord.append('C')
        elif letter == 'S':
            newWord.append('J')
        elif letter == 'T':
            newWord.append('z')
        elif letter == 'U':
            newWord.append('&')
        elif letter == 'V':
            newWord.append(':')
        elif letter == 'W':
            newWord.append('+')
        elif letter == 'X':
            newWord.append(']')
        elif letter == 'Y':
            newWord.append('S')
        elif letter == 'Z':
            newWord.append('x')
        elif letter == 'a':
            newWord.append('I')
        elif letter == 'b':
            newWord.append('~')
        elif letter == 'c':
            newWord.append('n')
        elif letter == 'd':
            newWord.append('7')
        elif letter == 'e':
            newWord.append('Q')
        elif letter == 'f':
            newWord.append('{')
        elif letter == 'g':
            newWord.append('<')
        elif letter == 'h':
            newWord.append('3')
        elif letter == 'i':
            newWord.append('o')
        elif letter == 'j':
            newWord.append('R')
        elif letter == 'k':
            newWord.append('M')
        elif letter == 'l':
            newWord.append('Y')
        elif letter == 'm':
            newWord.append('$')
        elif letter == 'n':
            newWord.append('>')
        elif letter == 'o':
            newWord.append('^')
        elif letter == 'p':
            newWord.append('Z')
        elif letter == 'q':
            newWord.append('W')
        elif letter == 'r':
            newWord.append('9')
        elif letter == 's':
            newWord.append('[')
        elif letter == 't':
            newWord.append('i')
        elif letter == 'u':
            newWord.append('s')
        elif letter == 'v':
            newWord.append('F')
        elif letter == 'w':
            newWord.append('*')
        elif letter == 'x':
            newWord.append('f')
        elif letter == 'y':
            newWord.append('h')
        elif letter == 'z':
            newWord.append('-')
        elif letter == '1':
            newWord.append('N')
        elif letter == '2':
            newWord.append('O')
        elif letter == '3':
            newWord.append('j')
        elif letter == '4':
            newWord.append('#')
        elif letter == '5':
            newWord.append('D')
        elif letter == '6':
            newWord.append('4')
        elif letter == '7':
            newWord.append('E')
        elif letter == '8':
            newWord.append('!')
        elif letter == '9':
            newWord.append('T')
        elif letter == '0':
            newWord.append('p')
        elif letter == '!':
            newWord.append('8')
        elif letter == '@':
            newWord.append('V')
        elif letter == '#':
            newWord.append('a')
        elif letter == '$':
            newWord.append('5')
        elif letter == '%':
            newWord.append('L')
        elif letter == '^':
            newWord.append('`')
        elif letter == '&':
            newWord.append('%')
        elif letter == '*':
            newWord.append('d')
        elif letter == '(':
            newWord.append('t')
        elif letter == ')':
            newWord.append('k')
        elif letter == '-':
            newWord.append(',')
        elif letter == '_':
            newWord.append('_')
        elif letter == '+':
            newWord.append('c')
        elif letter == '=':
            newWord.append('K')
        elif letter == '`':
            newWord.append('|')
        elif letter == '~':
            newWord.append('U')
        elif letter == '[':
            newWord.append('1')
        elif letter == ']':
            newWord.append('y')
        elif letter == '{':
            newWord.append(' ')
        elif letter == '}':
            newWord.append('m')
        elif letter == '|':
            newWord.append('q')
        elif letter == ':':
            newWord.append('b')
        elif letter == ',':
            newWord.append('X')
        elif letter == '<':
            newWord.append('H')
        elif letter == '.':
            newWord.append('r')
        elif letter == '>':
            newWord.append('P')
        elif letter == '/':
            newWord.append('w')
        elif letter == '?':
            newWord.append('B')
        elif letter == ' ':
            newWord.append('?')
    Switched: str  = ''.join(newWord)
    return Switched

def U_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('A')
        elif letter == '.':
            newWord.append('B')
        elif letter == '2':
            newWord.append('C')
        elif letter == '}':
            newWord.append('D')
        elif letter == 'v':
            newWord.append('E')
        elif letter == 'G':
            newWord.append('F')
        elif letter == 'e':
            newWord.append('G')
        elif letter == '6':
            newWord.append('H')
        elif letter == '0':
            newWord.append('I')
        elif letter == 'u':
            newWord.append('J')
        elif letter == '/':
            newWord.append('K')
        elif letter == 'l':
            newWord.append('L')
        elif letter == '=':
            newWord.append('M')
        elif letter == '@':
            newWord.append('N')
        elif letter == '(':
            newWord.append('O')
        elif letter == 'g':
            newWord.append('P')
        elif letter == ')':
            newWord.append('Q')
        elif letter == 'C':
            newWord.append('R')
        elif letter == 'J':
            newWord.append('S')
        elif letter == 'z':
            newWord.append('T')
        elif letter == '&':
            newWord.append('U')
        elif letter == ':':
            newWord.append('V')
        elif letter == '+':
            newWord.append('W')
        elif letter == ']':
            newWord.append('X')
        elif letter == 'S':
            newWord.append('Y')
        elif letter == 'x':
            newWord.append('Z')
        elif letter == 'I':
            newWord.append('a')
        elif letter == '~':
            newWord.append('b')
        elif letter == 'n':
            newWord.append('c')
        elif letter == '7':
            newWord.append('d')
        elif letter == 'Q':
            newWord.append('e')
        elif letter == '{':
            newWord.append('f')
        elif letter == '<':
            newWord.append('g')
        elif letter == '3':
            newWord.append('h')
        elif letter == 'o':
            newWord.append('i')
        elif letter == 'R':
            newWord.append('j')
        elif letter == 'M':
            newWord.append('k')
        elif letter == 'Y':
            newWord.append('l')
        elif letter == '$':
            newWord.append('m')
        elif letter == '>':
            newWord.append('n')
        elif letter == '^':
            newWord.append('o')
        elif letter == 'Z':
            newWord.append('p')
        elif letter == 'W':
            newWord.append('q')
        elif letter == '9':
            newWord.append('r')
        elif letter == '[':
            newWord.append('s')
        elif letter == 'i':
            newWord.append('t')
        elif letter == 's':
            newWord.append('u')
        elif letter == 'F':
            newWord.append('v')
        elif letter == '*':
            newWord.append('w')
        elif letter == 'f':
            newWord.append('x')
        elif letter == 'h':
            newWord.append('y')
        elif letter == '-':
            newWord.append('z')
        elif letter == 'N':
            newWord.append('1')
        elif letter == 'O':
            newWord.append('2')
        elif letter == 'j':
            newWord.append('3')
        elif letter == '#':
            newWord.append('4')
        elif letter == 'D':
            newWord.append('5')
        elif letter == '4':
            newWord.append('6')
        elif letter == 'E':
            newWord.append('7')
        elif letter == '!':
            newWord.append('8')
        elif letter == 'T':
            newWord.append('9')
        elif letter == 'p':
            newWord.append('0')
        elif letter == '8':
            newWord.append('!')
        elif letter == 'V':
            newWord.append('@')
        elif letter == 'a':
            newWord.append('#')
        elif letter == '5':
            newWord.append('$')
        elif letter == 'L':
            newWord.append('%')
        elif letter == '`':
            newWord.append('^')
        elif letter == '%':
            newWord.append('&')
        elif letter == 'd':
            newWord.append('*')
        elif letter == 't':
            newWord.append('(')
        elif letter == 'k':
            newWord.append(')')
        elif letter == ',':
            newWord.append('-')
        elif letter == '_':
            newWord.append('_')
        elif letter == 'c':
            newWord.append('+')
        elif letter == 'K':
            newWord.append('=')
        elif letter == '|':
            newWord.append('`')
        elif letter == 'U':
            newWord.append('~')
        elif letter == '1':
            newWord.append('[')
        elif letter == 'y':
            newWord.append(']')
        elif letter == ' ':
            newWord.append('{')
        elif letter == 'm':
            newWord.append('}')
        elif letter == 'q':
            newWord.append('|')
        elif letter == 'b':
            newWord.append(':')
        elif letter == 'X':
            newWord.append(',')
        elif letter == 'H':
            newWord.append('<')
        elif letter == 'r':
            newWord.append('.')
        elif letter == 'P':
            newWord.append('>')
        elif letter == 'w':
            newWord.append('/')
        elif letter == 'B':
            newWord.append('?')
        elif letter == '?':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def V_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('S')
        elif letter == 'B':
            newWord.append('|')
        elif letter == 'C':
            newWord.append('i')
        elif letter == 'D':
            newWord.append('j')
        elif letter == 'E':
            newWord.append('a')
        elif letter == 'F':
            newWord.append('A')
        elif letter == 'G':
            newWord.append(')')
        elif letter == 'H':
            newWord.append('^')
        elif letter == 'I':
            newWord.append('1')
        elif letter == 'J':
            newWord.append('k')
        elif letter == 'K':
            newWord.append('/')
        elif letter == 'L':
            newWord.append('R')
        elif letter == 'M':
            newWord.append('o')
        elif letter == 'N':
            newWord.append('r')
        elif letter == 'O':
            newWord.append('{')
        elif letter == 'P':
            newWord.append('d')
        elif letter == 'Q':
            newWord.append('0')
        elif letter == 'R':
            newWord.append('%')
        elif letter == 'S':
            newWord.append('q')
        elif letter == 'T':
            newWord.append('n')
        elif letter == 'U':
            newWord.append('m')
        elif letter == 'V':
            newWord.append('T')
        elif letter == 'W':
            newWord.append('`')
        elif letter == 'X':
            newWord.append('t')
        elif letter == 'Y':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append(':')
        elif letter == 'a':
            newWord.append('L')
        elif letter == 'b':
            newWord.append('K')
        elif letter == 'c':
            newWord.append('[')
        elif letter == 'd':
            newWord.append('~')
        elif letter == 'e':
            newWord.append('!')
        elif letter == 'f':
            newWord.append('.')
        elif letter == 'g':
            newWord.append('U')
        elif letter == 'h':
            newWord.append('7')
        elif letter == 'i':
            newWord.append('e')
        elif letter == 'j':
            newWord.append('Y')
        elif letter == 'k':
            newWord.append('p')
        elif letter == 'l':
            newWord.append('V')
        elif letter == 'm':
            newWord.append('N')
        elif letter == 'n':
            newWord.append('E')
        elif letter == 'o':
            newWord.append('P')
        elif letter == 'p':
            newWord.append('-')
        elif letter == 'q':
            newWord.append('H')
        elif letter == 'r':
            newWord.append('z')
        elif letter == 's':
            newWord.append('O')
        elif letter == 't':
            newWord.append('8')
        elif letter == 'u':
            newWord.append('<')
        elif letter == 'v':
            newWord.append('$')
        elif letter == 'w':
            newWord.append('F')
        elif letter == 'x':
            newWord.append('Q')
        elif letter == 'y':
            newWord.append('G')
        elif letter == 'z':
            newWord.append(',')
        elif letter == '1':
            newWord.append('(')
        elif letter == '2':
            newWord.append('v')
        elif letter == '3':
            newWord.append(' ')
        elif letter == '4':
            newWord.append('X')
        elif letter == '5':
            newWord.append('W')
        elif letter == '6':
            newWord.append('C')
        elif letter == '7':
            newWord.append(']')
        elif letter == '8':
            newWord.append('l')
        elif letter == '9':
            newWord.append('}')
        elif letter == '0':
            newWord.append('u')
        elif letter == '!':
            newWord.append('=')
        elif letter == '@':
            newWord.append('@')
        elif letter == '#':
            newWord.append('M')
        elif letter == '$':
            newWord.append('x')
        elif letter == '%':
            newWord.append('9')
        elif letter == '^':
            newWord.append('h')
        elif letter == '&':
            newWord.append('?')
        elif letter == '*':
            newWord.append('y')
        elif letter == '(':
            newWord.append('D')
        elif letter == ')':
            newWord.append('_')
        elif letter == '-':
            newWord.append('6')
        elif letter == '_':
            newWord.append('>')
        elif letter == '+':
            newWord.append('4')
        elif letter == '=':
            newWord.append('*')
        elif letter == '`':
            newWord.append('Z')
        elif letter == '~':
            newWord.append('J')
        elif letter == '[':
            newWord.append('f')
        elif letter == ']':
            newWord.append('s')
        elif letter == '{':
            newWord.append('c')
        elif letter == '}':
            newWord.append('5')
        elif letter == '|':
            newWord.append('2')
        elif letter == ':':
            newWord.append('b')
        elif letter == ',':
            newWord.append('B')
        elif letter == '<':
            newWord.append('+')
        elif letter == '.':
            newWord.append('#')
        elif letter == '>':
            newWord.append('&')
        elif letter == '/':
            newWord.append('I')
        elif letter == '?':
            newWord.append('3')
        elif letter == ' ':
            newWord.append('g')
    Switched: str  = ''.join(newWord)
    return Switched

def V_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'S':
            newWord.append('A')
        elif letter == '|':
            newWord.append('B')
        elif letter == 'i':
            newWord.append('C')
        elif letter == 'j':
            newWord.append('D')
        elif letter == 'a':
            newWord.append('E')
        elif letter == 'A':
            newWord.append('F')
        elif letter == ')':
            newWord.append('G')
        elif letter == '^':
            newWord.append('H')
        elif letter == '1':
            newWord.append('I')
        elif letter == 'k':
            newWord.append('J')
        elif letter == '/':
            newWord.append('K')
        elif letter == 'R':
            newWord.append('L')
        elif letter == 'o':
            newWord.append('M')
        elif letter == 'r':
            newWord.append('N')
        elif letter == '{':
            newWord.append('O')
        elif letter == 'd':
            newWord.append('P')
        elif letter == '0':
            newWord.append('Q')
        elif letter == '%':
            newWord.append('R')
        elif letter == 'q':
            newWord.append('S')
        elif letter == 'n':
            newWord.append('T')
        elif letter == 'm':
            newWord.append('U')
        elif letter == 'T':
            newWord.append('V')
        elif letter == '`':
            newWord.append('W')
        elif letter == 't':
            newWord.append('X')
        elif letter == 'w':
            newWord.append('Y')
        elif letter == ':':
            newWord.append('Z')
        elif letter == 'L':
            newWord.append('a')
        elif letter == 'K':
            newWord.append('b')
        elif letter == '[':
            newWord.append('c')
        elif letter == '~':
            newWord.append('d')
        elif letter == '!':
            newWord.append('e')
        elif letter == '.':
            newWord.append('f')
        elif letter == 'U':
            newWord.append('g')
        elif letter == '7':
            newWord.append('h')
        elif letter == 'e':
            newWord.append('i')
        elif letter == 'Y':
            newWord.append('j')
        elif letter == 'p':
            newWord.append('k')
        elif letter == 'V':
            newWord.append('l')
        elif letter == 'N':
            newWord.append('m')
        elif letter == 'E':
            newWord.append('n')
        elif letter == 'P':
            newWord.append('o')
        elif letter == '-':
            newWord.append('p')
        elif letter == 'H':
            newWord.append('q')
        elif letter == 'z':
            newWord.append('r')
        elif letter == 'O':
            newWord.append('s')
        elif letter == '8':
            newWord.append('t')
        elif letter == '<':
            newWord.append('u')
        elif letter == '$':
            newWord.append('v')
        elif letter == 'F':
            newWord.append('w')
        elif letter == 'Q':
            newWord.append('x')
        elif letter == 'G':
            newWord.append('y')
        elif letter == ',':
            newWord.append('z')
        elif letter == '(':
            newWord.append('1')
        elif letter == 'v':
            newWord.append('2')
        elif letter == ' ':
            newWord.append('3')
        elif letter == 'X':
            newWord.append('4')
        elif letter == 'W':
            newWord.append('5')
        elif letter == 'C':
            newWord.append('6')
        elif letter == ']':
            newWord.append('7')
        elif letter == 'l':
            newWord.append('8')
        elif letter == '}':
            newWord.append('9')
        elif letter == 'u':
            newWord.append('0')
        elif letter == '=':
            newWord.append('!')
        elif letter == '@':
            newWord.append('@')
        elif letter == 'M':
            newWord.append('#')
        elif letter == 'x':
            newWord.append('$')
        elif letter == '9':
            newWord.append('%')
        elif letter == 'h':
            newWord.append('^')
        elif letter == '?':
            newWord.append('&')
        elif letter == 'y':
            newWord.append('*')
        elif letter == 'D':
            newWord.append('(')
        elif letter == '_':
            newWord.append(')')
        elif letter == '6':
            newWord.append('-')
        elif letter == '>':
            newWord.append('_')
        elif letter == '4':
            newWord.append('+')
        elif letter == '*':
            newWord.append('=')
        elif letter == 'Z':
            newWord.append('`')
        elif letter == 'J':
            newWord.append('~')
        elif letter == 'f':
            newWord.append('[')
        elif letter == 's':
            newWord.append(']')
        elif letter == 'c':
            newWord.append('{')
        elif letter == '5':
            newWord.append('}')
        elif letter == '2':
            newWord.append('|')
        elif letter == 'b':
            newWord.append(':')
        elif letter == 'B':
            newWord.append(',')
        elif letter == '+':
            newWord.append('<')
        elif letter == '#':
            newWord.append('.')
        elif letter == '&':
            newWord.append('>')
        elif letter == 'I':
            newWord.append('/')
        elif letter == '3':
            newWord.append('?')
        elif letter == 'g':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def W_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('&')
        elif letter == 'B':
            newWord.append('d')
        elif letter == 'C':
            newWord.append('E')
        elif letter == 'D':
            newWord.append('j')
        elif letter == 'E':
            newWord.append('|')
        elif letter == 'F':
            newWord.append('$')
        elif letter == 'G':
            newWord.append('T')
        elif letter == 'H':
            newWord.append('b')
        elif letter == 'I':
            newWord.append('~')
        elif letter == 'J':
            newWord.append('w')
        elif letter == 'K':
            newWord.append('M')
        elif letter == 'L':
            newWord.append('p')
        elif letter == 'M':
            newWord.append('N')
        elif letter == 'N':
            newWord.append('O')
        elif letter == 'O':
            newWord.append('q')
        elif letter == 'P':
            newWord.append('{')
        elif letter == 'Q':
            newWord.append('P')
        elif letter == 'R':
            newWord.append('.')
        elif letter == 'S':
            newWord.append('D')
        elif letter == 'T':
            newWord.append('@')
        elif letter == 'U':
            newWord.append('G')
        elif letter == 'V':
            newWord.append('<')
        elif letter == 'W':
            newWord.append('l')
        elif letter == 'X':
            newWord.append('%')
        elif letter == 'Y':
            newWord.append('V')
        elif letter == 'Z':
            newWord.append('2')
        elif letter == 'a':
            newWord.append('C')
        elif letter == 'b':
            newWord.append('k')
        elif letter == 'c':
            newWord.append('i')
        elif letter == 'd':
            newWord.append('5')
        elif letter == 'e':
            newWord.append('>')
        elif letter == 'f':
            newWord.append('a')
        elif letter == 'g':
            newWord.append('J')
        elif letter == 'h':
            newWord.append('H')
        elif letter == 'i':
            newWord.append('*')
        elif letter == 'j':
            newWord.append('3')
        elif letter == 'k':
            newWord.append('Q')
        elif letter == 'l':
            newWord.append('u')
        elif letter == 'm':
            newWord.append('A')
        elif letter == 'n':
            newWord.append('g')
        elif letter == 'o':
            newWord.append('W')
        elif letter == 'p':
            newWord.append('0')
        elif letter == 'q':
            newWord.append(')')
        elif letter == 'r':
            newWord.append('8')
        elif letter == 's':
            newWord.append('y')
        elif letter == 't':
            newWord.append('[')
        elif letter == 'u':
            newWord.append('}')
        elif letter == 'v':
            newWord.append('S')
        elif letter == 'w':
            newWord.append('^')
        elif letter == 'x':
            newWord.append('+')
        elif letter == 'y':
            newWord.append('4')
        elif letter == 'z':
            newWord.append('X')
        elif letter == '1':
            newWord.append('L')
        elif letter == '2':
            newWord.append('B')
        elif letter == '3':
            newWord.append(',')
        elif letter == '4':
            newWord.append('(')
        elif letter == '5':
            newWord.append('s')
        elif letter == '6':
            newWord.append('v')
        elif letter == '7':
            newWord.append('_')
        elif letter == '8':
            newWord.append('-')
        elif letter == '9':
            newWord.append('?')
        elif letter == '0':
            newWord.append('n')
        elif letter == '!':
            newWord.append('o')
        elif letter == '@':
            newWord.append('6')
        elif letter == '#':
            newWord.append('f')
        elif letter == '$':
            newWord.append('R')
        elif letter == '%':
            newWord.append(']')
        elif letter == '^':
            newWord.append('7')
        elif letter == '&':
            newWord.append('I')
        elif letter == '*':
            newWord.append('9')
        elif letter == '(':
            newWord.append('!')
        elif letter == ')':
            newWord.append(':')
        elif letter == '-':
            newWord.append('U')
        elif letter == '_':
            newWord.append('r')
        elif letter == '+':
            newWord.append('F')
        elif letter == '=':
            newWord.append('#')
        elif letter == '`':
            newWord.append('`')
        elif letter == '~':
            newWord.append('K')
        elif letter == '[':
            newWord.append('m')
        elif letter == ']':
            newWord.append('1')
        elif letter == '{':
            newWord.append('c')
        elif letter == '}':
            newWord.append('=')
        elif letter == '|':
            newWord.append('x')
        elif letter == ':':
            newWord.append('h')
        elif letter == ',':
            newWord.append('Y')
        elif letter == '<':
            newWord.append('/')
        elif letter == '.':
            newWord.append(' ')
        elif letter == '>':
            newWord.append('e')
        elif letter == '/':
            newWord.append('t')
        elif letter == '?':
            newWord.append('Z')
        elif letter == ' ':
            newWord.append('z')
    Switched: str  = ''.join(newWord)
    return Switched

def W_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '&':
            newWord.append('A')
        elif letter == 'd':
            newWord.append('B')
        elif letter == 'E':
            newWord.append('C')
        elif letter == 'j':
            newWord.append('D')
        elif letter == '|':
            newWord.append('E')
        elif letter == '$':
            newWord.append('F')
        elif letter == 'T':
            newWord.append('G')
        elif letter == 'b':
            newWord.append('H')
        elif letter == '~':
            newWord.append('I')
        elif letter == 'w':
            newWord.append('J')
        elif letter == 'M':
            newWord.append('K')
        elif letter == 'p':
            newWord.append('L')
        elif letter == 'N':
            newWord.append('M')
        elif letter == 'O':
            newWord.append('N')
        elif letter == 'q':
            newWord.append('O')
        elif letter == '{':
            newWord.append('P')
        elif letter == 'P':
            newWord.append('Q')
        elif letter == '.':
            newWord.append('R')
        elif letter == 'D':
            newWord.append('S')
        elif letter == '@':
            newWord.append('T')
        elif letter == 'G':
            newWord.append('U')
        elif letter == '<':
            newWord.append('V')
        elif letter == 'l':
            newWord.append('W')
        elif letter == '%':
            newWord.append('X')
        elif letter == 'V':
            newWord.append('Y')
        elif letter == '2':
            newWord.append('Z')
        elif letter == 'C':
            newWord.append('a')
        elif letter == 'k':
            newWord.append('b')
        elif letter == 'i':
            newWord.append('c')
        elif letter == '5':
            newWord.append('d')
        elif letter == '>':
            newWord.append('e')
        elif letter == 'a':
            newWord.append('f')
        elif letter == 'J':
            newWord.append('g')
        elif letter == 'H':
            newWord.append('h')
        elif letter == '*':
            newWord.append('i')
        elif letter == '3':
            newWord.append('j')
        elif letter == 'Q':
            newWord.append('k')
        elif letter == 'u':
            newWord.append('l')
        elif letter == 'A':
            newWord.append('m')
        elif letter == 'g':
            newWord.append('n')
        elif letter == 'W':
            newWord.append('o')
        elif letter == '0':
            newWord.append('p')
        elif letter == ')':
            newWord.append('q')
        elif letter == '8':
            newWord.append('r')
        elif letter == 'y':
            newWord.append('s')
        elif letter == '[':
            newWord.append('t')
        elif letter == '}':
            newWord.append('u')
        elif letter == 'S':
            newWord.append('v')
        elif letter == '^':
            newWord.append('w')
        elif letter == '+':
            newWord.append('x')
        elif letter == '4':
            newWord.append('y')
        elif letter == 'X':
            newWord.append('z')
        elif letter == 'L':
            newWord.append('1')
        elif letter == 'B':
            newWord.append('2')
        elif letter == ',':
            newWord.append('3')
        elif letter == '(':
            newWord.append('4')
        elif letter == 's':
            newWord.append('5')
        elif letter == 'v':
            newWord.append('6')
        elif letter == '_':
            newWord.append('7')
        elif letter == '-':
            newWord.append('8')
        elif letter == '?':
            newWord.append('9')
        elif letter == 'n':
            newWord.append('0')
        elif letter == 'o':
            newWord.append('!')
        elif letter == '6':
            newWord.append('@')
        elif letter == 'f':
            newWord.append('#')
        elif letter == 'R':
            newWord.append('$')
        elif letter == ']':
            newWord.append('%')
        elif letter == '7':
            newWord.append('^')
        elif letter == 'I':
            newWord.append('&')
        elif letter == '9':
            newWord.append('*')
        elif letter == '!':
            newWord.append('(')
        elif letter == ':':
            newWord.append(')')
        elif letter == 'U':
            newWord.append('-')
        elif letter == 'r':
            newWord.append('_')
        elif letter == 'F':
            newWord.append('+')
        elif letter == '#':
            newWord.append('=')
        elif letter == '`':
            newWord.append('`')
        elif letter == 'K':
            newWord.append('~')
        elif letter == 'm':
            newWord.append('[')
        elif letter == '1':
            newWord.append(']')
        elif letter == 'c':
            newWord.append('{')
        elif letter == '=':
            newWord.append('}')
        elif letter == 'x':
            newWord.append('|')
        elif letter == 'h':
            newWord.append(':')
        elif letter == 'Y':
            newWord.append(',')
        elif letter == '/':
            newWord.append('<')
        elif letter == ' ':
            newWord.append('.')
        elif letter == 'e':
            newWord.append('>')
        elif letter == 't':
            newWord.append('/')
        elif letter == 'Z':
            newWord.append('?')
        elif letter == 'z':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def X_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('{')
        elif letter == 'B':
            newWord.append('6')
        elif letter == 'C':
            newWord.append('W')
        elif letter == 'D':
            newWord.append('a')
        elif letter == 'E':
            newWord.append('B')
        elif letter == 'F':
            newWord.append('<')
        elif letter == 'G':
            newWord.append('x')
        elif letter == 'H':
            newWord.append('Q')
        elif letter == 'I':
            newWord.append(')')
        elif letter == 'J':
            newWord.append('k')
        elif letter == 'K':
            newWord.append('A')
        elif letter == 'L':
            newWord.append('[')
        elif letter == 'M':
            newWord.append('N')
        elif letter == 'N':
            newWord.append('X')
        elif letter == 'O':
            newWord.append('9')
        elif letter == 'P':
            newWord.append('R')
        elif letter == 'Q':
            newWord.append('j')
        elif letter == 'R':
            newWord.append('4')
        elif letter == 'S':
            newWord.append('#')
        elif letter == 'T':
            newWord.append('D')
        elif letter == 'U':
            newWord.append('E')
        elif letter == 'V':
            newWord.append('H')
        elif letter == 'W':
            newWord.append('I')
        elif letter == 'X':
            newWord.append('F')
        elif letter == 'Y':
            newWord.append('v')
        elif letter == 'Z':
            newWord.append('z')
        elif letter == 'a':
            newWord.append('w')
        elif letter == 'b':
            newWord.append('2')
        elif letter == 'c':
            newWord.append('f')
        elif letter == 'd':
            newWord.append('!')
        elif letter == 'e':
            newWord.append('7')
        elif letter == 'f':
            newWord.append('/')
        elif letter == 'g':
            newWord.append(',')
        elif letter == 'h':
            newWord.append('V')
        elif letter == 'i':
            newWord.append('d')
        elif letter == 'j':
            newWord.append('8')
        elif letter == 'k':
            newWord.append('%')
        elif letter == 'l':
            newWord.append('S')
        elif letter == 'm':
            newWord.append('p')
        elif letter == 'n':
            newWord.append('y')
        elif letter == 'o':
            newWord.append('.')
        elif letter == 'p':
            newWord.append('T')
        elif letter == 'q':
            newWord.append('m')
        elif letter == 'r':
            newWord.append('=')
        elif letter == 's':
            newWord.append('o')
        elif letter == 't':
            newWord.append('$')
        elif letter == 'u':
            newWord.append('*')
        elif letter == 'v':
            newWord.append('L')
        elif letter == 'w':
            newWord.append('5')
        elif letter == 'x':
            newWord.append('Z')
        elif letter == 'y':
            newWord.append('@')
        elif letter == 'z':
            newWord.append('c')
        elif letter == '1':
            newWord.append('P')
        elif letter == '2':
            newWord.append('C')
        elif letter == '3':
            newWord.append('G')
        elif letter == '4':
            newWord.append('r')
        elif letter == '5':
            newWord.append('0')
        elif letter == '6':
            newWord.append('+')
        elif letter == '7':
            newWord.append(':')
        elif letter == '8':
            newWord.append('n')
        elif letter == '9':
            newWord.append('`')
        elif letter == '0':
            newWord.append('h')
        elif letter == '!':
            newWord.append(' ')
        elif letter == '@':
            newWord.append('b')
        elif letter == '#':
            newWord.append('u')
        elif letter == '$':
            newWord.append('-')
        elif letter == '%':
            newWord.append('e')
        elif letter == '^':
            newWord.append('1')
        elif letter == '&':
            newWord.append('q')
        elif letter == '*':
            newWord.append('_')
        elif letter == '(':
            newWord.append('3')
        elif letter == ')':
            newWord.append('i')
        elif letter == '-':
            newWord.append('t')
        elif letter == '_':
            newWord.append('(')
        elif letter == '+':
            newWord.append(']')
        elif letter == '=':
            newWord.append('U')
        elif letter == '`':
            newWord.append('Y')
        elif letter == '~':
            newWord.append('~')
        elif letter == '[':
            newWord.append('g')
        elif letter == ']':
            newWord.append('&')
        elif letter == '{':
            newWord.append('M')
        elif letter == '}':
            newWord.append('|')
        elif letter == '|':
            newWord.append('s')
        elif letter == ':':
            newWord.append('O')
        elif letter == ',':
            newWord.append('^')
        elif letter == '<':
            newWord.append('>')
        elif letter == '.':
            newWord.append('}')
        elif letter == '>':
            newWord.append('l')
        elif letter == '/':
            newWord.append('?')
        elif letter == '?':
            newWord.append('K')
        elif letter == ' ':
            newWord.append('J')
    Switched: str  = ''.join(newWord)
    return Switched

def X_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == '{':
            newWord.append('A')
        elif letter == '6':
            newWord.append('B')
        elif letter == 'W':
            newWord.append('C')
        elif letter == 'a':
            newWord.append('D')
        elif letter == 'B':
            newWord.append('E')
        elif letter == '<':
            newWord.append('F')
        elif letter == 'x':
            newWord.append('G')
        elif letter == 'Q':
            newWord.append('H')
        elif letter == ')':
            newWord.append('I')
        elif letter == 'k':
            newWord.append('J')
        elif letter == 'A':
            newWord.append('K')
        elif letter == '[':
            newWord.append('L')
        elif letter == 'N':
            newWord.append('M')
        elif letter == 'X':
            newWord.append('N')
        elif letter == '9':
            newWord.append('O')
        elif letter == 'R':
            newWord.append('P')
        elif letter == 'j':
            newWord.append('Q')
        elif letter == '4':
            newWord.append('R')
        elif letter == '#':
            newWord.append('S')
        elif letter == 'D':
            newWord.append('T')
        elif letter == 'E':
            newWord.append('U')
        elif letter == 'H':
            newWord.append('V')
        elif letter == 'I':
            newWord.append('W')
        elif letter == 'F':
            newWord.append('X')
        elif letter == 'v':
            newWord.append('Y')
        elif letter == 'z':
            newWord.append('Z')
        elif letter == 'w':
            newWord.append('a')
        elif letter == '2':
            newWord.append('b')
        elif letter == 'f':
            newWord.append('c')
        elif letter == '!':
            newWord.append('d')
        elif letter == '7':
            newWord.append('e')
        elif letter == '/':
            newWord.append('f')
        elif letter == ',':
            newWord.append('g')
        elif letter == 'V':
            newWord.append('h')
        elif letter == 'd':
            newWord.append('i')
        elif letter == '8':
            newWord.append('j')
        elif letter == '%':
            newWord.append('k')
        elif letter == 'S':
            newWord.append('l')
        elif letter == 'p':
            newWord.append('m')
        elif letter == 'y':
            newWord.append('n')
        elif letter == '.':
            newWord.append('o')
        elif letter == 'T':
            newWord.append('p')
        elif letter == 'm':
            newWord.append('q')
        elif letter == '=':
            newWord.append('r')
        elif letter == 'o':
            newWord.append('s')
        elif letter == '$':
            newWord.append('t')
        elif letter == '*':
            newWord.append('u')
        elif letter == 'L':
            newWord.append('v')
        elif letter == '5':
            newWord.append('w')
        elif letter == 'Z':
            newWord.append('x')
        elif letter == '@':
            newWord.append('y')
        elif letter == 'c':
            newWord.append('z')
        elif letter == 'P':
            newWord.append('1')
        elif letter == 'C':
            newWord.append('2')
        elif letter == 'G':
            newWord.append('3')
        elif letter == 'r':
            newWord.append('4')
        elif letter == '0':
            newWord.append('5')
        elif letter == '+':
            newWord.append('6')
        elif letter == ':':
            newWord.append('7')
        elif letter == 'n':
            newWord.append('8')
        elif letter == '`':
            newWord.append('9')
        elif letter == 'h':
            newWord.append('0')
        elif letter == ' ':
            newWord.append('!')
        elif letter == 'b':
            newWord.append('@')
        elif letter == 'u':
            newWord.append('#')
        elif letter == '-':
            newWord.append('$')
        elif letter == 'e':
            newWord.append('%')
        elif letter == '1':
            newWord.append('^')
        elif letter == 'q':
            newWord.append('&')
        elif letter == '_':
            newWord.append('*')
        elif letter == '3':
            newWord.append('(')
        elif letter == 'i':
            newWord.append(')')
        elif letter == 't':
            newWord.append('-')
        elif letter == '(':
            newWord.append('_')
        elif letter == ']':
            newWord.append('+')
        elif letter == 'U':
            newWord.append('=')
        elif letter == 'Y':
            newWord.append('`')
        elif letter == '~':
            newWord.append('~')
        elif letter == 'g':
            newWord.append('[')
        elif letter == '&':
            newWord.append(']')
        elif letter == 'M':
            newWord.append('{')
        elif letter == '|':
            newWord.append('}')
        elif letter == 's':
            newWord.append('|')
        elif letter == 'O':
            newWord.append(':')
        elif letter == '^':
            newWord.append(',')
        elif letter == '>':
            newWord.append('<')
        elif letter == '}':
            newWord.append('.')
        elif letter == 'l':
            newWord.append('>')
        elif letter == '?':
            newWord.append('/')
        elif letter == 'K':
            newWord.append('?')
        elif letter == 'J':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def Y_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('N')
        elif letter == 'B':
            newWord.append('8')
        elif letter == 'C':
            newWord.append('m')
        elif letter == 'D':
            newWord.append('!')
        elif letter == 'E':
            newWord.append('I')
        elif letter == 'F':
            newWord.append('F')
        elif letter == 'G':
            newWord.append('f')
        elif letter == 'H':
            newWord.append('2')
        elif letter == 'I':
            newWord.append('C')
        elif letter == 'J':
            newWord.append('9')
        elif letter == 'K':
            newWord.append('P')
        elif letter == 'L':
            newWord.append('h')
        elif letter == 'M':
            newWord.append(':')
        elif letter == 'N':
            newWord.append('d')
        elif letter == 'O':
            newWord.append('0')
        elif letter == 'P':
            newWord.append('?')
        elif letter == 'Q':
            newWord.append('u')
        elif letter == 'R':
            newWord.append('K')
        elif letter == 'S':
            newWord.append('_')
        elif letter == 'T':
            newWord.append('v')
        elif letter == 'U':
            newWord.append('*')
        elif letter == 'V':
            newWord.append('[')
        elif letter == 'W':
            newWord.append('l')
        elif letter == 'X':
            newWord.append('G')
        elif letter == 'Y':
            newWord.append('j')
        elif letter == 'Z':
            newWord.append('6')
        elif letter == 'a':
            newWord.append('.')
        elif letter == 'b':
            newWord.append(')')
        elif letter == 'c':
            newWord.append('M')
        elif letter == 'd':
            newWord.append('i')
        elif letter == 'e':
            newWord.append('~')
        elif letter == 'f':
            newWord.append('{')
        elif letter == 'g':
            newWord.append('p')
        elif letter == 'h':
            newWord.append('$')
        elif letter == 'i':
            newWord.append('1')
        elif letter == 'j':
            newWord.append(']')
        elif letter == 'k':
            newWord.append('B')
        elif letter == 'l':
            newWord.append('r')
        elif letter == 'm':
            newWord.append('Q')
        elif letter == 'n':
            newWord.append('U')
        elif letter == 'o':
            newWord.append('z')
        elif letter == 'p':
            newWord.append('<')
        elif letter == 'q':
            newWord.append('A')
        elif letter == 'r':
            newWord.append('O')
        elif letter == 's':
            newWord.append('/')
        elif letter == 't':
            newWord.append('@')
        elif letter == 'u':
            newWord.append('J')
        elif letter == 'v':
            newWord.append('X')
        elif letter == 'w':
            newWord.append('s')
        elif letter == 'x':
            newWord.append(',')
        elif letter == 'y':
            newWord.append('Y')
        elif letter == 'z':
            newWord.append('n')
        elif letter == '1':
            newWord.append(' ')
        elif letter == '2':
            newWord.append('e')
        elif letter == '3':
            newWord.append('E')
        elif letter == '4':
            newWord.append('Z')
        elif letter == '5':
            newWord.append('q')
        elif letter == '6':
            newWord.append('%')
        elif letter == '7':
            newWord.append('+')
        elif letter == '8':
            newWord.append('^')
        elif letter == '9':
            newWord.append('c')
        elif letter == '0':
            newWord.append('4')
        elif letter == '!':
            newWord.append('R')
        elif letter == '@':
            newWord.append('b')
        elif letter == '#':
            newWord.append('T')
        elif letter == '$':
            newWord.append('-')
        elif letter == '%':
            newWord.append('t')
        elif letter == '^':
            newWord.append('>')
        elif letter == '&':
            newWord.append('7')
        elif letter == '*':
            newWord.append('#')
        elif letter == '(':
            newWord.append('W')
        elif letter == ')':
            newWord.append('S')
        elif letter == '-':
            newWord.append('y')
        elif letter == '_':
            newWord.append('L')
        elif letter == '+':
            newWord.append('&')
        elif letter == '=':
            newWord.append('=')
        elif letter == '`':
            newWord.append('3')
        elif letter == '~':
            newWord.append('g')
        elif letter == '[':
            newWord.append('H')
        elif letter == ']':
            newWord.append('o')
        elif letter == '{':
            newWord.append('5')
        elif letter == '}':
            newWord.append('|')
        elif letter == '|':
            newWord.append('`')
        elif letter == ':':
            newWord.append('(')
        elif letter == ',':
            newWord.append('V')
        elif letter == '<':
            newWord.append('}')
        elif letter == '.':
            newWord.append('k')
        elif letter == '>':
            newWord.append('w')
        elif letter == '/':
            newWord.append('a')
        elif letter == '?':
            newWord.append('D')
        elif letter == ' ':
            newWord.append('x')
    Switched: str  = ''.join(newWord)
    return Switched

def Y_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'N':
            newWord.append('A')
        elif letter == '8':
            newWord.append('B')
        elif letter == 'm':
            newWord.append('C')
        elif letter == '!':
            newWord.append('D')
        elif letter == 'I':
            newWord.append('E')
        elif letter == 'F':
            newWord.append('F')
        elif letter == 'f':
            newWord.append('G')
        elif letter == '2':
            newWord.append('H')
        elif letter == 'C':
            newWord.append('I')
        elif letter == '9':
            newWord.append('J')
        elif letter == 'P':
            newWord.append('K')
        elif letter == 'h':
            newWord.append('L')
        elif letter == ':':
            newWord.append('M')
        elif letter == 'd':
            newWord.append('N')
        elif letter == '0':
            newWord.append('O')
        elif letter == '?':
            newWord.append('P')
        elif letter == 'u':
            newWord.append('Q')
        elif letter == 'K':
            newWord.append('R')
        elif letter == '_':
            newWord.append('S')
        elif letter == 'v':
            newWord.append('T')
        elif letter == '*':
            newWord.append('U')
        elif letter == '[':
            newWord.append('V')
        elif letter == 'l':
            newWord.append('W')
        elif letter == 'G':
            newWord.append('X')
        elif letter == 'j':
            newWord.append('Y')
        elif letter == '6':
            newWord.append('Z')
        elif letter == '.':
            newWord.append('a')
        elif letter == ')':
            newWord.append('b')
        elif letter == 'M':
            newWord.append('c')
        elif letter == 'i':
            newWord.append('d')
        elif letter == '~':
            newWord.append('e')
        elif letter == '{':
            newWord.append('f')
        elif letter == 'p':
            newWord.append('g')
        elif letter == '$':
            newWord.append('h')
        elif letter == '1':
            newWord.append('i')
        elif letter == ']':
            newWord.append('j')
        elif letter == 'B':
            newWord.append('k')
        elif letter == 'r':
            newWord.append('l')
        elif letter == 'Q':
            newWord.append('m')
        elif letter == 'U':
            newWord.append('n')
        elif letter == 'z':
            newWord.append('o')
        elif letter == '<':
            newWord.append('p')
        elif letter == 'A':
            newWord.append('q')
        elif letter == 'O':
            newWord.append('r')
        elif letter == '/':
            newWord.append('s')
        elif letter == '@':
            newWord.append('t')
        elif letter == 'J':
            newWord.append('u')
        elif letter == 'X':
            newWord.append('v')
        elif letter == 's':
            newWord.append('w')
        elif letter == ',':
            newWord.append('x')
        elif letter == 'Y':
            newWord.append('y')
        elif letter == 'n':
            newWord.append('z')
        elif letter == ' ':
            newWord.append('1')
        elif letter == 'e':
            newWord.append('2')
        elif letter == 'E':
            newWord.append('3')
        elif letter == 'Z':
            newWord.append('4')
        elif letter == 'q':
            newWord.append('5')
        elif letter == '%':
            newWord.append('6')
        elif letter == '+':
            newWord.append('7')
        elif letter == '^':
            newWord.append('8')
        elif letter == 'c':
            newWord.append('9')
        elif letter == '4':
            newWord.append('0')
        elif letter == 'R':
            newWord.append('!')
        elif letter == 'b':
            newWord.append('@')
        elif letter == 'T':
            newWord.append('#')
        elif letter == '-':
            newWord.append('$')
        elif letter == 't':
            newWord.append('%')
        elif letter == '>':
            newWord.append('^')
        elif letter == '7':
            newWord.append('&')
        elif letter == '#':
            newWord.append('*')
        elif letter == 'W':
            newWord.append('(')
        elif letter == 'S':
            newWord.append(')')
        elif letter == 'y':
            newWord.append('-')
        elif letter == 'L':
            newWord.append('_')
        elif letter == '&':
            newWord.append('+')
        elif letter == '=':
            newWord.append('=')
        elif letter == '3':
            newWord.append('`')
        elif letter == 'g':
            newWord.append('~')
        elif letter == 'H':
            newWord.append('[')
        elif letter == 'o':
            newWord.append(']')
        elif letter == '5':
            newWord.append('{')
        elif letter == '|':
            newWord.append('}')
        elif letter == '`':
            newWord.append('|')
        elif letter == '(':
            newWord.append(':')
        elif letter == 'V':
            newWord.append(',')
        elif letter == '}':
            newWord.append('<')
        elif letter == 'k':
            newWord.append('.')
        elif letter == 'w':
            newWord.append('>')
        elif letter == 'a':
            newWord.append('/')
        elif letter == 'D':
            newWord.append('?')
        elif letter == 'x':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def Z_Encode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'A':
            newWord.append('C')
        elif letter == 'B':
            newWord.append('t')
        elif letter == 'C':
            newWord.append('n')
        elif letter == 'D':
            newWord.append('q')
        elif letter == 'E':
            newWord.append('.')
        elif letter == 'F':
            newWord.append('w')
        elif letter == 'G':
            newWord.append('d')
        elif letter == 'H':
            newWord.append('$')
        elif letter == 'I':
            newWord.append('r')
        elif letter == 'J':
            newWord.append('8')
        elif letter == 'K':
            newWord.append('1')
        elif letter == 'L':
            newWord.append('e')
        elif letter == 'M':
            newWord.append('%')
        elif letter == 'N':
            newWord.append('N')
        elif letter == 'O':
            newWord.append('@')
        elif letter == 'P':
            newWord.append('V')
        elif letter == 'Q':
            newWord.append('4')
        elif letter == 'R':
            newWord.append('J')
        elif letter == 'S':
            newWord.append('y')
        elif letter == 'T':
            newWord.append('j')
        elif letter == 'U':
            newWord.append('7')
        elif letter == 'V':
            newWord.append('K')
        elif letter == 'W':
            newWord.append('u')
        elif letter == 'X':
            newWord.append('=')
        elif letter == 'Y':
            newWord.append('R')
        elif letter == 'Z':
            newWord.append('c')
        elif letter == 'a':
            newWord.append('Q')
        elif letter == 'b':
            newWord.append('+')
        elif letter == 'c':
            newWord.append('M')
        elif letter == 'd':
            newWord.append('|')
        elif letter == 'e':
            newWord.append('0')
        elif letter == 'f':
            newWord.append('2')
        elif letter == 'g':
            newWord.append('z')
        elif letter == 'h':
            newWord.append('F')
        elif letter == 'i':
            newWord.append('i')
        elif letter == 'j':
            newWord.append('O')
        elif letter == 'k':
            newWord.append('`')
        elif letter == 'l':
            newWord.append('o')
        elif letter == 'm':
            newWord.append('x')
        elif letter == 'n':
            newWord.append('f')
        elif letter == 'o':
            newWord.append('U')
        elif letter == 'p':
            newWord.append('B')
        elif letter == 'q':
            newWord.append('Y')
        elif letter == 'r':
            newWord.append('H')
        elif letter == 's':
            newWord.append('P')
        elif letter == 't':
            newWord.append(':')
        elif letter == 'u':
            newWord.append('X')
        elif letter == 'v':
            newWord.append(']')
        elif letter == 'w':
            newWord.append('9')
        elif letter == 'x':
            newWord.append('~')
        elif letter == 'y':
            newWord.append('E')
        elif letter == 'z':
            newWord.append(' ')
        elif letter == '1':
            newWord.append('v')
        elif letter == '2':
            newWord.append('l')
        elif letter == '3':
            newWord.append('g')
        elif letter == '4':
            newWord.append('p')
        elif letter == '5':
            newWord.append('(')
        elif letter == '6':
            newWord.append('>')
        elif letter == '7':
            newWord.append(',')
        elif letter == '8':
            newWord.append('/')
        elif letter == '9':
            newWord.append('!')
        elif letter == '0':
            newWord.append('<')
        elif letter == '!':
            newWord.append('_')
        elif letter == '@':
            newWord.append('I')
        elif letter == '#':
            newWord.append('k')
        elif letter == '$':
            newWord.append('Z')
        elif letter == '%':
            newWord.append('-')
        elif letter == '^':
            newWord.append('}')
        elif letter == '&':
            newWord.append('h')
        elif letter == '*':
            newWord.append('?')
        elif letter == '(':
            newWord.append('5')
        elif letter == ')':
            newWord.append('T')
        elif letter == '-':
            newWord.append('S')
        elif letter == '_':
            newWord.append('{')
        elif letter == '+':
            newWord.append(')')
        elif letter == '=':
            newWord.append('a')
        elif letter == '`':
            newWord.append('s')
        elif letter == '~':
            newWord.append('A')
        elif letter == '[':
            newWord.append('3')
        elif letter == ']':
            newWord.append('D')
        elif letter == '{':
            newWord.append('L')
        elif letter == '}':
            newWord.append('W')
        elif letter == '|':
            newWord.append('b')
        elif letter == ':':
            newWord.append('^')
        elif letter == ',':
            newWord.append('[')
        elif letter == '<':
            newWord.append('m')
        elif letter == '.':
            newWord.append('*')
        elif letter == '>':
            newWord.append('6')
        elif letter == '/':
            newWord.append('&')
        elif letter == '?':
            newWord.append('G')
        elif letter == ' ':
            newWord.append('#')
    Switched: str  = ''.join(newWord)
    return Switched

def Z_Decode(Text: str):
    newWord: list[str] = []
    for letter in Text:
        if letter == 'C':
            newWord.append('A')
        elif letter == 't':
            newWord.append('B')
        elif letter == 'n':
            newWord.append('C')
        elif letter == 'q':
            newWord.append('D')
        elif letter == '.':
            newWord.append('E')
        elif letter == 'w':
            newWord.append('F')
        elif letter == 'd':
            newWord.append('G')
        elif letter == '$':
            newWord.append('H')
        elif letter == 'r':
            newWord.append('I')
        elif letter == '8':
            newWord.append('J')
        elif letter == '1':
            newWord.append('K')
        elif letter == 'e':
            newWord.append('L')
        elif letter == '%':
            newWord.append('M')
        elif letter == 'N':
            newWord.append('N')
        elif letter == '@':
            newWord.append('O')
        elif letter == 'V':
            newWord.append('P')
        elif letter == '4':
            newWord.append('Q')
        elif letter == 'J':
            newWord.append('R')
        elif letter == 'y':
            newWord.append('S')
        elif letter == 'j':
            newWord.append('T')
        elif letter == '7':
            newWord.append('U')
        elif letter == 'K':
            newWord.append('V')
        elif letter == 'u':
            newWord.append('W')
        elif letter == '=':
            newWord.append('X')
        elif letter == 'R':
            newWord.append('Y')
        elif letter == 'c':
            newWord.append('Z')
        elif letter == 'Q':
            newWord.append('a')
        elif letter == '+':
            newWord.append('b')
        elif letter == 'M':
            newWord.append('c')
        elif letter == '|':
            newWord.append('d')
        elif letter == '0':
            newWord.append('e')
        elif letter == '2':
            newWord.append('f')
        elif letter == 'z':
            newWord.append('g')
        elif letter == 'F':
            newWord.append('h')
        elif letter == 'i':
            newWord.append('i')
        elif letter == 'O':
            newWord.append('j')
        elif letter == '`':
            newWord.append('k')
        elif letter == 'o':
            newWord.append('l')
        elif letter == 'x':
            newWord.append('m')
        elif letter == 'f':
            newWord.append('n')
        elif letter == 'U':
            newWord.append('o')
        elif letter == 'B':
            newWord.append('p')
        elif letter == 'Y':
            newWord.append('q')
        elif letter == 'H':
            newWord.append('r')
        elif letter == 'P':
            newWord.append('s')
        elif letter == ':':
            newWord.append('t')
        elif letter == 'X':
            newWord.append('u')
        elif letter == ']':
            newWord.append('v')
        elif letter == '9':
            newWord.append('w')
        elif letter == '~':
            newWord.append('x')
        elif letter == 'E':
            newWord.append('y')
        elif letter == ' ':
            newWord.append('z')
        elif letter == 'v':
            newWord.append('1')
        elif letter == 'l':
            newWord.append('2')
        elif letter == 'g':
            newWord.append('3')
        elif letter == 'p':
            newWord.append('4')
        elif letter == '(':
            newWord.append('5')
        elif letter == '>':
            newWord.append('6')
        elif letter == ',':
            newWord.append('7')
        elif letter == '/':
            newWord.append('8')
        elif letter == '!':
            newWord.append('9')
        elif letter == '<':
            newWord.append('0')
        elif letter == '_':
            newWord.append('!')
        elif letter == 'I':
            newWord.append('@')
        elif letter == 'k':
            newWord.append('#')
        elif letter == 'Z':
            newWord.append('$')
        elif letter == '-':
            newWord.append('%')
        elif letter == '}':
            newWord.append('^')
        elif letter == 'h':
            newWord.append('&')
        elif letter == '?':
            newWord.append('*')
        elif letter == '5':
            newWord.append('(')
        elif letter == 'T':
            newWord.append(')')
        elif letter == 'S':
            newWord.append('-')
        elif letter == '{':
            newWord.append('_')
        elif letter == ')':
            newWord.append('+')
        elif letter == 'a':
            newWord.append('=')
        elif letter == 's':
            newWord.append('`')
        elif letter == 'A':
            newWord.append('~')
        elif letter == '3':
            newWord.append('[')
        elif letter == 'D':
            newWord.append(']')
        elif letter == 'L':
            newWord.append('{')
        elif letter == 'W':
            newWord.append('}')
        elif letter == 'b':
            newWord.append('|')
        elif letter == '^':
            newWord.append(':')
        elif letter == '[':
            newWord.append(',')
        elif letter == 'm':
            newWord.append('<')
        elif letter == '*':
            newWord.append('.')
        elif letter == '6':
            newWord.append('>')
        elif letter == '&':
            newWord.append('/')
        elif letter == 'G':
            newWord.append('?')
        elif letter == '#':
            newWord.append(' ')
    Switched: str  = ''.join(newWord)
    return Switched

def Encode(Text: str):
    if Text[0] == 'A' or Text[0] == 'a':
        HalfText = A_Decode(Text)
    elif Text[0] == 'B' or Text[0] == 'b':
        HalfText = B_Encode(Text)
    elif Text[0] == 'C' or Text[0] == 'c':
        HalfText = C_Encode(Text)
    elif Text[0] == 'D' or Text[0] == 'd':
        HalfText = D_Encode(Text)
    elif Text[0] == 'E' or Text[0] == 'e':
        HalfText = E_Encode(Text)
    elif Text[0] == 'F' or Text[0] == 'f':
        HalfText = F_Encode(Text)
    elif Text[0] == 'G' or Text[0] == 'g':
        HalfText = G_Encode(Text)
    elif Text[0] == 'H' or Text[0] == 'h':
        HalfText = H_Encode(Text)
    elif Text[0] == 'I' or Text[0] == 'i':
        HalfText = I_Encode(Text)
    elif Text[0] == 'J' or Text[0] == 'j':
        HalfText = J_Encode(Text)
    elif Text[0] == 'K' or Text[0] == 'k':
        HalfText = K_Encode(Text)
    elif Text[0] == 'L' or Text[0] == 'l':
        HalfText = L_Encode(Text)
    elif Text[0] == 'M' or Text[0] == 'm':
        HalfText = M_Encode(Text)
    elif Text[0] == 'N' or Text[0] == 'n':
        HalfText = N_Encode(Text)
    elif Text[0] == 'O' or Text[0] == 'o':
        HalfText = O_Encode(Text)
    elif Text[0] == 'P' or Text[0] == 'p':
        HalfText = P_Encode(Text)
    elif Text[0] == 'Q' or Text[0] == 'q':
        HalfText = Q_Encode(Text)
    elif Text[0] == 'R' or Text[0] == 'r':
        HalfText = R_Encode(Text)
    elif Text[0] == 'S' or Text[0] == 's':
        HalfText = S_Encode(Text)
    elif Text[0] == 'T' or Text[0] == 't':
        HalfText = T_Encode(Text)
    elif Text[0] == 'U' or Text[0] == 'u':
        HalfText = U_Encode(Text)
    elif Text[0] == 'V' or Text[0] == 'v':
        HalfText = V_Encode(Text)
    elif Text[0] == 'W' or Text[0] == 'w':
        HalfText = W_Encode(Text)
    elif Text[0] == 'X' or Text[0] == 'x':
        HalfText = X_Encode(Text)
    elif Text[0] == 'Y' or Text[0] == 'y':
        HalfText = Y_Encode(Text)
    else:
        HalfText = Z_Encode(Text)
    EncodedList: list = []
    for x in HalfText:
        if x != HalfText[0]:
            EncodedList.append(x)
        else:
            EncodedList.append(Text[0])
    EncodedText: str  = ''.join(EncodedList)
    return EncodedText

def Decode(Text: str):
    if Text[0] == 'A' or Text[0] == 'a':
        HalfText = A_Decode(Text)
    elif Text[0] == 'B' or Text[0] == 'b':
        HalfText = B_Encode(Text)
    elif Text[0] == 'C' or Text[0] == 'c':
        HalfText = C_Encode(Text)
    elif Text[0] == 'D' or Text[0] == 'd':
        HalfText = D_Encode(Text)
    elif Text[0] == 'E' or Text[0] == 'e':
        HalfText = E_Encode(Text)
    elif Text[0] == 'F' or Text[0] == 'f':
        HalfText = F_Encode(Text)
    elif Text[0] == 'G' or Text[0] == 'g':
        HalfText = G_Encode(Text)
    elif Text[0] == 'H' or Text[0] == 'h':
        HalfText = H_Encode(Text)
    elif Text[0] == 'I' or Text[0] == 'i':
        HalfText = I_Encode(Text)
    elif Text[0] == 'J' or Text[0] == 'j':
        HalfText = J_Encode(Text)
    elif Text[0] == 'K' or Text[0] == 'k':
        HalfText = K_Encode(Text)
    elif Text[0] == 'L' or Text[0] == 'l':
        HalfText = L_Encode(Text)
    elif Text[0] == 'M' or Text[0] == 'm':
        HalfText = M_Encode(Text)
    elif Text[0] == 'N' or Text[0] == 'n':
        HalfText = N_Encode(Text)
    elif Text[0] == 'O' or Text[0] == 'o':
        HalfText = O_Encode(Text)
    elif Text[0] == 'P' or Text[0] == 'p':
        HalfText = P_Encode(Text)
    elif Text[0] == 'Q' or Text[0] == 'q':
        HalfText = Q_Encode(Text)
    elif Text[0] == 'R' or Text[0] == 'r':
        HalfText = R_Encode(Text)
    elif Text[0] == 'S' or Text[0] == 's':
        HalfText = S_Encode(Text)
    elif Text[0] == 'T' or Text[0] == 't':
        HalfText = T_Encode(Text)
    elif Text[0] == 'U' or Text[0] == 'u':
        HalfText = U_Encode(Text)
    elif Text[0] == 'V' or Text[0] == 'v':
        HalfText = V_Encode(Text)
    elif Text[0] == 'W' or Text[0] == 'w':
        HalfText = W_Encode(Text)
    elif Text[0] == 'X' or Text[0] == 'x':
        HalfText = X_Encode(Text)
    elif Text[0] == 'Y' or Text[0] == 'y':
        HalfText = Y_Encode(Text)
    else:
        HalfText = Z_Encode(Text)
    DecodedList: list = []
    for x in HalfText:
        if x != HalfText[0]:
            DecodedList.append(x)
        else:
            DecodedList.append(Text[0])
    DecodedText: str  = ''.join(DecodedList)
    return DecodedText

if __name__ == "__main__":
    UserInput: str = input("> ")
    EncodedInput = Encode(UserInput)
    print(f"{EncodedInput}\n")
    DecodedInput = Decode(EncodedInput)
    print(f"{DecodedInput}\n")