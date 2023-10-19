symbols = ["*","-","/"]

for a in symbols:
    for b in symbols:
        for c in symbols:
            print(f"if found == False:")
            print(f"    if w{a}x{b}y{c}z == 10:")
            print(f"        print(f'[w]{a}[x]{b}[y]{c}[z] = 10')")
            print(f"        found = True")

#digitList = [w,x,y,z]
#   if found == False:
#       if w+x+y+z == 10:
#           print(f"{w}+{x}+{y}+{z} = 10")
#           found = True