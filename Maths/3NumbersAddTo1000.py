import random, time

found = False

while not found:
    nums = [1,2,3,4,5,6,7,8,9]
    aa = random.choice(nums)
    nums.remove(aa)
    ab = random.choice(nums)
    nums.remove(ab)
    ac = random.choice(nums)
    nums.remove(ac)
    ba = random.choice(nums)
    nums.remove(ba)
    bb = random.choice(nums)
    nums.remove(bb)
    bc = random.choice(nums)
    nums.remove(bc)
    ca = random.choice(nums)
    nums.remove(ca)
    cb = random.choice(nums)
    nums.remove(cb)
    cc = random.choice(nums)
    nums.remove(cc)
    if aa*100+ba*100+ca*100+ab*10+bb*10+cb*10+ac+bc+cc >= 99 and aa*100+ba*100+ca*100+ab*10+bb*10+cb*10+ac+bc+cc <= 101:
        print(f" {aa}{ab}{ac}")
        print(f"+{ba}{bb}{bc}")
        print(f"+{ca}{cb}{cc}")
        print(f"={aa*100+ba*100+ca*100+ab*10+bb*10+cb*10+ac+bc+cc}")
        found = True
    else:
        print(f" {aa}{ab}{ac}")
        print(f"+{ba}{bb}{bc}")
        print(f"+{ca}{cb}{cc}")
        print(f"={aa*100+ba*100+ca*100+ab*10+bb*10+cb*10+ac+bc+cc}")

total = 1

for x in range(100):
    total = total*(x+1)

print(total)