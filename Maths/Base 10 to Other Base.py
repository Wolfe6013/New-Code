#credit to https://germanna.edu/sites/default/files/2022-03/Change%20of%20Number%20Bases.pdf for the conversion maths
import math
b10 = int(input("What Number Needs Converting? "))
b_ = int(input("Base Converting To? "))

during = b10
number = []
number = list(number)

while during >= 1:
    remainder = during % b_
    during = math.floor(during/b_)
    number.insert(0,remainder)

print(f"{b10} in Base {b_} is ",end='')
for x in number:
    print(x,end="")
print(".")