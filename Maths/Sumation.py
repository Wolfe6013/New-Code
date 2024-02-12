import os

while True:
    os.system("cls")
    n = int(input())
    number = 0
    for x in range(n):
        number += x
    print(number)
    input()