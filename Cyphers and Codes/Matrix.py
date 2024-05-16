K: list = [[1,2],
           [3,4]]

input: str = input("Numbers: ")
decrypted: list[int] = input.split(" ")
if len(decrypted) % 2 == 1:
    decrypted.append(0)
print(decrypted)
NumberOfMatrixes: int = int(len(decrypted)/2)
encrypted: list[int]
for x in range(NumberOfMatrixes):
    value1 = K[0][0]
    value2 = K[0][1]
    value3 = K[1][0]
    value4 = K[1][1]
    print(value1,value2,value3,value4)
    print(f"{(int(decrypted[((2*x)-1)]*K[0][0]))+int(int(decrypted[((2*x)-1)])*int(K[1][0]))}")
    print(f"{int(decrypted[((2*x))]*K[0][1])+int(int(decrypted[(2*x)])*int(K[1][1]))}")
    TopMatrix = int(decrypted[(2*x)-1]*K[0][0])+int(decrypted[(2*x)-1]*(K[1][0]))
    BottomMatrix = int(decrypted[(2*x)]*K[0][1])+int(decrypted[(2*x)-1]*(K[1][0]))
    encrypted.append(TopMatrix)
    encrypted.append(BottomMatrix)

for x in encrypted:
    print(f"{x} ",end="")