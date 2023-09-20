sum = int(input("Original number: "))
i = int(input("To the power of: "))
times = int(input("Number of times: ")) 
n=0
while times > n:
    print(f" {sum}^{i} = {sum**i}")
    sum = sum ** i
    n = n+1
print("")
print("DONE!")