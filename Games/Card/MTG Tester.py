import os

path = r'C:\Users\210108\Downloads\Archelos, Lagoon Mystic MTG Decks'

name: str = input()
num = 0
total = 0
folder = []
for file in os.listdir(path):
    if file.endswith('.txt'):
        folder.append(file)
for x in folder:
    total += 1
    file1 = open(f"C:\\Users\\210108\\Downloads\\Archelos, Lagoon Mystic MTG Decks\\{x}")
    data = file1.read()
    fileCards = data.split("\n") 
    for y in fileCards:
        if name in y:
            print(f"'{y}' from '{x}")
            num += 1
    file1.close()
print(f"{name} appeared {num} times ({num/total*100}% of {total})")