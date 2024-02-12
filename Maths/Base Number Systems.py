import os
base = int(input("Base "))
symbols = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
os.system("cls")
for x in symbols:
    if symbols.index(x) < base:
        for y in symbols:
            if symbols.index(y) < base:
                for z in symbols:
                    if symbols.index(z) < base:
                        if x != "0":
                            print(f", {x}{y}{z}",end="")
                        elif y != "0":
                            print(f", {y}{z}",end="")
                        elif z == "1":
                            print(f"{z}",end="")
                        elif z != "0":
                            print(f", {z}",end="")
print(".")