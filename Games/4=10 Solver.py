while True:
    code = input("What are the numbers? ")
    noSymbols = input("Which symbols can't you use? ")
    cantSymbol = []
    for x in noSymbols:
        cantSymbol.append(x)
    num1 = code[0]
    num2 = code[1]
    num3 = code[2]
    num4 = code[3]
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    numList = [num1,num2,num3,num4]
    found = False
    if 0 in numList:
        cantSymbol.append("/")

    for w in numList:
        for x in numList:
            for y in numList:
                for z in numList:
                    digitList = [w,x,y,z]
                    if num1 in digitList:
                        digitList.remove(num1)
                        if num2 in digitList:
                            digitList.remove(num2)
                            if num3 in digitList:
                                digitList.remove(num3)
                                if num4 in digitList:
                                    digitList.remove(num4)
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w+x+y+z == 10:
                                                        print(f'{w}+{x}+{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w+x+y*z == 10:
                                                        print(f'{w}+{x}+{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w+x+y-z == 10:
                                                        print(f'{w}+{x}+{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w+x+y/z == 10:
                                                        print(f'{w}+{x}+{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w+x*y+z == 10:
                                                        print(f'{w}+{x}*{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w+x*y*z == 10:
                                                        print(f'{w}+{x}*{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w+x*y-z == 10:
                                                        print(f'{w}+{x}*{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w+x*y/z == 10:
                                                        print(f'{w}+{x}*{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w+x-y+z == 10:
                                                        print(f'{w}+{x}-{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w+x-y*z == 10:
                                                        print(f'{w}+{x}-{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w+x-y-z == 10:
                                                        print(f'{w}+{x}-{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w+x-y/z == 10:
                                                        print(f'{w}+{x}-{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w+x/y+z == 10:
                                                        print(f'{w}+{x}/{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w+x/y*z == 10:
                                                        print(f'{w}+{x}/{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w+x/y-z == 10:
                                                        print(f'{w}+{x}/{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "+" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w+x/y/z == 10:
                                                        print(f'{w}+{x}/{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w*x+y+z == 10:
                                                        print(f'{w}*{x}+{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w*x+y*z == 10:
                                                        print(f'{w}*{x}+{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w*x+y-z == 10:
                                                        print(f'{w}*{x}+{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w*x+y/z == 10:
                                                        print(f'{w}*{x}+{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w*x*y+z == 10:
                                                        print(f'{w}*{x}*{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w*x*y*z == 10:
                                                        print(f'{w}*{x}*{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w*x*y-z == 10:
                                                        print(f'{w}*{x}*{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w*x*y/z == 10:
                                                        print(f'{w}*{x}*{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w*x-y+z == 10:
                                                        print(f'{w}*{x}-{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w*x-y*z == 10:
                                                        print(f'{w}*{x}-{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w*x-y-z == 10:
                                                        print(f'{w}*{x}-{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w*x-y/z == 10:
                                                        print(f'{w}*{x}-{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w*x/y+z == 10:
                                                        print(f'{w}*{x}/{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w*x/y*z == 10:
                                                        print(f'{w}*{x}/{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w*x/y-z == 10:
                                                        print(f'{w}*{x}/{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "*" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w*x/y/z == 10:
                                                        print(f'{w}*{x}/{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w-x+y+z == 10:
                                                        print(f'{w}-{x}+{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w-x+y*z == 10:
                                                        print(f'{w}-{x}+{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w-x+y-z == 10:
                                                        print(f'{w}-{x}+{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w-x+y/z == 10:
                                                        print(f'{w}-{x}+{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w-x*y+z == 10:
                                                        print(f'{w}-{x}*{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w-x*y*z == 10:
                                                        print(f'{w}-{x}*{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w-x*y-z == 10:
                                                        print(f'{w}-{x}*{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w-x*y/z == 10:
                                                        print(f'{w}-{x}*{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w-x-y+z == 10:
                                                        print(f'{w}-{x}-{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w-x-y*z == 10:
                                                        print(f'{w}-{x}-{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w-x-y-z == 10:
                                                        print(f'{w}-{x}-{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w-x-y/z == 10:
                                                        print(f'{w}-{x}-{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w-x/y+z == 10:
                                                        print(f'{w}-{x}/{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w-x/y*z == 10:
                                                        print(f'{w}-{x}/{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w-x/y-z == 10:
                                                        print(f'{w}-{x}/{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "-" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w-x/y/z == 10:
                                                        print(f'{w}-{x}/{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w/x+y+z == 10:
                                                        print(f'{w}/{x}+{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w/x+y*z == 10:
                                                        print(f'{w}/{x}+{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w/x+y-z == 10:
                                                        print(f'{w}/{x}+{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "+" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w/x+y/z == 10:
                                                        print(f'{w}/{x}+{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w/x*y+z == 10:
                                                        print(f'{w}/{x}*{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w/x*y*z == 10:
                                                        print(f'{w}/{x}*{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w/x*y-z == 10:
                                                        print(f'{w}/{x}*{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "*" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w/x*y/z == 10:
                                                        print(f'{w}/{x}*{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w/x-y+z == 10:
                                                        print(f'{w}/{x}-{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w/x-y*z == 10:
                                                        print(f'{w}/{x}-{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w/x-y-z == 10:
                                                        print(f'{w}/{x}-{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "-" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w/x-y/z == 10:
                                                        print(f'{w}/{x}-{y}/{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "+" not in cantSymbol:
                                                    if w/x/y+z == 10:
                                                        print(f'{w}/{x}/{y}+{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "*" not in cantSymbol:
                                                    if w/x/y*z == 10:
                                                        print(f'{w}/{x}/{y}*{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "-" not in cantSymbol:
                                                    if w/x/y-z == 10:
                                                        print(f'{w}/{x}/{y}-{z} = 10')
                                                        found = True
                                    if found == False:
                                        if "/" not in cantSymbol:
                                            if "/" not in cantSymbol:
                                                if "/" not in cantSymbol:
                                                    if w/x/y/z == 10:
                                                        print(f'{w}/{x}/{y}/{z} = 10')
                                                        found = True