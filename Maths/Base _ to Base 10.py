#credit to https://germanna.edu/sites/default/files/2022-03/Change%20of%20Number%20Bases.pdf for the conversion maths

b_No = int(input("Number Converting? "))
b_ = int(input("Which Base? "))

powerOf = len(str(b_No))-1
NoList = list(str(b_No))
NoPos = 0
number = 0

while powerOf > -1:
    number += int(NoList.pop(0))*(b_**powerOf)
    powerOf -= 1

print(number)