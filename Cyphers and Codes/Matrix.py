K: list = [[1,0],
           [0,1]]

input: str = input("Numbers: ")
decrypted: list[int] = input.split(" ")
if len(decrypted) % 2 == 1:
    decrypted.append(f"{int(0)}")
NumberOfMatrixes: int = int(len(decrypted)/2)
encrypted: list[int] = []
for x in range(NumberOfMatrixes):
    value1: int = K[0][0]
    value2: int = K[0][1]
    value3: int = K[1][0]
    value4: int = K[1][1]
    OneByOne: int = decrypted[(2*x)-2]*value1
    TwoByTwo: int = decrypted[(2*x)-1]*value2
    ThreeByOne: int = decrypted[(2*x)-2]*value3
    FourByTwo: int = decrypted[(2*x)-1]*value4
    TopMatrix = int(OneByOne+TwoByTwo)
    BottomMatrix = int(ThreeByOne+FourByTwo)
    encrypted.append(TopMatrix)
    encrypted.append(BottomMatrix)

encrypted.append((encrypted[0]))
encrypted.pop(0)
encrypted.append((encrypted[0]))
encrypted.pop(0)

for x in encrypted:
    print(f"{x} ",end="")