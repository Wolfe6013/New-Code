numbers = [1,3,5,7,9,11,13,15]

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x+y+z == 30:
                print(f"{x}+{y}+{z} = 30")