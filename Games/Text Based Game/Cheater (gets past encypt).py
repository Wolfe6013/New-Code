name = input("Name? ")
floor = int(input("Floor? "))
x = int(input("x? "))
y = int(input("y? "))
HP = int(input("HP? "))
MaxHP = int(input("Max HP? "))
Strength = int(input("Strength? "))
Mana = int(input("Mana? "))
Wit = int(input("Wit? "))
Dexterity = int(input("Dexterity? "))

if (floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity) % 2 == 0:
    even = True
else:
    even = False
key = (floor+x+y+HP+MaxHP+Strength+Mana+Wit+Dexterity) % 8

statsList = [
        name,
        str(x),
        str(y),
        str(floor),
        str(HP),
        str(MaxHP),
        str(key),
        str(even),
        str(key)
    ]

for item in statsList:
    print(item)