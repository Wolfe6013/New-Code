from itertools import permutations 
list = ['0','1','2','3','4','5','6','7','8','9']
comb = permutations(list, 4)
num0 = 0
for num, x in enumerate(comb): pass
print(num+1-num0)

num = 0
for a in list:
    for b in list:
        for c in list:
            for d in list:
                num += 1
print(num)