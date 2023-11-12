symbols = ["+","*","-","/"]

for a in symbols:
    for b in symbols:
        for c in symbols:
            print(f"                                    if found == False:")
            print(f"                                        if '{a}' not in cantSymbol:")
            print(f"                                            if '{b}' not in cantSymbol:")
            print(f"                                                if '{c}' not in cantSymbol:")
            print(f"                                                    if w{a}x{b}y{c}z == 10:")
            print(f"                                                        clear()")
            print(f"                                                        print(f'[w]{a}[x]{b}[y]{c}[z] = 10')")
            print(f"                                                        found = True")

#digitList = [w,x,y,z]
#cantSymbol = []
#   if found == False:
#       if a not in cantSymbol:
#           if b not in cantSymbol:
#               if c not in cantSymbol:
#                   if w+x+y+z == 10:
#                       print(f"{w}+{x}+{y}+{z} = 10")
#                       found = True