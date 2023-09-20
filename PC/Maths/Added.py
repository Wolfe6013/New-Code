sum = 0
i = int(input("Number added: "))
n = int(input("Number to stop at: ")) 
times = 0
while sum+i <= n:
    sum = sum + i
    print("",sum-i,"+",i,"=",sum,"     you are",n-sum,"away from finishing")
    times = times + 1
print("")
print("DONE!")
print("It got added",times,"times!")