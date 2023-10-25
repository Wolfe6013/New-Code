while True:
    firstInput = input("first input: ")
    firstAnswer = int(input("first answer: "))

    secondInput = input("second input: ")
    secondAnswer = int(input("second answer: "))

    for x in range(-100,100):
        for y in range(-100,100):
            if firstInput == "+":
                check1 = x+y
            if firstInput == "-":
                check1 = x-y
            if firstInput == "x" or firstInput == "*":
                check1 = x*y
            if firstInput == "/":
                check1 = x/y
            if secondInput == "+":
                check2 = x+y
            if secondInput == "-":
                check2 = x-y
            if secondInput == "x" or secondInput == "*":
                check2 = x*y
            if secondInput == "/":
                check2 = x/y
            if check1 == firstAnswer:
                if check2 == secondAnswer:
                    print(x,y)
    input()