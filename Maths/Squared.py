maxNum = int(input('What is the max digit to check? '))

for x in range(maxNum+1):
    if x % 2 == 0:
        value = 'even'
    else:
        value = 'odd'
    if x**2 % 2 == 0:
        squaredValue = 'even'
    else:
        squaredValue = 'odd'
    print(f"{x}^2 = {x**2} - {x} is {value} and {x**2} is {squaredValue}")
    if value != squaredValue:
        print("THEY AREN'T EQUAL!!!!!!")
        break