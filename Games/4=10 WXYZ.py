symbols = ["+","*","-","/"]

for a in symbols:
    for b in symbols:
        for c in symbols:
            print(f"                                    if found == False:")
            print(f"                                        if '{a}' != '/' or x != 0:")
            print(f"                                            if '{b}' != '/' or y != 0:")
            print(f"                                                if '{c}' != '/' or z != 0:")
            print(f"                                                    if '{a}' not in cantSymbol:")
            print(f"                                                        if '{b}' not in cantSymbol:")
            print(f"                                                            if '{c}' not in cantSymbol:")
            print(f"                                                                if w{a}x{b}y{c}z == 10:")
            print(f"                                                                    clear()")
            print(f"                                                                    print(f'[w]{a}[x]{b}[y]{c}[z] = 10')")
            print(f"                                                                    found = True")