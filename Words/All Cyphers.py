import random, os, pyautogui, time

AlphLetter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if True:
    for x in AlphLetter:
        input()
        os.system("cls")
        Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","`","~","[","]","{","}","|",":",",","<",".",">","/","?"," "]
        ChangeAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","`","~","[","]","{","}","|",":",",","<",".",">","/","?"," "]
        newAlphabet = []

        currentLetter: str = x

        print(f"\ndef {currentLetter}_Encode(Text: str):")
        print("    newWord: list[str] = []")
        print("    for letter in Text:")
        for x in Alphabet:
            change = random.choice(ChangeAlphabet)
            if x == "A":
                print(f"        if letter == '{x}':")
            else:
                print(f"        elif letter == '{x}':")
            print(f"            newWord.append('{change}')")
            ChangeAlphabet.remove(change)
            newAlphabet.append(change)
        print("    Switched: str  = ''.join(newWord)")
        print("    return Switched\n")
        print(f"def {currentLetter}_Decode(Text: str):")
        print("    newWord: list[str] = []")
        print("    for letter in Text:")
        for y, x in enumerate(newAlphabet):
            if x == newAlphabet[0]:
                print(f"        if letter == '{x}':")
            else:
                print(f"        elif letter == '{x}':")
            print(f"            newWord.append('{Alphabet[y]}')")
        print("    Switched: str  = ''.join(newWord)")
        print("    return Switched")