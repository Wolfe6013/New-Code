import sys, os, time
sys.set_int_max_str_digits(99999999)
total = 95
#for x in range(2000-50):
#    var1 = 500**(x+51)
#    print(var1)
#    total += var1
#    print()
#print()
#print()
#decimalLength = 5
#decimal: str = "."
#for x in range(decimalLength):
#    decimal += str(total)[x+1]
#print(f"{str(total)[0]}{decimal}x10^{len(str(total))-1}")
for x in range(int(1312000-1)):
    total = total*95
print("DONE")
f = open("LoBabelSave.txt","w")
f.write(f"START{str(total)}END")
f.close()
print(total)
#2.344979 x10^2594773